from enum import Enum
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict

class ShapeType(Enum):
    """Network device shape types."""
    ROUTER = "router"
    SWITCH = "switch"
    FIREWALL = "firewall"
    SERVER = "server"
    WORKSTATION = "workstation"
    CLOUD = "cloud"
    UNKNOWN = "unknown"

@dataclass
class NetworkShape:
    """Represents a network device shape from Visio."""
    id: str
    name: str
    shape_type: ShapeType
    x: float
    y: float
    width: float
    height: float
    properties: Dict[str, Any]
    
    def dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        data = asdict(self)
        data['shape_type'] = self.shape_type.value
        return data
    
    @classmethod
    def from_visio_shape(cls, shape_data: Dict[str, Any]) -> "NetworkShape":
        """Create NetworkShape from Visio shape data."""
        # Validate shape_data
        if not shape_data:
            shape_data = {}
            
        # Extract shape type from master shape name or text
        shape_type = ShapeType.UNKNOWN
        master_shape = shape_data.get("master_shape", "")
        text = shape_data.get("text", "")
        
        # Ensure strings are not None before calling lower()
        master_shape = master_shape.lower() if master_shape else ""
        text = text.lower() if text else ""
        
        # Determine shape type based on master shape or text content
        if any(keyword in master_shape for keyword in ["router", "rtr"]):
            shape_type = ShapeType.ROUTER
        elif any(keyword in master_shape for keyword in ["switch", "sw"]):
            shape_type = ShapeType.SWITCH
        elif any(keyword in master_shape for keyword in ["firewall", "fw"]):
            shape_type = ShapeType.FIREWALL
        elif any(keyword in master_shape for keyword in ["server", "srv"]):
            shape_type = ShapeType.SERVER
        elif any(keyword in master_shape for keyword in ["workstation", "pc", "computer"]):
            shape_type = ShapeType.WORKSTATION
        elif any(keyword in master_shape for keyword in ["cloud"]):
            shape_type = ShapeType.CLOUD
        elif any(keyword in master_shape for keyword in ["storage", "disk", "nas", "san"]):
            shape_type = ShapeType.STORAGE
        elif any(keyword in master_shape for keyword in ["wireless", "ap", "access point"]):
            shape_type = ShapeType.WIRELESS_AP
        elif any(keyword in master_shape for keyword in ["load", "balancer", "lb"]):
            shape_type = ShapeType.LOAD_BALANCER
        
        # Extract position and size
        bounds = shape_data.get("bounds", {})
        x = bounds.get("x", 0.0)
        y = bounds.get("y", 0.0)
        width = bounds.get("width", 100.0)
        height = bounds.get("height", 100.0)
        
        # Extract properties
        properties = {}
        if "ip_address" in shape_data:
            properties["ip_address"] = shape_data["ip_address"]
        if "mac_address" in shape_data:
            properties["mac_address"] = shape_data["mac_address"]
        if "model" in shape_data:
            properties["model"] = shape_data["model"]
        if "vendor" in shape_data:
            properties["vendor"] = shape_data["vendor"]
        
        return cls(
            id=shape_data.get("id", ""),
            name=shape_data.get("name", "") or shape_data.get("text", ""),
            shape_type=shape_type,
            x=x,
            y=y,
            width=width,
            height=height,
            properties=properties
        )

@dataclass
class Connection:
    """Represents a connection between network shapes."""
    id: str
    source_id: str
    target_id: str
    connection_type: str
    properties: Dict[str, Any]
    
    def dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)