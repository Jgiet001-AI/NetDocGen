import os
import platform
import re
from pathlib import Path
from typing import Optional
from .shapes import ShapeType

def get_visio_file_extension() -> str:
    """Get the appropriate Visio file extension for the platform."""
    if platform.system() == "Windows":
        return ".vsd"
    else:
        return ".vsdx"

def is_visio_file(file_path: Path) -> bool:
    """Check if a file is a Visio document."""
    valid_extensions = {".vsd", ".vsdx", ".vsdm", ".vss", ".vssx", ".vssm"}
    return file_path.suffix.lower() in valid_extensions

def extract_vsdx_contents(file_path: Path, output_dir: Path) -> bool:
    """
    Extract contents of a VSDX file (which is a ZIP archive).
    
    Args:
        file_path: Path to the VSDX file
        output_dir: Directory to extract contents to
        
    Returns:
        True if extraction successful, False otherwise
    """
    import zipfile
    
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        return True
    except Exception as e:
        print(f"Error extracting VSDX file: {e}")
        return False

def detect_shape_type(master_name: str, text: str) -> ShapeType:
    """
    Detect the type of network device based on shape master name and text.
    
    Args:
        master_name: The master shape name from Visio
        text: The text content of the shape
        
    Returns:
        ShapeType enum value
    """
    # Handle None values
    master_name = master_name or ""
    text = text or ""
    
    # Combine master name and text for analysis
    combined = f"{master_name} {text}".lower()
    
    # Define patterns for each device type
    patterns = {
        ShapeType.ROUTER: [
            r'\brouter\b', r'\brt\b', r'\bcisco.*router', r'\bjuniper.*router',
            r'\bmikrotik', r'\bedge.*router', r'\bcore.*router', r'\bbgp'
        ],
        ShapeType.SWITCH: [
            r'\bswitch\b', r'\bsw\b', r'\bl2.*switch', r'\bl3.*switch',
            r'\bmanaged.*switch', r'\bcore.*switch', r'\bdistribution.*switch',
            r'\baccess.*switch', r'\bcisco.*switch'
        ],
        ShapeType.FIREWALL: [
            r'\bfirewall\b', r'\bfw\b', r'\basa\b', r'\bpalo.*alto',
            r'\bfortinet', r'\bfortigate', r'\bcheckpoint', r'\bpfsense',
            r'\bsecurity.*appliance'
        ],
        ShapeType.SERVER: [
            r'\bserver\b', r'\bsrv\b', r'\bhost\b', r'\bvm\b',
            r'\bwindows.*server', r'\blinux.*server', r'\besxi',
            r'\bvmware', r'\bhyper-v', r'\bapp.*server', r'\bweb.*server',
            r'\bdatabase.*server', r'\bfile.*server'
        ],
        ShapeType.WORKSTATION: [
            r'\bworkstation\b', r'\bpc\b', r'\bdesktop\b', r'\blaptop\b',
            r'\bcomputer\b', r'\bclient\b', r'\buser.*device', r'\bendpoint'
        ],
        ShapeType.CLOUD: [
            r'\bcloud\b', r'\baws\b', r'\bazure\b', r'\bgcp\b',
            r'\binternet\b', r'\bweb\b', r'\bsaas\b', r'\bpaas',
            r'\biaas', r'\bpublic.*cloud', r'\bprivate.*cloud'
        ]
    }
    
    # Check each pattern
    for shape_type, pattern_list in patterns.items():
        for pattern in pattern_list:
            if re.search(pattern, combined):
                return shape_type
    
    # Additional checks based on common stencil names
    stencil_mapping = {
        'router': ShapeType.ROUTER,
        'switch': ShapeType.SWITCH,
        'firewall': ShapeType.FIREWALL,
        'server': ShapeType.SERVER,
        'pc': ShapeType.WORKSTATION,
        'computer': ShapeType.WORKSTATION,
        'cloud': ShapeType.CLOUD,
        'internet': ShapeType.CLOUD,
    }
    
    for key, shape_type in stencil_mapping.items():
        if key in master_name.lower():
            return shape_type
    
    # Default to UNKNOWN if no match found
    return ShapeType.UNKNOWN

def normalize_connection_type(connector_text: str, source_type: ShapeType, target_type: ShapeType) -> str:
    """
    Normalize connection type based on connector text and connected device types.
    
    Args:
        connector_text: Text from the connector shape
        source_type: Type of source device
        target_type: Type of target device
        
    Returns:
        Normalized connection type string
    """
    # Handle None or empty connector_text
    if not connector_text:
        connector_text = ""
    
    text_lower = connector_text.lower()
    
    # Check for specific connection types
    if any(term in text_lower for term in ['ethernet', 'eth', 'gig', 'fast']):
        return "ethernet"
    elif any(term in text_lower for term in ['fiber', 'optical', 'sfp']):
        return "fiber"
    elif any(term in text_lower for term in ['serial', 'rs232', 'console']):
        return "serial"
    elif any(term in text_lower for term in ['wireless', 'wifi', 'wi-fi', '802.11']):
        return "wireless"
    elif any(term in text_lower for term in ['vpn', 'tunnel', 'ipsec']):
        return "vpn"
    elif any(term in text_lower for term in ['wan', 'mpls', 'leased']):
        return "wan"
    
    # Infer based on device types
    if source_type == ShapeType.CLOUD or target_type == ShapeType.CLOUD:
        return "internet"
    elif source_type == ShapeType.FIREWALL or target_type == ShapeType.FIREWALL:
        return "security_link"
    
    # Default
    return "network_link"