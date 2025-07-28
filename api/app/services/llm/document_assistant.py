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
        
        # Count device types and analyze network characteristics
        device_types = {}
        security_devices = 0
        network_devices = 0
        server_devices = 0
        
        for shape in data.get("shapes", []):
            device_type = shape.get("shape_type", "unknown")
            device_name = shape.get("name", "").lower()
            device_types[device_type] = device_types.get(device_type, 0) + 1
            
            # Categorize devices for better summary
            if any(term in device_name for term in ['firewall', 'fw', 'asa', 'palo', 'fortinet']):
                security_devices += 1
            elif any(term in device_name for term in ['switch', 'router', 'sw', 'rtr']):
                network_devices += 1
            elif any(term in device_name for term in ['server', 'srv', 'vm', 'host']):
                server_devices += 1
        
        # Determine network complexity
        complexity = "simple"
        if device_count > 20:
            complexity = "large-scale"
        elif device_count > 10:
            complexity = "medium-scale"
        elif device_count > 5:
            complexity = "moderate"
        
        # Calculate redundancy indicators
        redundancy_factor = (connection_count / device_count) if device_count > 0 else 0
        redundancy_level = "minimal"
        if redundancy_factor > 3:
            redundancy_level = "high"
        elif redundancy_factor > 2:
            redundancy_level = "moderate"
        
        device_summary = ", ".join([f"{count} {dtype}(s)" for dtype, count in device_types.items()])
        
        prompt = f"""Write a comprehensive, professional executive summary for enterprise network documentation:

Network Overview:
- Project: {data.get('project_name', 'Network Infrastructure Implementation')}
- Scale: {complexity} infrastructure with {device_count} devices
- Connectivity: {connection_count} network connections (redundancy level: {redundancy_level})
- Device Breakdown: {device_summary}
- Security Components: {security_devices} security devices
- Network Infrastructure: {network_devices} networking devices  
- Compute Resources: {server_devices} servers/hosts

Create a 4-5 paragraph executive summary that:

1. **Opening Statement**: Clearly state what this documentation represents and its business purpose
2. **Infrastructure Overview**: Describe the scale, complexity, and key characteristics of the network
3. **Key Components**: Highlight critical infrastructure elements including security, networking, and compute resources
4. **Documentation Value**: Explain how this documentation supports operations, maintenance, and strategic planning
5. **Summary Statement**: Conclude with the documentation's role in infrastructure management

Writing Requirements:
- Use professional, executive-level language
- Include specific metrics and quantities where relevant
- Focus on business value and operational importance
- Avoid technical jargon while maintaining accuracy
- Structure for easy scanning by executives and technical staff
- Emphasize what EXISTS, not what should be implemented"""
        
        system_prompt = "You are a senior technical documentation specialist creating executive-level infrastructure documentation. Your writing should be authoritative, clear, and valuable to both technical and business stakeholders. Focus on factual description of existing infrastructure with emphasis on business value and operational significance."
        
        summary = await self._call_ollama(prompt, system_prompt)
        
        if not summary:
            summary = f"""This documentation provides a comprehensive overview of a {complexity} network infrastructure implementation. 

The documented network consists of {device_count} interconnected devices operating across {connection_count} network connections, providing {redundancy_level} redundancy for business continuity. The infrastructure includes {device_summary}, representing a balanced approach to networking, security, and compute resources.

This documentation serves as the authoritative reference for network operations, maintenance planning, and strategic infrastructure decisions. It provides detailed insights into device configurations, network topology, and connectivity patterns essential for effective infrastructure management.

The comprehensive nature of this documentation supports both day-to-day operational requirements and long-term strategic planning initiatives, ensuring optimal network performance and reliability."""
        
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
        """Generate better descriptions for devices with intelligent analysis"""
        shapes = data.get("shapes", [])[:25]  # Increased limit for better coverage
        
        if not shapes:
            return []
        
        # Analyze and categorize devices more intelligently
        devices_by_category = self._categorize_devices_intelligently(shapes)
        
        prompt = f"""Create comprehensive, professional descriptions for these network infrastructure devices:

{self._format_devices_for_enhanced_prompt(devices_by_category)}

For each device, provide a detailed description that includes:

1. **Device Function**: What the device does in the network
2. **Strategic Role**: Its importance in the overall infrastructure
3. **Technical Characteristics**: Key technical attributes based on its type and name
4. **Operational Context**: How it fits into network operations
5. **Dependencies**: What other devices or services it likely depends on

Format each description as:
DEVICE_NAME: [Comprehensive description addressing all points above]

Requirements:
- Use professional, technical language appropriate for network documentation
- Infer intelligent details from device names and types
- Consider device placement in network hierarchy
- Address both technical and operational aspects
- Focus on existing capabilities, not recommendations
- Include any apparent redundancy or high-availability considerations"""
        
        system_prompt = "You are a senior network engineer and technical writer creating detailed device documentation. Your descriptions should demonstrate deep understanding of network infrastructure, device roles, and operational considerations. Write for an audience of network engineers, architects, and operations teams."
        
        response = await self._call_ollama(prompt, system_prompt)
        
        # Parse and match descriptions to devices
        enhanced_devices = []
        if response:
            descriptions = self._parse_device_descriptions(response)
            
            # Apply enhanced descriptions to devices
            for shape in shapes:
                device_name = shape.get("name", "")
                device_type = shape.get("shape_type", "unknown")
                
                # Generate intelligent fallback description if not in response
                fallback_desc = self._generate_intelligent_fallback_description(shape)
                
                enhanced_devices.append({
                    "id": shape.get("id"),
                    "name": device_name,
                    "type": device_type,
                    "description": descriptions.get(device_name, fallback_desc),
                    "properties": shape.get("properties", {}),
                    "category": self._determine_device_category(shape),
                    "criticality": self._assess_device_criticality(shape, data)
                })
        
        return enhanced_devices
        
    def _categorize_devices_intelligently(self, shapes: List[Dict]) -> Dict[str, List[Dict]]:
        """Intelligently categorize devices for better description generation"""
        categories = {
            "Core Infrastructure": [],
            "Distribution/Aggregation": [],
            "Access Layer": [],
            "Security Appliances": [],
            "Routing Infrastructure": [],
            "Wireless Infrastructure": [],
            "Compute Resources": [],
            "Storage Systems": [],
            "Management/Monitoring": [],
            "Other/Unknown": []
        }
        
        for shape in shapes:
            name = shape.get("name", "").lower()
            shape_type = shape.get("shape_type", "").lower()
            
            if any(term in name for term in ['core', 'c-', 'cr-', 'spine']):
                categories["Core Infrastructure"].append(shape)
            elif any(term in name for term in ['dist', 'distribution', 'd-', 'dr-', 'aggr', 'leaf']):
                categories["Distribution/Aggregation"].append(shape)
            elif any(term in name for term in ['access', 'acc', 'a-', 'edge']):
                categories["Access Layer"].append(shape)
            elif any(term in name for term in ['fw', 'firewall', 'asa', 'palo', 'fortigate', 'security']):
                categories["Security Appliances"].append(shape)
            elif any(term in name for term in ['rtr', 'router', 'r-', 'wan', 'border']):
                categories["Routing Infrastructure"].append(shape)
            elif any(term in name for term in ['wlc', 'wireless', 'wifi', 'ap', 'controller']):
                categories["Wireless Infrastructure"].append(shape)
            elif any(term in name for term in ['srv', 'server', 'vm', 'host', 'compute']):
                categories["Compute Resources"].append(shape)
            elif any(term in name for term in ['san', 'nas', 'storage', 'disk']):
                categories["Storage Systems"].append(shape)
            elif any(term in name for term in ['mgmt', 'monitor', 'nms', 'snmp']):
                categories["Management/Monitoring"].append(shape)
            else:
                categories["Other/Unknown"].append(shape)
        
        # Remove empty categories
        return {k: v for k, v in categories.items() if v}
        
    def _format_devices_for_enhanced_prompt(self, devices_by_category: Dict[str, List]) -> str:
        """Format devices for enhanced LLM prompt"""
        output = []
        for category, devices in devices_by_category.items():
            if devices:
                output.append(f"\n{category.upper()}:")
                for device in devices[:8]:  # Limit per category
                    name = device.get("name", "Unnamed")
                    shape_type = device.get("shape_type", "Unknown")
                    props = device.get("properties", {})
                    text = props.get("text", "")
                    output.append(f"- {name} (Type: {shape_type}): {text[:100] if text else 'No additional info'}")
        
        return "\n".join(output)
        
    def _parse_device_descriptions(self, response: str) -> Dict[str, str]:
        """Parse LLM response to extract device descriptions"""
        descriptions = {}
        lines = response.split('\n')
        current_device = None
        current_description = []
        
        for line in lines:
            line = line.strip()
            if ':' in line and not line.startswith(' '):
                # New device description
                if current_device and current_description:
                    descriptions[current_device] = ' '.join(current_description)
                
                parts = line.split(':', 1)
                if len(parts) == 2:
                    current_device = parts[0].strip()
                    current_description = [parts[1].strip()] if parts[1].strip() else []
            elif current_device and line:
                # Continuation of current description
                current_description.append(line)
        
        # Add the last device
        if current_device and current_description:
            descriptions[current_device] = ' '.join(current_description)
        
        return descriptions
        
    def _generate_intelligent_fallback_description(self, shape: Dict) -> str:
        """Generate intelligent fallback description when LLM doesn't provide one"""
        name = shape.get("name", "Unnamed Device")
        shape_type = shape.get("shape_type", "network device")
        
        # Determine role from name
        name_lower = name.lower()
        if any(term in name_lower for term in ['core', 'c-']):
            role = "core infrastructure device providing high-speed backbone connectivity"
        elif any(term in name_lower for term in ['dist', 'distribution']):
            role = "distribution layer device aggregating access layer connections"
        elif any(term in name_lower for term in ['access', 'acc']):
            role = "access layer device providing end-user connectivity"
        elif any(term in name_lower for term in ['fw', 'firewall']):
            role = "security appliance providing network protection and traffic filtering"
        elif any(term in name_lower for term in ['rtr', 'router']):
            role = "routing device managing inter-network communication"
        else:
            role = f"{shape_type} supporting network operations"
        
        return f"{name} is a {role}. This device plays a critical role in the network infrastructure, providing essential connectivity and services to support business operations."
        
    def _determine_device_category(self, shape: Dict) -> str:
        """Determine device category for documentation organization"""
        name = shape.get("name", "").lower()
        
        if any(term in name for term in ['core', 'spine']):
            return "Core"
        elif any(term in name for term in ['dist', 'leaf']):
            return "Distribution"
        elif any(term in name for term in ['access', 'edge']):
            return "Access"
        elif any(term in name for term in ['fw', 'firewall']):
            return "Security"
        elif any(term in name for term in ['rtr', 'router']):
            return "Routing"
        else:
            return "Infrastructure"
            
    def _assess_device_criticality(self, shape: Dict, data: Dict) -> str:
        """Assess device criticality for documentation"""
        # Simple criticality assessment based on connections and role
        connections = data.get("connections", [])
        device_id = shape.get("id")
        
        connection_count = sum(1 for conn in connections 
                             if conn.get("source_id") == device_id or conn.get("target_id") == device_id)
        
        name = shape.get("name", "").lower()
        
        # Core devices are typically critical
        if any(term in name for term in ['core', 'spine']) or connection_count > 5:
            return "Critical"
        elif any(term in name for term in ['dist', 'leaf']) or connection_count > 2:
            return "High"
        else:
            return "Medium"
    
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
    
    async def _suggest_network_design(self, data: Dict[str, Any]) -> List[str]:
        """Suggest network design pattern based on topology"""
        shapes = data.get("shapes", [])
        connections = data.get("connections", [])
        
        if not shapes or not connections:
            return []
        
        # Analyze device names, types, and connections
        device_names = [s.get("name", "").lower() for s in shapes]
        device_types = [s.get("shape_type", "").lower() for s in shapes]
        device_count = len(shapes)
        connection_count = len(connections)
        
        # Calculate network characteristics
        avg_connections = (2 * connection_count) / device_count if device_count > 0 else 0
        
        # Extract device role indicators
        role_indicators = []
        for name in device_names:
            if any(term in name for term in ['core', 'c-', 'cr-']):
                role_indicators.append('core')
            elif any(term in name for term in ['dist', 'distribution', 'd-', 'dr-']):
                role_indicators.append('distribution')
            elif any(term in name for term in ['access', 'acc', 'a-', 'sw-']):
                role_indicators.append('access')
            elif any(term in name for term in ['spine', 'leaf']):
                role_indicators.append('datacenter')
            elif any(term in name for term in ['fw', 'firewall', 'asa', 'palo']):
                role_indicators.append('security')
            elif any(term in name for term in ['rtr', 'router', 'r-', 'wan']):
                role_indicators.append('routing')
        
        prompt = f"""Analyze this network topology and suggest the most likely design patterns:

Network Analysis:
- Device count: {device_count}
- Connection count: {connection_count}
- Average connections per device: {avg_connections:.2f}
- Device types found: {', '.join(set(device_types)) if device_types else 'Unknown'}
- Role indicators in names: {', '.join(set(role_indicators)) if role_indicators else 'None'}
- Sample device names: {', '.join([name for name in device_names[:5] if name])}

Analyze for these topology patterns:
1. Three-Tier Hierarchical: Core, Distribution, Access layers clearly separated
2. Collapsed Core: Core and distribution functions combined
3. Spine-Leaf: Data center with spine and leaf switches
4. Hub and Spoke: Central hub with multiple spokes
5. Full/Partial Mesh: High interconnectivity between devices
6. Star: Central device with devices radiating out
7. Ring: Devices connected in a loop
8. Campus Network: Multiple buildings/areas with interconnects
9. WAN/Branch: Wide area connections between sites
10. DMZ/Security Focused: Security appliances prominent
11. Hybrid: Combination of multiple patterns

Based on the device names, types, connection patterns, and network characteristics, suggest the 3 most likely patterns with confidence levels."""

        response = await self._call_ollama(prompt)
        
        if response:
            # Extract pattern suggestions with broader pattern matching
            patterns = []
            pattern_mapping = {
                "three_tier": ["three-tier", "hierarchical", "three tier"],
                "collapsed_core": ["collapsed core", "collapsed-core", "two-tier"],
                "spine_leaf": ["spine-leaf", "spine leaf", "data center", "datacenter"],
                "hub_spoke": ["hub and spoke", "hub-spoke", "hub spoke"],
                "mesh": ["mesh", "full mesh", "partial mesh"],
                "star": ["star", "star topology"],
                "ring": ["ring", "ring topology"],
                "campus": ["campus", "campus network"],
                "wan": ["wan", "branch", "wide area"],
                "dmz": ["dmz", "security", "firewall"],
                "hybrid": ["hybrid", "mixed", "combination"]
            }
            
            response_lower = response.lower()
            for pattern_key, keywords in pattern_mapping.items():
                if any(keyword in response_lower for keyword in keywords):
                    patterns.append(pattern_key)
            
            return patterns[:3] if patterns else ["hybrid", "three_tier", "collapsed_core"]
        
        return ["hybrid", "three_tier", "collapsed_core"]  # Enhanced default suggestions
    
    async def _suggest_device_models(self, data: Dict[str, Any]) -> List[str]:
        """Suggest device models based on device names and types"""
        shapes = data.get("shapes", [])
        incomplete_devices = []
        
        for shape in shapes[:10]:  # Limit to first 10
            props = shape.get("properties", {})
            if not any(key in props for key in ["model", "device_model"]):
                incomplete_devices.append({
                    "name": shape.get("name", ""),
                    "type": shape.get("shape_type", "")
                })
        
        if not incomplete_devices:
            return []
        
        prompt = f"""Suggest likely device models for these network devices:

{chr(10).join([f"- {d['name']} (type: {d['type']})" for d in incomplete_devices])}

Provide realistic model suggestions based on device names and types.
Format: DeviceName: Suggested Model"""
        
        response = await self._call_ollama(prompt)
        
        suggestions = []
        if response:
            lines = response.split('\n')
            for line in lines:
                if ':' in line:
                    model = line.split(':', 1)[1].strip()
                    if model:
                        suggestions.append(model)
        
        return suggestions
    
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