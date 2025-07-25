"""
Network Analyzer service using Ollama Phi-3
"""
import os
import logging
from typing import Dict, Any, Optional
import aiohttp
import json

logger = logging.getLogger(__name__)

class NetworkAnalyzer:
    """Service for analyzing network topologies using LLM"""
    
    def __init__(self):
        self.ollama_url = os.getenv("OLLAMA_URL", "http://ollama:11434")
        self.model = "phi3"
        
    async def analyze_network(self, parsed_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze network topology and generate insights
        
        Args:
            parsed_data: Parsed network data from Visio
            
        Returns:
            Analysis results with insights and recommendations
        """
        try:
            # Generate various analyses
            executive_summary = await self._generate_executive_summary(parsed_data)
            architecture_analysis = await self._analyze_architecture(parsed_data)
            security_assessment = await self._assess_security(parsed_data)
            optimization_suggestions = await self._suggest_optimizations(parsed_data)
            
            return {
                "executive_summary": executive_summary,
                "architecture_analysis": architecture_analysis,
                "security_assessment": security_assessment,
                "optimization_suggestions": optimization_suggestions,
                "generated_by": "Phi-3 AI Analysis"
            }
        except Exception as e:
            logger.error(f"Error analyzing network: {e}")
            return self._get_fallback_analysis(parsed_data)
    
    async def _call_ollama(self, prompt: str, system: Optional[str] = None) -> str:
        """Make a call to Ollama API"""
        url = f"{self.ollama_url}/api/generate"
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9
            }
        }
        
        if system:
            payload["system"] = system
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload, timeout=30) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get("response", "")
                    else:
                        logger.error(f"Ollama API error: {response.status}")
                        return ""
        except aiohttp.ClientError as e:
            logger.error(f"Error calling Ollama: {e}")
            return ""
        except Exception as e:
            logger.error(f"Unexpected error calling Ollama: {e}")
            return ""
    
    async def _generate_executive_summary(self, data: Dict[str, Any]) -> str:
        """Generate executive summary"""
        device_count = len(data.get("shapes", []))
        connection_count = len(data.get("connections", []))
        
        # Count device types
        device_types = {}
        for shape in data.get("shapes", []):
            device_type = shape.get("type", "unknown")
            device_types[device_type] = device_types.get(device_type, 0) + 1
        
        device_summary = ", ".join([f"{count} {dtype}(s)" for dtype, count in device_types.items()])
        
        prompt = f"""Generate a professional executive summary for this network documentation:

Network: {data.get('title', 'Enterprise Network')}
Total Devices: {device_count}
Total Connections: {connection_count}
Device Types: {device_summary}

Create a 3-4 sentence executive summary that:
1. Describes the network's purpose and scale
2. Highlights key infrastructure components
3. Notes the overall architecture approach
4. Is suitable for C-level executives

Keep it concise and business-focused."""
        
        summary = await self._call_ollama(prompt)
        
        if not summary:
            # Fallback summary
            summary = f"This network infrastructure consists of {device_count} devices connected through {connection_count} links. The architecture includes {device_summary}, providing a comprehensive networking solution."
        
        return summary
    
    async def _analyze_architecture(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze network architecture"""
        shapes = data.get("shapes", [])
        connections = data.get("connections", [])
        
        # Build device and connection summaries
        device_info = self._build_device_summary(shapes)
        connection_info = self._build_connection_summary(connections, shapes)
        
        prompt = f"""Analyze this network architecture:

Devices:
{device_info}

Connections:
{connection_info}

Provide analysis covering:
1. Architecture Pattern (e.g., hierarchical, flat, hybrid)
2. Design Strengths
3. Design Weaknesses
4. Redundancy Assessment
5. Scalability Potential

Format as clear sections with bullet points."""
        
        system_prompt = "You are a senior network architect. Provide professional, technical analysis focused on architecture patterns and best practices."
        
        analysis_text = await self._call_ollama(prompt, system_prompt)
        
        if not analysis_text:
            return self._get_fallback_architecture_analysis(shapes, connections)
        
        # Parse the response into sections
        return self._parse_architecture_analysis(analysis_text)
    
    async def _assess_security(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Assess network security"""
        shapes = data.get("shapes", [])
        
        # Check for security devices
        security_devices = [s for s in shapes if s.get("type") in ["firewall", "ids", "ips"]]
        
        prompt = f"""Perform a security assessment of this network:

Total Devices: {len(shapes)}
Security Devices Found: {len(security_devices)}
Device Types: {self._count_device_types(shapes)}

Assess:
1. Perimeter Security
2. Internal Segmentation
3. Access Control Points
4. Missing Security Controls
5. Compliance Considerations (general)

Provide specific security recommendations and identify critical gaps."""
        
        system_prompt = "You are a cybersecurity expert. Focus on identifying security risks and providing actionable recommendations."
        
        assessment = await self._call_ollama(prompt, system_prompt)
        
        if not assessment:
            return self._get_fallback_security_assessment(shapes)
        
        return {
            "assessment": assessment,
            "risk_level": self._determine_risk_level(assessment, security_devices),
            "has_firewall": any(s.get("type") == "firewall" for s in shapes),
            "security_device_count": len(security_devices)
        }
    
    async def _suggest_optimizations(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Suggest network optimizations"""
        shapes = data.get("shapes", [])
        connections = data.get("connections", [])
        
        # Analyze current state
        device_counts = self._count_device_types(shapes)
        avg_connections = len(connections) / len(shapes) if shapes else 0
        
        prompt = f"""Suggest optimizations for this network:

Current Configuration:
- Devices: {len(shapes)}
- Connections: {len(connections)}
- Average connections per device: {avg_connections:.1f}
- Device distribution: {device_counts}

Provide optimization suggestions for:
1. Performance Improvements
2. Redundancy Enhancements
3. Cost Optimization
4. Management Simplification
5. Future Growth Planning

Be specific and practical in recommendations."""
        
        suggestions = await self._call_ollama(prompt)
        
        if not suggestions:
            return self._get_fallback_optimizations(shapes, connections)
        
        return {
            "suggestions": suggestions,
            "priority_items": self._extract_priority_items(suggestions)
        }
    
    def _build_device_summary(self, shapes: list) -> str:
        """Build a summary of devices"""
        if not shapes:
            return "No devices found"
        
        summary = []
        for shape in shapes[:10]:  # Limit to first 10 for prompt size
            summary.append(f"- {shape.get('name', 'Unnamed')}: {shape.get('type', 'unknown')} device")
        
        if len(shapes) > 10:
            summary.append(f"... and {len(shapes) - 10} more devices")
        
        return "\n".join(summary)
    
    def _build_connection_summary(self, connections: list, shapes: list) -> str:
        """Build a summary of connections"""
        if not connections:
            return "No connections defined"
        
        # Create shape lookup
        shape_lookup = {s.get("id"): s.get("name", s.get("id")) for s in shapes}
        
        summary = []
        for conn in connections[:10]:  # Limit for prompt size
            source = shape_lookup.get(conn.get("source"), "Unknown")
            target = shape_lookup.get(conn.get("target"), "Unknown")
            conn_type = conn.get("type", "unknown")
            summary.append(f"- {source} -> {target} ({conn_type})")
        
        if len(connections) > 10:
            summary.append(f"... and {len(connections) - 10} more connections")
        
        return "\n".join(summary)
    
    def _count_device_types(self, shapes: list) -> Dict[str, int]:
        """Count devices by type"""
        counts = {}
        for shape in shapes:
            device_type = shape.get("type", "unknown")
            counts[device_type] = counts.get(device_type, 0) + 1
        return counts
    
    def _parse_architecture_analysis(self, text: str) -> Dict[str, Any]:
        """Parse architecture analysis text into structured format"""
        sections = {
            "pattern": "",
            "strengths": [],
            "weaknesses": [],
            "redundancy": "",
            "scalability": ""
        }
        
        current_section = None
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Detect sections
            if "pattern" in line.lower() and "architecture" in line.lower():
                current_section = "pattern"
            elif "strength" in line.lower():
                current_section = "strengths"
            elif "weakness" in line.lower():
                current_section = "weaknesses"
            elif "redundancy" in line.lower():
                current_section = "redundancy"
            elif "scalability" in line.lower():
                current_section = "scalability"
            elif current_section:
                # Add content to current section
                if line.startswith(('-', '•', '*')) or (line and line[0].isdigit() and '.' in line):
                    clean_line = line.lstrip('-•*').strip()
                    if line[0].isdigit():
                        clean_line = line.split('.', 1)[1].strip() if '.' in line else line
                    
                    if current_section in ["strengths", "weaknesses"]:
                        sections[current_section].append(clean_line)
                    else:
                        sections[current_section] += clean_line + " "
        
        return sections
    
    def _determine_risk_level(self, assessment: str, security_devices: list) -> str:
        """Determine overall risk level"""
        assessment_lower = assessment.lower()
        
        # Check for risk indicators
        if any(word in assessment_lower for word in ["critical", "severe", "urgent", "immediate"]):
            return "critical"
        elif any(word in assessment_lower for word in ["high risk", "significant", "major"]):
            return "high"
        elif len(security_devices) == 0:
            return "high"
        elif any(word in assessment_lower for word in ["moderate", "medium risk", "some concerns"]):
            return "medium"
        else:
            return "low"
    
    def _extract_priority_items(self, suggestions: str) -> list:
        """Extract priority optimization items"""
        priority_items = []
        lines = suggestions.split('\n')
        
        for line in lines:
            line = line.strip()
            if line and (line[0].isdigit() or line.startswith(('-', '•'))):
                # Clean and add
                if line[0].isdigit() and '.' in line:
                    line = line.split('.', 1)[1].strip()
                else:
                    line = line.lstrip('-•').strip()
                
                if line and len(priority_items) < 5:  # Top 5 items
                    priority_items.append(line)
        
        return priority_items
    
    def _get_fallback_analysis(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Provide fallback analysis if LLM is unavailable"""
        device_count = len(data.get("shapes", []))
        connection_count = len(data.get("connections", []))
        
        return {
            "executive_summary": f"Network infrastructure containing {device_count} devices and {connection_count} connections.",
            "architecture_analysis": {
                "pattern": "Standard enterprise network",
                "strengths": ["Structured topology", "Clear device roles"],
                "weaknesses": ["Requires detailed analysis"],
                "redundancy": "Manual review required",
                "scalability": "Depends on current utilization"
            },
            "security_assessment": {
                "assessment": "Security assessment requires manual review",
                "risk_level": "medium",
                "has_firewall": any(s.get("type") == "firewall" for s in data.get("shapes", [])),
                "security_device_count": len([s for s in data.get("shapes", []) if s.get("type") in ["firewall", "ids", "ips"]])
            },
            "optimization_suggestions": {
                "suggestions": "Optimization analysis requires manual review",
                "priority_items": ["Review current capacity", "Assess redundancy needs", "Evaluate security posture"]
            },
            "generated_by": "Fallback Analysis (LLM Unavailable)"
        }
    
    def _get_fallback_architecture_analysis(self, shapes: list, connections: list) -> Dict[str, Any]:
        """Fallback architecture analysis"""
        return {
            "pattern": "Network topology identified",
            "strengths": [
                f"Contains {len(shapes)} network devices",
                f"Has {len(connections)} defined connections"
            ],
            "weaknesses": ["Requires manual architecture review"],
            "redundancy": "Manual assessment needed",
            "scalability": "Based on current device count and connections"
        }
    
    def _get_fallback_security_assessment(self, shapes: list) -> Dict[str, Any]:
        """Fallback security assessment"""
        security_devices = [s for s in shapes if s.get("type") in ["firewall", "ids", "ips"]]
        
        return {
            "assessment": f"Network contains {len(security_devices)} security devices. Manual security review recommended.",
            "risk_level": "high" if len(security_devices) == 0 else "medium",
            "has_firewall": any(s.get("type") == "firewall" for s in shapes),
            "security_device_count": len(security_devices)
        }
    
    def _get_fallback_optimizations(self, shapes: list, connections: list) -> Dict[str, Any]:
        """Fallback optimization suggestions"""
        avg_connections = len(connections) / len(shapes) if shapes else 0
        
        suggestions = []
        if avg_connections < 2:
            suggestions.append("Consider adding redundant connections")
        if len([s for s in shapes if s.get("type") == "firewall"]) == 0:
            suggestions.append("Add firewall for security")
        
        return {
            "suggestions": "Manual optimization review recommended",
            "priority_items": suggestions or ["Review network design", "Assess performance metrics"]
        }