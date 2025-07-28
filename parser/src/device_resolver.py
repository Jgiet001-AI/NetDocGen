"""
Device ID Resolution System

This module provides intelligent device identification and metadata extraction
from Visio diagrams, transforming cryptic IDs into meaningful device information.
"""

import re
import logging
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class DeviceType(Enum):
    """Network device types"""
    ROUTER = "router"
    SWITCH = "switch"
    FIREWALL = "firewall"
    LOAD_BALANCER = "load_balancer"
    SERVER = "server"
    WIRELESS_AP = "wireless_ap"
    WIRELESS_CONTROLLER = "wireless_controller"
    STORAGE = "storage"
    WORKSTATION = "workstation"
    CLOUD = "cloud"
    INTERNET = "internet"
    UNKNOWN = "unknown"


class DeviceRole(Enum):
    """Device roles in network architecture"""
    CORE = "core"
    DISTRIBUTION = "distribution"
    ACCESS = "access"
    EDGE = "edge"
    BORDER = "border"
    SPINE = "spine"
    LEAF = "leaf"
    COMPUTE = "compute"
    STORAGE = "storage"
    MANAGEMENT = "management"
    UNKNOWN = "unknown"


@dataclass
class DeviceInfo:
    """Enhanced device information"""
    id: str
    name: str
    display_name: str
    device_type: DeviceType
    device_role: DeviceRole
    vendor: Optional[str] = None
    model: Optional[str] = None
    management_ip: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    properties: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.properties is None:
            self.properties = {}


class DeviceResolver:
    """Resolves device IDs and extracts meaningful device information"""
    
    # Common device name patterns
    DEVICE_PATTERNS = {
        # Routers
        r'(rtr|router|rt)[-_]?(\w+)?': DeviceType.ROUTER,
        r'(gw|gateway)[-_]?(\w+)?': DeviceType.ROUTER,
        r'(bgp|mpls|wan)[-_]?(\w+)?': DeviceType.ROUTER,
        
        # Switches
        r'(sw|switch)[-_]?(\w+)?': DeviceType.SWITCH,
        r'(core)[-_]?(sw|switch)?[-_]?(\w+)?': DeviceType.SWITCH,
        r'(dist|distribution)[-_]?(sw|switch)?[-_]?(\w+)?': DeviceType.SWITCH,
        r'(access)[-_]?(sw|switch)?[-_]?(\w+)?': DeviceType.SWITCH,
        r'(tor|top[-_]?of[-_]?rack)[-_]?(\w+)?': DeviceType.SWITCH,
        
        # Firewalls
        r'(fw|firewall|asa|palo|fortinet|checkpoint)[-_]?(\w+)?': DeviceType.FIREWALL,
        r'(dmz|security)[-_]?(\w+)?': DeviceType.FIREWALL,
        
        # Load Balancers
        r'(lb|loadbalancer|f5|netscaler|haproxy)[-_]?(\w+)?': DeviceType.LOAD_BALANCER,
        r'(vip|virtual[-_]?ip)[-_]?(\w+)?': DeviceType.LOAD_BALANCER,
        
        # Servers
        r'(srv|server|host)[-_]?(\w+)?': DeviceType.SERVER,
        r'(web|app|db|database|sql)[-_]?(srv|server)?[-_]?(\w+)?': DeviceType.SERVER,
        r'(vm|virtual[-_]?machine)[-_]?(\w+)?': DeviceType.SERVER,
        
        # Wireless
        r'(ap|access[-_]?point|wap)[-_]?(\w+)?': DeviceType.WIRELESS_AP,
        r'(wlc|wireless[-_]?controller)[-_]?(\w+)?': DeviceType.WIRELESS_CONTROLLER,
        
        # Storage
        r'(storage|san|nas|filer)[-_]?(\w+)?': DeviceType.STORAGE,
    }
    
    # Role patterns
    ROLE_PATTERNS = {
        r'core': DeviceRole.CORE,
        r'dist|distribution': DeviceRole.DISTRIBUTION,
        r'access': DeviceRole.ACCESS,
        r'edge|border': DeviceRole.EDGE,
        r'spine': DeviceRole.SPINE,
        r'leaf': DeviceRole.LEAF,
        r'mgmt|management': DeviceRole.MANAGEMENT,
    }
    
    # Vendor patterns
    VENDOR_PATTERNS = {
        r'cisco|catalyst|nexus|asr|isr': 'Cisco',
        r'juniper|junos|srx|ex\d+': 'Juniper',
        r'arista|eos': 'Arista',
        r'fortinet|fortigate': 'Fortinet',
        r'palo[-_]?alto|pan': 'Palo Alto',
        r'f5|bigip': 'F5',
        r'dell|force10': 'Dell',
        r'hp|hpe|aruba|procurve': 'HPE',
        r'huawei': 'Huawei',
        r'vmware|nsx': 'VMware',
    }
    
    def __init__(self):
        self.device_cache: Dict[str, DeviceInfo] = {}
        
    def resolve_device(self, shape: Dict[str, Any]) -> DeviceInfo:
        """
        Resolve device information from a shape
        
        Args:
            shape: Shape dictionary from parser
            
        Returns:
            DeviceInfo object with resolved information
        """
        shape_id = shape.get("id", "unknown")
        
        # Check cache
        if shape_id in self.device_cache:
            return self.device_cache[shape_id]
        
        # Extract basic info
        name = shape.get("name", "")
        text = shape.get("text", "")
        master_name = shape.get("master_name", "")
        properties = shape.get("properties", {})
        
        # Determine device type
        device_type = self._detect_device_type(name, text, master_name, properties)
        
        # Determine device role
        device_role = self._detect_device_role(name, text, properties)
        
        # Extract vendor and model
        vendor = self._detect_vendor(name, text, properties)
        model = self._extract_model(name, text, properties)
        
        # Extract management IP
        management_ip = self._extract_ip(text, properties)
        
        # Generate display name
        display_name = self._generate_display_name(name, text, device_type, device_role)
        
        # Extract location
        location = self._extract_location(properties)
        
        # Create device info
        device_info = DeviceInfo(
            id=shape_id,
            name=name or f"Device_{shape_id}",
            display_name=display_name,
            device_type=device_type,
            device_role=device_role,
            vendor=vendor,
            model=model,
            management_ip=management_ip,
            location=location,
            description=text if text and text != name else None,
            properties=properties
        )
        
        # Cache result
        self.device_cache[shape_id] = device_info
        
        return device_info
    
    def _detect_device_type(self, name: str, text: str, master_name: str, 
                           properties: Dict[str, Any]) -> DeviceType:
        """Detect device type from various sources"""
        # Check all text sources
        text_sources = [
            name.lower() if name else "",
            text.lower() if text else "",
            master_name.lower() if master_name else "",
            " ".join(str(v).lower() for v in properties.values())
        ]
        
        combined_text = " ".join(text_sources)
        
        # Check patterns
        for pattern, device_type in self.DEVICE_PATTERNS.items():
            if re.search(pattern, combined_text, re.IGNORECASE):
                return device_type
        
        # Check stencil/master names
        if master_name:
            master_lower = master_name.lower()
            if any(keyword in master_lower for keyword in ['router', 'rtr']):
                return DeviceType.ROUTER
            elif any(keyword in master_lower for keyword in ['switch', 'sw']):
                return DeviceType.SWITCH
            elif any(keyword in master_lower for keyword in ['firewall', 'fw']):
                return DeviceType.FIREWALL
            elif any(keyword in master_lower for keyword in ['server', 'srv']):
                return DeviceType.SERVER
        
        return DeviceType.UNKNOWN
    
    def _detect_device_role(self, name: str, text: str, 
                           properties: Dict[str, Any]) -> DeviceRole:
        """Detect device role from various sources"""
        text_sources = [
            name.lower() if name else "",
            text.lower() if text else "",
            " ".join(str(v).lower() for v in properties.values())
        ]
        
        combined_text = " ".join(text_sources)
        
        for pattern, role in self.ROLE_PATTERNS.items():
            if re.search(pattern, combined_text, re.IGNORECASE):
                return role
        
        return DeviceRole.UNKNOWN
    
    def _detect_vendor(self, name: str, text: str, 
                      properties: Dict[str, Any]) -> Optional[str]:
        """Detect device vendor"""
        text_sources = [
            name.lower() if name else "",
            text.lower() if text else "",
            " ".join(str(v).lower() for v in properties.values())
        ]
        
        combined_text = " ".join(text_sources)
        
        for pattern, vendor in self.VENDOR_PATTERNS.items():
            if re.search(pattern, combined_text, re.IGNORECASE):
                return vendor
        
        return None
    
    def _extract_model(self, name: str, text: str, 
                      properties: Dict[str, Any]) -> Optional[str]:
        """Extract device model information"""
        # Common model patterns
        model_patterns = [
            r'(catalyst|cat)[-\s]?(\d{4}[a-z]?)',  # Cisco Catalyst
            r'(nexus|n)[-\s]?(\d{4}[a-z]?)',  # Cisco Nexus
            r'(asr)[-\s]?(\d{4}[a-z]?)',  # Cisco ASR
            r'(isr)[-\s]?(\d{4}[a-z]?)',  # Cisco ISR
            r'(ex|srx)[-\s]?(\d{4}[a-z]?)',  # Juniper
            r'(fortigate)[-\s]?(\d{2,4}[a-z]?)',  # Fortinet
            r'model[:\s]+([^\s,]+)',  # Generic model field
        ]
        
        text_sources = [name, text] + list(properties.values())
        
        for source in text_sources:
            if not source:
                continue
            source_str = str(source)
            for pattern in model_patterns:
                match = re.search(pattern, source_str, re.IGNORECASE)
                if match:
                    return match.group(0).strip()
        
        return None
    
    def _extract_ip(self, text: str, properties: Dict[str, Any]) -> Optional[str]:
        """Extract IP address from text or properties"""
        ip_pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
        
        # Check properties first
        ip_keys = ['ip', 'ip_address', 'management_ip', 'mgmt_ip', 'address']
        for key in ip_keys:
            if key in properties and properties[key]:
                ip_match = re.search(ip_pattern, str(properties[key]))
                if ip_match:
                    return ip_match.group(0)
        
        # Check text
        if text:
            ip_match = re.search(ip_pattern, text)
            if ip_match:
                return ip_match.group(0)
        
        return None
    
    def _extract_location(self, properties: Dict[str, Any]) -> Optional[str]:
        """Extract location information from properties"""
        location_keys = ['location', 'site', 'building', 'floor', 'rack', 'datacenter', 'dc']
        
        for key in location_keys:
            if key in properties and properties[key]:
                return str(properties[key])
        
        return None
    
    def _generate_display_name(self, name: str, text: str, 
                              device_type: DeviceType, device_role: DeviceRole) -> str:
        """Generate a human-readable display name"""
        # If we have a good name, use it
        if name and not name.startswith("Shape_") and not name.startswith("shape_"):
            return name
        
        # Otherwise, try to build a meaningful name
        parts = []
        
        # Add role if known
        if device_role != DeviceRole.UNKNOWN:
            parts.append(device_role.value.title())
        
        # Add type if known
        if device_type != DeviceType.UNKNOWN:
            parts.append(device_type.value.title())
        
        # Extract any numbers from the original name or text
        numbers = re.findall(r'\d+', f"{name} {text}")
        if numbers:
            parts.append(numbers[0])
        
        if parts:
            return " ".join(parts)
        
        # Fallback to original name
        return name or f"Device_{id(name)}"
    
    def resolve_devices(self, shapes: List[Dict[str, Any]]) -> Dict[str, DeviceInfo]:
        """
        Resolve all devices from a list of shapes
        
        Args:
            shapes: List of shape dictionaries
            
        Returns:
            Dictionary mapping shape IDs to DeviceInfo objects
        """
        devices = {}
        
        for shape in shapes:
            device_info = self.resolve_device(shape)
            devices[device_info.id] = device_info
            
            logger.debug(f"Resolved device: {device_info.display_name} "
                        f"(Type: {device_info.device_type.value}, "
                        f"Role: {device_info.device_role.value})")
        
        return devices
    
    def generate_device_inventory(self, devices: Dict[str, DeviceInfo]) -> List[Dict[str, Any]]:
        """
        Generate a device inventory report
        
        Args:
            devices: Dictionary of resolved devices
            
        Returns:
            List of device inventory entries
        """
        inventory = []
        
        for device_id, device in devices.items():
            entry = {
                "id": device_id,
                "name": device.display_name,
                "type": device.device_type.value,
                "role": device.device_role.value,
                "vendor": device.vendor or "Unknown",
                "model": device.model or "Unknown",
                "management_ip": device.management_ip or "N/A",
                "location": device.location or "N/A",
                "description": device.description or ""
            }
            inventory.append(entry)
        
        # Sort by role, then type, then name
        inventory.sort(key=lambda x: (
            self._role_priority(x["role"]),
            x["type"],
            x["name"]
        ))
        
        return inventory
    
    def _role_priority(self, role: str) -> int:
        """Get sort priority for device role"""
        priorities = {
            "core": 1,
            "spine": 2,
            "distribution": 3,
            "leaf": 4,
            "access": 5,
            "edge": 6,
            "management": 7,
            "unknown": 99
        }
        return priorities.get(role, 50)