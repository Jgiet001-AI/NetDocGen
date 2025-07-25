import pytest
from pathlib import Path
import json
import tempfile
from unittest.mock import Mock, patch

# Add parent directory to path
import sys
sys.path.append(str(Path(__file__).parent.parent))

from src.parser import VisioParser
from src.shapes import ShapeType, NetworkShape, Connection
from src.utils import detect_shape_type, normalize_connection_type

class TestShapeDetection:
    """Test shape type detection functionality."""
    
    def test_detect_router_shape(self):
        """Test router detection from various inputs."""
        assert detect_shape_type("Router", "") == ShapeType.ROUTER
        assert detect_shape_type("Cisco Router", "") == ShapeType.ROUTER
        assert detect_shape_type("", "Core Router") == ShapeType.ROUTER
        assert detect_shape_type("", "RT-01") == ShapeType.ROUTER
        assert detect_shape_type("network", "Edge Router BGP") == ShapeType.ROUTER
    
    def test_detect_switch_shape(self):
        """Test switch detection from various inputs."""
        assert detect_shape_type("Switch", "") == ShapeType.SWITCH
        assert detect_shape_type("L2 Switch", "") == ShapeType.SWITCH
        assert detect_shape_type("", "SW-CORE-01") == ShapeType.SWITCH
        assert detect_shape_type("", "Distribution Switch") == ShapeType.SWITCH
        assert detect_shape_type("Cisco", "Access Switch") == ShapeType.SWITCH
    
    def test_detect_firewall_shape(self):
        """Test firewall detection from various inputs."""
        assert detect_shape_type("Firewall", "") == ShapeType.FIREWALL
        assert detect_shape_type("", "FW-01") == ShapeType.FIREWALL
        assert detect_shape_type("", "Palo Alto") == ShapeType.FIREWALL
        assert detect_shape_type("FortiGate", "") == ShapeType.FIREWALL
        assert detect_shape_type("", "ASA 5505") == ShapeType.FIREWALL
    
    def test_detect_server_shape(self):
        """Test server detection from various inputs."""
        assert detect_shape_type("Server", "") == ShapeType.SERVER
        assert detect_shape_type("", "Web Server") == ShapeType.SERVER
        assert detect_shape_type("", "DB-SRV-01") == ShapeType.SERVER
        assert detect_shape_type("VMware", "ESXi Host") == ShapeType.SERVER
        assert detect_shape_type("", "Application Server") == ShapeType.SERVER
    
    def test_detect_workstation_shape(self):
        """Test workstation detection from various inputs."""
        assert detect_shape_type("PC", "") == ShapeType.WORKSTATION
        assert detect_shape_type("Workstation", "") == ShapeType.WORKSTATION
        assert detect_shape_type("", "Desktop Computer") == ShapeType.WORKSTATION
        assert detect_shape_type("", "User Laptop") == ShapeType.WORKSTATION
        assert detect_shape_type("Computer", "") == ShapeType.WORKSTATION
    
    def test_detect_cloud_shape(self):
        """Test cloud detection from various inputs."""
        assert detect_shape_type("Cloud", "") == ShapeType.CLOUD
        assert detect_shape_type("Internet", "") == ShapeType.CLOUD
        assert detect_shape_type("", "AWS VPC") == ShapeType.CLOUD
        assert detect_shape_type("", "Azure Cloud") == ShapeType.CLOUD
        assert detect_shape_type("", "Public Cloud") == ShapeType.CLOUD
    
    def test_detect_unknown_shape(self):
        """Test unknown shape detection."""
        assert detect_shape_type("", "") == ShapeType.UNKNOWN
        assert detect_shape_type("Random Shape", "") == ShapeType.UNKNOWN
        assert detect_shape_type("", "Some Text") == ShapeType.UNKNOWN

class TestConnectionNormalization:
    """Test connection type normalization."""
    
    def test_normalize_ethernet_connection(self):
        """Test ethernet connection detection."""
        assert normalize_connection_type("Ethernet", ShapeType.SWITCH, ShapeType.SERVER) == "ethernet"
        assert normalize_connection_type("1 Gig", ShapeType.SWITCH, ShapeType.SWITCH) == "ethernet"
        assert normalize_connection_type("FastEthernet", ShapeType.ROUTER, ShapeType.SWITCH) == "ethernet"
    
    def test_normalize_fiber_connection(self):
        """Test fiber connection detection."""
        assert normalize_connection_type("Fiber", ShapeType.SWITCH, ShapeType.SWITCH) == "fiber"
        assert normalize_connection_type("10G SFP+", ShapeType.SWITCH, ShapeType.ROUTER) == "fiber"
        assert normalize_connection_type("Optical Link", ShapeType.ROUTER, ShapeType.ROUTER) == "fiber"
    
    def test_normalize_vpn_connection(self):
        """Test VPN connection detection."""
        assert normalize_connection_type("VPN Tunnel", ShapeType.FIREWALL, ShapeType.FIREWALL) == "vpn"
        assert normalize_connection_type("IPSec", ShapeType.ROUTER, ShapeType.ROUTER) == "vpn"
        assert normalize_connection_type("Site-to-Site VPN", ShapeType.FIREWALL, ShapeType.CLOUD) == "vpn"
    
    def test_normalize_cloud_connection(self):
        """Test cloud connection detection."""
        assert normalize_connection_type("", ShapeType.ROUTER, ShapeType.CLOUD) == "internet"
        assert normalize_connection_type("", ShapeType.CLOUD, ShapeType.FIREWALL) == "internet"
        assert normalize_connection_type("Internet Link", ShapeType.ROUTER, ShapeType.ROUTER) == "network_link"
    
    def test_normalize_default_connection(self):
        """Test default connection type."""
        assert normalize_connection_type("", ShapeType.SWITCH, ShapeType.SWITCH) == "network_link"
        assert normalize_connection_type("Link", ShapeType.ROUTER, ShapeType.SWITCH) == "network_link"

class TestNetworkShape:
    """Test NetworkShape dataclass."""
    
    def test_shape_to_dict(self):
        """Test converting shape to dictionary."""
        shape = NetworkShape(
            id="1",
            name="Test Router",
            shape_type=ShapeType.ROUTER,
            x=100.0,
            y=200.0,
            width=50.0,
            height=50.0,
            properties={"ip": "192.168.1.1"}
        )
        
        shape_dict = shape.dict()
        assert shape_dict["id"] == "1"
        assert shape_dict["name"] == "Test Router"
        assert shape_dict["shape_type"] == "router"
        assert shape_dict["x"] == 100.0
        assert shape_dict["y"] == 200.0
        assert shape_dict["properties"]["ip"] == "192.168.1.1"

class TestConnection:
    """Test Connection dataclass."""
    
    def test_connection_to_dict(self):
        """Test converting connection to dictionary."""
        conn = Connection(
            id="conn1",
            source_id="shape1",
            target_id="shape2",
            connection_type="ethernet",
            properties={"bandwidth": "1Gbps"}
        )
        
        conn_dict = conn.dict()
        assert conn_dict["id"] == "conn1"
        assert conn_dict["source_id"] == "shape1"
        assert conn_dict["target_id"] == "shape2"
        assert conn_dict["connection_type"] == "ethernet"
        assert conn_dict["properties"]["bandwidth"] == "1Gbps"

class TestVisioParser:
    """Test VisioParser functionality."""
    
    def test_parser_initialization(self):
        """Test parser initialization."""
        parser = VisioParser()
        assert parser.shapes == []
        assert parser.connections == []
        assert parser.visio_file is None
    
    def test_parse_nonexistent_file(self):
        """Test parsing a non-existent file."""
        parser = VisioParser()
        with pytest.raises(FileNotFoundError):
            parser.parse_file(Path("nonexistent.vsdx"))
    
    def test_parse_invalid_file_type(self):
        """Test parsing an invalid file type."""
        parser = VisioParser()
        with tempfile.NamedTemporaryFile(suffix=".txt") as f:
            with pytest.raises(ValueError):
                parser.parse_file(Path(f.name))
    
    @patch('src.parser.VSDX_AVAILABLE', False)
    def test_parse_without_vsdx_library(self):
        """Test parsing when vsdx library is not available."""
        parser = VisioParser()
        with tempfile.NamedTemporaryFile(suffix=".vsdx") as f:
            with pytest.raises(NotImplementedError):
                parser.parse_file(Path(f.name))

# Integration tests would go here if we had sample VSDX files
# For now, these are primarily unit tests for the utility functions