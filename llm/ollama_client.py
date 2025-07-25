"""
Ollama client for interacting with Phi-3 model
"""
import aiohttp
import json
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class OllamaClient:
    """Client for interacting with Ollama API"""
    
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url
        self.model = "phi3"
        
    async def generate(self, prompt: str, system: Optional[str] = None) -> str:
        """
        Generate a response from the Phi-3 model
        
        Args:
            prompt: The user prompt
            system: Optional system prompt
            
        Returns:
            Generated response text
        """
        url = f"{self.base_url}/api/generate"
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        
        if system:
            payload["system"] = system
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get("response", "")
                    else:
                        error_text = await response.text()
                        logger.error(f"Ollama API error: {response.status} - {error_text}")
                        return ""
        except Exception as e:
            logger.error(f"Error calling Ollama API: {e}")
            return ""
    
    async def analyze_network(self, network_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze network topology using Phi-3
        
        Args:
            network_data: Parsed network data from Visio
            
        Returns:
            Analysis results including insights and recommendations
        """
        # Prepare network summary for analysis
        device_summary = self._summarize_devices(network_data.get("shapes", []))
        connection_summary = self._summarize_connections(network_data.get("connections", []))
        
        prompt = f"""Analyze this network topology and provide insights:

Network Overview:
- Total Devices: {len(network_data.get('shapes', []))}
- Total Connections: {len(network_data.get('connections', []))}

Device Distribution:
{device_summary}

Connection Summary:
{connection_summary}

Please provide:
1. Network Architecture Assessment
2. Security Considerations
3. Performance Optimization Recommendations
4. Potential Single Points of Failure
5. Scalability Assessment
"""
        
        system_prompt = """You are a network architecture expert. Analyze network topologies and provide professional insights about security, performance, reliability, and scalability. Be specific and actionable in your recommendations."""
        
        response = await self.generate(prompt, system_prompt)
        
        # Parse the response into structured format
        analysis = self._parse_analysis(response)
        
        return analysis
    
    async def generate_executive_summary(self, network_data: Dict[str, Any]) -> str:
        """
        Generate an executive summary of the network
        """
        device_count = len(network_data.get("shapes", []))
        connection_count = len(network_data.get("connections", []))
        
        prompt = f"""Generate a concise executive summary for this network documentation:

Network: {network_data.get('title', 'Corporate Network')}
Total Devices: {device_count}
Total Connections: {connection_count}
Key Components: {self._get_key_components(network_data)}

The summary should be 3-4 sentences suitable for executives, highlighting the network's purpose, scale, and key characteristics."""
        
        return await self.generate(prompt)
    
    async def identify_security_risks(self, network_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Identify potential security risks in the network
        """
        prompt = f"""Analyze this network topology for security vulnerabilities:

Devices: {self._summarize_devices(network_data.get('shapes', []))}
Connections: {len(network_data.get('connections', []))} total

Identify:
1. Missing security controls (firewalls, IDS/IPS)
2. Exposed services or systems
3. Network segmentation issues
4. Access control concerns
5. Compliance considerations

Provide specific, actionable security recommendations."""
        
        system_prompt = "You are a cybersecurity expert specializing in network security architecture."
        
        response = await self.generate(prompt, system_prompt)
        
        return {
            "risk_assessment": response,
            "severity": self._assess_severity(response),
            "recommendations": self._extract_recommendations(response)
        }
    
    async def suggest_optimizations(self, network_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Suggest network optimizations
        """
        prompt = f"""Analyze this network for optimization opportunities:

Current Setup:
{self._describe_network(network_data)}

Suggest optimizations for:
1. Performance improvements
2. Redundancy and reliability
3. Cost optimization
4. Simplified management
5. Future scalability

Be specific about which components to add, remove, or reconfigure."""
        
        response = await self.generate(prompt)
        
        return {
            "optimizations": response,
            "priority_actions": self._extract_priority_actions(response)
        }
    
    def _summarize_devices(self, shapes: list) -> str:
        """Summarize device types and counts"""
        device_types = {}
        for shape in shapes:
            device_type = shape.get("type", "unknown")
            device_types[device_type] = device_types.get(device_type, 0) + 1
        
        summary = []
        for device_type, count in sorted(device_types.items()):
            summary.append(f"- {device_type.capitalize()}: {count}")
        
        return "\n".join(summary)
    
    def _summarize_connections(self, connections: list) -> str:
        """Summarize connection types"""
        total = len(connections)
        if total == 0:
            return "No connections defined"
        
        # Group by connection type if available
        conn_types = {}
        for conn in connections:
            conn_type = conn.get("type", "ethernet")
            conn_types[conn_type] = conn_types.get(conn_type, 0) + 1
        
        summary = [f"Total: {total} connections"]
        for conn_type, count in sorted(conn_types.items()):
            summary.append(f"- {conn_type.capitalize()}: {count}")
        
        return "\n".join(summary)
    
    def _get_key_components(self, network_data: Dict[str, Any]) -> str:
        """Extract key components for summary"""
        shapes = network_data.get("shapes", [])
        key_types = ["router", "firewall", "switch", "server"]
        
        components = []
        for shape in shapes:
            if shape.get("type") in key_types:
                components.append(f"{shape.get('type')} ({shape.get('name', 'unnamed')})")
        
        return ", ".join(components[:5])  # Limit to 5 key components
    
    def _describe_network(self, network_data: Dict[str, Any]) -> str:
        """Create a brief network description"""
        return f"""
- Devices: {self._summarize_devices(network_data.get('shapes', []))}
- Connections: {self._summarize_connections(network_data.get('connections', []))}
- Network Size: {len(network_data.get('shapes', []))} devices
"""
    
    def _parse_analysis(self, response: str) -> Dict[str, Any]:
        """Parse LLM response into structured format"""
        # Simple parsing - in production, use more sophisticated parsing
        sections = {
            "architecture_assessment": "",
            "security_considerations": "",
            "performance_recommendations": "",
            "single_points_of_failure": "",
            "scalability_assessment": ""
        }
        
        current_section = None
        lines = response.split('\n')
        
        for line in lines:
            line = line.strip()
            if "Architecture Assessment" in line:
                current_section = "architecture_assessment"
            elif "Security Considerations" in line:
                current_section = "security_considerations"
            elif "Performance" in line and "Recommendations" in line:
                current_section = "performance_recommendations"
            elif "Single Points of Failure" in line:
                current_section = "single_points_of_failure"
            elif "Scalability Assessment" in line:
                current_section = "scalability_assessment"
            elif current_section and line:
                sections[current_section] += line + "\n"
        
        return sections
    
    def _assess_severity(self, risk_text: str) -> str:
        """Assess overall security risk severity"""
        risk_keywords = {
            "critical": ["critical", "severe", "immediate", "urgent"],
            "high": ["high", "significant", "major", "important"],
            "medium": ["medium", "moderate", "should", "recommended"],
            "low": ["low", "minor", "consider", "optional"]
        }
        
        risk_text_lower = risk_text.lower()
        
        for severity, keywords in risk_keywords.items():
            if any(keyword in risk_text_lower for keyword in keywords):
                return severity
        
        return "medium"
    
    def _extract_recommendations(self, text: str) -> list:
        """Extract specific recommendations from text"""
        recommendations = []
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            # Look for numbered items or bullet points
            if line and (line[0].isdigit() or line.startswith('-') or line.startswith('•')):
                # Clean up the line
                if line[0].isdigit():
                    line = line.split('.', 1)[1].strip() if '.' in line else line
                else:
                    line = line[1:].strip()
                
                if line:
                    recommendations.append(line)
        
        return recommendations
    
    def _extract_priority_actions(self, text: str) -> list:
        """Extract priority actions from optimization text"""
        # Similar to recommendations extraction but focused on actions
        return self._extract_recommendations(text)[:5]  # Top 5 actions