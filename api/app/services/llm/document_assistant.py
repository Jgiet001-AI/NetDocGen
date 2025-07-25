"""
Document Assistant service using Ollama Phi
Focuses on improving documentation quality and clarity
"""
import os
import logging
from typing import Dict, Any, Optional, List
import aiohttp
import json

logger = logging.getLogger(__name__)

class DocumentAssistant:
    """Service for enhancing documentation quality using LLM"""
    
    def __init__(self):
        self.ollama_url = os.getenv("OLLAMA_URL", "http://ollama:11434")
        self.model = "phi"
        
    async def enhance_documentation(self, parsed_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Enhance documentation quality with better descriptions and organization
        
        Args:
            parsed_data: Parsed network data from Visio
            
        Returns:
            Enhanced documentation content
        """
        try:
            # Generate documentation enhancements
            executive_summary = await self._generate_executive_summary(parsed_data)
            glossary = await self._generate_glossary(parsed_data)
            device_descriptions = await self._enhance_device_descriptions(parsed_data)
            connection_explanations = await self._explain_connections(parsed_data)
            documentation_sections = await self._suggest_documentation_structure(parsed_data)
            
            return {
                "executive_summary": executive_summary,
                "glossary": glossary,
                "enhanced_devices": device_descriptions,
                "connection_explanations": connection_explanations,
                "suggested_sections": documentation_sections,
                "generated_by": "Phi AI Documentation Assistant"
            }
        except Exception as e:
            logger.error(f"Error enhancing documentation: {e}")
            return self._get_fallback_content(parsed_data)
    
    async def _call_ollama(self, prompt: str, system: Optional[str] = None) -> str:
        """Make a call to Ollama API"""
        url = f"{self.ollama_url}/api/generate"
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.3,  # Lower temperature for more consistent documentation
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
        except Exception as e:
            logger.error(f"Error calling Ollama: {e}")
            return ""
    
    async def _generate_executive_summary(self, data: Dict[str, Any]) -> str:
        """Generate a clear executive summary for the documentation"""
        device_count = len(data.get("shapes", []))
        connection_count = len(data.get("connections", []))
        
        # Count device types
        device_types = {}
        for shape in data.get("shapes", []):
            device_type = shape.get("shape_type", "unknown")
            device_types[device_type] = device_types.get(device_type, 0) + 1
        
        device_summary = ", ".join([f"{count} {dtype}(s)" for dtype, count in device_types.items()])
        
        prompt = f"""Write a clear, professional executive summary for network documentation:

Network: {data.get('project_name', 'Network Infrastructure')}
Total Devices: {device_count}
Total Connections: {connection_count}
Device Types: {device_summary}

Create a 3-4 paragraph executive summary that:
1. Describes what this network diagram represents
2. Summarizes the key components and their quantities
3. Explains the documentation's purpose and scope
4. Uses clear, non-technical language suitable for all stakeholders

Focus on describing WHAT is documented, not HOW the network should be designed."""
        
        system_prompt = "You are a technical writer creating clear, professional documentation. Focus on describing the existing network clearly without making design recommendations."
        
        summary = await self._call_ollama(prompt, system_prompt)
        
        if not summary:
            summary = f"This documentation covers a network infrastructure consisting of {device_count} devices connected through {connection_count} network links. The network includes {device_summary}."
        
        return summary
    
    async def _generate_glossary(self, data: Dict[str, Any]) -> List[Dict[str, str]]:
        """Generate a glossary of technical terms found in the network"""
        # Extract unique technical terms
        terms = set()
        
        # From device types
        for shape in data.get("shapes", []):
            terms.add(shape.get("shape_type", ""))
            # Extract terms from properties
            if "properties" in shape and "text" in shape["properties"]:
                text = shape["properties"]["text"]
                # Look for common network terms
                for word in ["VLAN", "IP", "BGP", "OSPF", "DNS", "DHCP", "NAT", "VPN"]:
                    if word in text.upper():
                        terms.add(word)
        
        # From connection types
        for conn in data.get("connections", []):
            conn_type = conn.get("connection_type", "")
            if conn_type:
                terms.add(conn_type)
        
        terms.discard("")  # Remove empty strings
        terms_list = sorted(list(terms))
        
        if not terms_list:
            return []
        
        prompt = f"""Create a glossary for these networking terms found in the documentation:

Terms: {', '.join(terms_list)}

For each term, provide:
1. The term
2. A clear, concise definition (1-2 sentences)
3. How it relates to this network documentation

Format each entry as:
TERM: Definition here. In this network: context here.

Keep definitions simple and avoid technical jargon where possible."""
        
        response = await self._call_ollama(prompt)
        
        # Parse response into glossary entries
        glossary = []
        if response:
            lines = response.split('\n')
            for line in lines:
                if ':' in line and line.strip():
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        term = parts[0].strip()
                        definition = parts[1].strip()
                        if term and definition:
                            glossary.append({
                                "term": term,
                                "definition": definition
                            })
        
        return glossary
    
    async def _enhance_device_descriptions(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate better descriptions for devices"""
        shapes = data.get("shapes", [])[:20]  # Limit to first 20 devices
        
        if not shapes:
            return []
        
        # Group devices by type
        devices_by_type = {}
        for shape in shapes:
            device_type = shape.get("shape_type", "unknown")
            if device_type not in devices_by_type:
                devices_by_type[device_type] = []
            devices_by_type[device_type].append(shape)
        
        prompt = f"""Create clear, professional descriptions for these network devices:

{self._format_devices_for_prompt(devices_by_type)}

For each device, provide:
1. A clear description of what the device is
2. Its role in the network (based on its name and type)
3. Key identifying information

Format: DEVICE_NAME: Description here.

Keep descriptions factual and focused on documentation clarity."""
        
        response = await self._call_ollama(prompt)
        
        # Parse and match descriptions to devices
        enhanced_devices = []
        if response:
            # Create a simple mapping of descriptions
            descriptions = {}
            lines = response.split('\n')
            for line in lines:
                if ':' in line:
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        device_name = parts[0].strip()
                        description = parts[1].strip()
                        descriptions[device_name] = description
            
            # Apply descriptions to devices
            for shape in shapes:
                device_name = shape.get("name", "")
                enhanced_devices.append({
                    "id": shape.get("id"),
                    "name": device_name,
                    "type": shape.get("shape_type"),
                    "description": descriptions.get(device_name, f"A {shape.get('shape_type', 'network')} device in the infrastructure"),
                    "properties": shape.get("properties", {})
                })
        
        return enhanced_devices
    
    async def _explain_connections(self, data: Dict[str, Any]) -> Dict[str, str]:
        """Generate explanations for different connection types"""
        connections = data.get("connections", [])
        
        # Get unique connection types
        connection_types = set()
        for conn in connections:
            conn_type = conn.get("connection_type", "")
            if conn_type:
                connection_types.add(conn_type)
        
        if not connection_types:
            return {}
        
        prompt = f"""Explain these network connection types for documentation:

Connection types: {', '.join(sorted(connection_types))}

For each connection type, provide:
1. What it is
2. Common uses in networking
3. Key characteristics (speed, medium, purpose)

Format: CONNECTION_TYPE: Explanation here.

Keep explanations clear and educational."""
        
        response = await self._call_ollama(prompt)
        
        explanations = {}
        if response:
            lines = response.split('\n')
            for line in lines:
                if ':' in line:
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        conn_type = parts[0].strip().lower()
                        explanation = parts[1].strip()
                        explanations[conn_type] = explanation
        
        return explanations
    
    async def _suggest_documentation_structure(self, data: Dict[str, Any]) -> List[Dict[str, str]]:
        """Suggest documentation sections based on the network content"""
        device_count = len(data.get("shapes", []))
        device_types = set(shape.get("shape_type", "") for shape in data.get("shapes", []))
        
        prompt = f"""Suggest documentation sections for a network with:
- {device_count} devices
- Device types: {', '.join(sorted(device_types))}

Provide 5-7 recommended documentation sections that would help readers understand this network.
For each section:
1. Section title
2. Brief description of what it should contain

Format: SECTION_TITLE: Description

Focus on documentation organization, not network design."""
        
        response = await self._call_ollama(prompt)
        
        sections = []
        if response:
            lines = response.split('\n')
            for line in lines:
                if ':' in line and line.strip():
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        title = parts[0].strip()
                        description = parts[1].strip()
                        if title and description:
                            sections.append({
                                "title": title,
                                "description": description
                            })
        
        # Add default sections if none generated
        if not sections:
            sections = [
                {"title": "Overview", "description": "High-level summary of the network infrastructure"},
                {"title": "Device Inventory", "description": "Complete list of all network devices"},
                {"title": "Network Topology", "description": "Visual representation and connection details"},
                {"title": "Device Details", "description": "Specifications and configurations for each device"},
                {"title": "Appendices", "description": "Additional technical information and references"}
            ]
        
        return sections
    
    def _format_devices_for_prompt(self, devices_by_type: Dict[str, List]) -> str:
        """Format devices for LLM prompt"""
        output = []
        for device_type, devices in devices_by_type.items():
            output.append(f"\n{device_type.upper()} devices:")
            for device in devices[:5]:  # Limit per type
                name = device.get("name", "Unnamed")
                props = device.get("properties", {})
                text = props.get("text", "")
                output.append(f"- {name}: {text[:50] if text else 'No additional info'}")
        
        return "\n".join(output)
    
    def _get_fallback_content(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Provide fallback content if LLM is unavailable"""
        device_count = len(data.get("shapes", []))
        connection_count = len(data.get("connections", []))
        
        return {
            "executive_summary": f"This documentation describes a network infrastructure containing {device_count} devices and {connection_count} connections.",
            "glossary": [
                {"term": "Router", "definition": "A network device that forwards data packets between computer networks"},
                {"term": "Switch", "definition": "A network device that connects devices within a network"},
                {"term": "Firewall", "definition": "A security device that monitors and controls network traffic"}
            ],
            "enhanced_devices": [],
            "connection_explanations": {
                "ethernet": "Standard wired network connection using copper or fiber cables",
                "fiber": "High-speed optical connection for long distances and high bandwidth",
                "vpn": "Secure encrypted connection over public networks"
            },
            "suggested_sections": [
                {"title": "Network Overview", "description": "Summary of the network infrastructure"},
                {"title": "Device Inventory", "description": "List of all network components"},
                {"title": "Connection Details", "description": "Network topology and links"}
            ],
            "generated_by": "Fallback Content (LLM Unavailable)"
        }