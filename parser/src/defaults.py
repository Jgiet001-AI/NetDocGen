"""Default values for missing network information."""

from typing import Dict, Any

# Default network configuration values
DEFAULT_NETWORK_CONFIG = {
    "vlan": {
        "id": "VLAN_ID",
        "name": "VLAN_NAME",
        "description": "Network VLAN"
    },
    "subnet": {
        "network": "10.0.0.0/24",
        "gateway": "10.0.0.1",
        "dhcp_start": "10.0.0.100",
        "dhcp_end": "10.0.0.200"
    },
    "device_defaults": {
        "router": {
            "vendor": "Generic",
            "model": "Router",
            "os_version": "Latest",
            "management_ip": "10.0.0.X"
        },
        "switch": {
            "vendor": "Generic", 
            "model": "Switch",
            "os_version": "Latest",
            "management_ip": "10.0.0.X",
            "port_count": 24
        },
        "firewall": {
            "vendor": "Generic",
            "model": "Firewall",
            "os_version": "Latest",
            "management_ip": "10.0.0.X",
            "policy_count": 0
        },
        "server": {
            "vendor": "Generic",
            "model": "Server",
            "os": "Linux/Windows",
            "ip_address": "10.0.0.X",
            "services": []
        }
    },
    "connection_defaults": {
        "bandwidth": "1 Gbps",
        "media_type": "Ethernet",
        "protocol": "TCP/IP"
    }
}

def get_default_device_properties(device_type: str, device_name: str = None) -> Dict[str, Any]:
    """
    Get default properties for a device type.
    
    Args:
        device_type: Type of device (router, switch, etc.)
        device_name: Optional device name to customize defaults
        
    Returns:
        Dictionary of default properties
    """
    # Handle None device_type
    if not device_type:
        device_type = "unknown"
    
    device_type_lower = device_type.lower()
    
    if device_type_lower in DEFAULT_NETWORK_CONFIG["device_defaults"]:
        defaults = DEFAULT_NETWORK_CONFIG["device_defaults"][device_type_lower].copy()
        
        # Add device-specific customization if needed
        if device_name:
            defaults["hostname"] = device_name
            defaults["description"] = f"{device_type} - {device_name}"
        else:
            defaults["hostname"] = f"{device_type}_HOSTNAME"
            defaults["description"] = f"{device_type} Device"
            
        return defaults
    
    # Return generic defaults for unknown device types
    return {
        "vendor": "Unknown",
        "model": "Unknown",
        "hostname": device_name or f"{device_type}_HOSTNAME",
        "description": f"{device_type} Device"
    }

def get_default_connection_properties(connection_type: str = None) -> Dict[str, Any]:
    """
    Get default properties for a connection.
    
    Args:
        connection_type: Optional connection type
        
    Returns:
        Dictionary of default connection properties
    """
    defaults = DEFAULT_NETWORK_CONFIG["connection_defaults"].copy()
    
    if connection_type:
        # Safely convert to lowercase
        connection_type_lower = connection_type.lower()
        
        # Customize based on connection type
        if "fiber" in connection_type_lower:
            defaults["bandwidth"] = "10 Gbps"
            defaults["media_type"] = "Fiber Optic"
        elif "wireless" in connection_type_lower:
            defaults["bandwidth"] = "300 Mbps"
            defaults["media_type"] = "Wireless"
            defaults["protocol"] = "802.11ac"
        elif "serial" in connection_type_lower:
            defaults["bandwidth"] = "115200 bps"
            defaults["media_type"] = "Serial"
            defaults["protocol"] = "RS-232"
            
    return defaults

def enrich_parsed_data(parsed_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Enrich parsed data with default values for missing information.
    
    Args:
        parsed_data: Original parsed data from Visio
        
    Returns:
        Enriched data with defaults filled in
    """
    # Add network information if missing
    if "network_info" not in parsed_data:
        parsed_data["network_info"] = DEFAULT_NETWORK_CONFIG.copy()
    
    # Enrich device information
    if "shapes" in parsed_data:
        for shape in parsed_data["shapes"]:
            # Add default properties if missing
            if not shape.get("properties"):
                shape["properties"] = {}
                
            # Get device type defaults
            device_defaults = get_default_device_properties(
                shape.get("type", "unknown"),
                shape.get("name")
            )
            
            # Merge with existing properties (existing properties take precedence)
            for key, value in device_defaults.items():
                if key not in shape["properties"]:
                    shape["properties"][key] = value
    
    # Enrich connection information
    if "connections" in parsed_data:
        for connection in parsed_data["connections"]:
            if not connection.get("properties"):
                connection["properties"] = {}
                
            # Get connection defaults
            conn_defaults = get_default_connection_properties(
                connection.get("type")
            )
            
            # Merge with existing properties
            for key, value in conn_defaults.items():
                if key not in connection["properties"]:
                    connection["properties"][key] = value
    
    # Add metadata
    parsed_data["metadata"] = parsed_data.get("metadata", {})
    parsed_data["metadata"]["defaults_applied"] = True
    parsed_data["metadata"]["notice"] = (
        "Some network information was filled with default values. "
        "Please update with actual values as needed."
    )
    
    return parsed_data