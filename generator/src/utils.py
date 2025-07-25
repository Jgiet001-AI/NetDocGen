import os
from pathlib import Path
from typing import Dict, Any, List

def create_table_of_contents(sections: List[Dict[str, Any]]) -> str:
    """
    Create a table of contents from document sections.
    
    Args:
        sections: List of section dictionaries with 'title' and 'level' keys
        
    Returns:
        Formatted table of contents as string
    """
    toc_lines = ["# Table of Contents\n"]
    
    for section in sections:
        level = section.get("level", 1)
        title = section.get("title", "")
        indent = "  " * (level - 1)
        toc_lines.append(f"{indent}- {title}")
    
    return "\n".join(toc_lines)

def format_device_list(devices: List[Dict[str, Any]]) -> str:
    """
    Format a list of network devices for documentation.
    
    Args:
        devices: List of device dictionaries
        
    Returns:
        Formatted device list as string
    """
    if not devices:
        return "No devices found."
    
    lines = []
    for device in devices:
        lines.append(f"- **{device.get('name', 'Unknown')}** ({device.get('type', 'Unknown Type')})")
        if device.get('ip_address'):
            lines.append(f"  - IP: {device['ip_address']}")
        if device.get('location'):
            lines.append(f"  - Location: {device['location']}")
    
    return "\n".join(lines)

def sanitize_filename(filename: str) -> str:
    """
    Sanitize a filename by removing invalid characters.
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename
    """
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename