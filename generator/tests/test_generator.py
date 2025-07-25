import pytest
from pathlib import Path
import json
import tempfile
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

# Add parent directory to path
import sys
sys.path.append(str(Path(__file__).parent.parent))

from src.generator import DocumentGenerator
from src.utils import format_bytes, extract_ip_addresses, categorize_devices


class TestDocumentGenerator:
    """Test DocumentGenerator class."""
    
    @pytest.fixture
    def generator(self):
        """Create a DocumentGenerator instance."""
        template_dir = Path(__file__).parent.parent / "src" / "templates"
        return DocumentGenerator(template_dir)
    
    @pytest.fixture
    def sample_data(self):
        """Sample parsed network data."""
        return {
            "project_name": "Test Network",
            "filename": "test_network.vsdx",
            "generated_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "shapes": [
                {
                    "id": "1",
                    "name": "Core Router",
                    "shape_type": "router",
                    "properties": {"text": "RT-CORE-01\nIP: 192.168.1.1"}
                },
                {
                    "id": "2",
                    "name": "Access Switch",
                    "shape_type": "switch",
                    "properties": {"text": "SW-ACCESS-01\nVLAN: 100"}
                },
                {
                    "id": "3",
                    "name": "Web Server",
                    "shape_type": "server",
                    "properties": {"text": "SRV-WEB-01\nIP: 192.168.10.10"}
                }
            ],
            "connections": [
                {
                    "id": "c1",
                    "source_id": "1",
                    "target_id": "2",
                    "connection_type": "ethernet",
                    "properties": {"bandwidth": "10Gbps"}
                },
                {
                    "id": "c2",
                    "source_id": "2",
                    "target_id": "3",
                    "connection_type": "ethernet",
                    "properties": {"bandwidth": "1Gbps"}
                }
            ],
            "metadata": {
                "total_shapes": 3,
                "total_connections": 2,
                "shape_types": {"router": 1, "switch": 1, "server": 1}
            }
        }
    
    def test_generator_initialization(self, generator):
        """Test generator initialization."""
        assert generator.template_dir.exists()
        assert generator.env is not None
        assert "format_bytes" in generator.env.filters
    
    def test_generate_html(self, generator, sample_data):
        """Test HTML document generation."""
        html_content = generator.generate_documentation(sample_data, "html")
        
        assert isinstance(html_content, bytes)
        html_str = html_content.decode('utf-8')
        
        # Check for key elements
        assert "Test Network" in html_str
        assert "Core Router" in html_str
        assert "192.168.1.1" in html_str
        assert "Network Topology" in html_str
        assert "Device Inventory" in html_str
    
    def test_generate_markdown(self, generator, sample_data):
        """Test Markdown document generation."""
        md_content = generator.generate_documentation(sample_data, "markdown")
        
        assert isinstance(md_content, bytes)
        md_str = md_content.decode('utf-8')
        
        # Check for markdown elements
        assert "# Test Network" in md_str
        assert "## Network Topology" in md_str
        assert "| Device Name" in md_str  # Table header
        assert "RT-CORE-01" in md_str
        assert "192.168.1.1" in md_str
    
    def test_generate_pdf(self, generator, sample_data):
        """Test PDF document generation."""
        # Mock WeasyPrint to avoid dependency
        with patch('src.generator.HTML') as mock_html:
            mock_document = Mock()
            mock_document.write_pdf.return_value = b"PDF content"
            mock_html.return_value = mock_document
            
            pdf_content = generator.generate_documentation(sample_data, "pdf")
            
            assert pdf_content == b"PDF content"
            mock_html.assert_called_once()
            mock_document.write_pdf.assert_called_once()
    
    def test_generate_docx(self, generator, sample_data):
        """Test DOCX document generation."""
        with patch('src.generator.Document') as mock_doc_class:
            mock_doc = Mock()
            mock_doc_class.return_value = mock_doc
            
            # Mock save method
            def mock_save(buffer):
                buffer.write(b"DOCX content")
            mock_doc.save = mock_save
            
            docx_content = generator.generate_documentation(sample_data, "docx")
            
            assert docx_content == b"DOCX content"
            mock_doc_class.assert_called_once()
            # Verify document structure was created
            assert mock_doc.add_heading.called
            assert mock_doc.add_paragraph.called
    
    def test_generate_invalid_format(self, generator, sample_data):
        """Test generation with invalid format."""
        with pytest.raises(ValueError) as exc_info:
            generator.generate_documentation(sample_data, "invalid")
        assert "Unsupported format" in str(exc_info.value)
    
    def test_generate_with_missing_template(self, generator, sample_data):
        """Test generation when template is missing."""
        # Mock template loading to raise error
        with patch.object(generator.env, 'get_template', side_effect=Exception("Template not found")):
            with pytest.raises(Exception) as exc_info:
                generator.generate_documentation(sample_data, "html")
            assert "Template not found" in str(exc_info.value)
    
    def test_generate_with_empty_data(self, generator):
        """Test generation with empty data."""
        empty_data = {
            "project_name": "Empty Project",
            "shapes": [],
            "connections": [],
            "metadata": {
                "total_shapes": 0,
                "total_connections": 0
            }
        }
        
        html_content = generator.generate_documentation(empty_data, "html")
        html_str = html_content.decode('utf-8')
        
        assert "Empty Project" in html_str
        assert "No devices found" in html_str or len(html_str) > 100
    
    def test_generate_with_professional_template(self, generator, sample_data):
        """Test generation with professional template."""
        sample_data["template"] = "professional"
        
        html_content = generator.generate_documentation(sample_data, "html")
        html_str = html_content.decode('utf-8')
        
        # Professional template should have additional sections
        assert "Executive Summary" in html_str
        assert "Network Analysis" in html_str
    
    def test_ai_analysis_integration(self, generator, sample_data):
        """Test AI analysis integration in document."""
        sample_data["ai_analysis"] = {
            "summary": "This is a small network with 3 devices.",
            "security_assessment": "Basic security measures in place.",
            "recommendations": ["Implement redundancy", "Add monitoring"]
        }
        
        html_content = generator.generate_documentation(sample_data, "html")
        html_str = html_content.decode('utf-8')
        
        assert "AI Network Analysis" in html_str
        assert "This is a small network" in html_str
        assert "Implement redundancy" in html_str


class TestUtilityFunctions:
    """Test utility functions."""
    
    def test_format_bytes(self):
        """Test byte formatting."""
        assert format_bytes(0) == "0 B"
        assert format_bytes(1024) == "1.00 KB"
        assert format_bytes(1048576) == "1.00 MB"
        assert format_bytes(1073741824) == "1.00 GB"
        assert format_bytes(1500) == "1.46 KB"
    
    def test_extract_ip_addresses(self):
        """Test IP address extraction."""
        text = "Server IP: 192.168.1.100, Gateway: 10.0.0.1"
        ips = extract_ip_addresses(text)
        assert ips == ["192.168.1.100", "10.0.0.1"]
        
        text_no_ip = "This text has no IP addresses"
        assert extract_ip_addresses(text_no_ip) == []
        
        text_invalid = "Invalid IP: 999.999.999.999"
        assert extract_ip_addresses(text_invalid) == []
    
    def test_categorize_devices(self):
        """Test device categorization."""
        devices = [
            {"shape_type": "router"},
            {"shape_type": "router"},
            {"shape_type": "switch"},
            {"shape_type": "server"},
            {"shape_type": "server"},
            {"shape_type": "server"},
            {"shape_type": "firewall"},
            {"shape_type": "unknown"}
        ]
        
        categories = categorize_devices(devices)
        
        assert categories["routers"] == 2
        assert categories["switches"] == 1
        assert categories["servers"] == 3
        assert categories["firewalls"] == 1
        assert categories["other"] == 1


class TestDocumentGeneratorIntegration:
    """Integration tests for document generation."""
    
    @pytest.fixture
    def complex_network_data(self):
        """Complex network data for testing."""
        return {
            "project_name": "Enterprise Network",
            "filename": "enterprise_network.vsdx",
            "generated_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "shapes": [
                # Core layer
                {"id": "1", "name": "Core-Router-1", "shape_type": "router", 
                 "properties": {"text": "CR-01\nIP: 10.0.0.1\nBGP AS: 65001"}},
                {"id": "2", "name": "Core-Router-2", "shape_type": "router",
                 "properties": {"text": "CR-02\nIP: 10.0.0.2\nBGP AS: 65001"}},
                
                # Distribution layer
                {"id": "3", "name": "Dist-Switch-1", "shape_type": "switch",
                 "properties": {"text": "DS-01\nIP: 10.1.0.1\nVLAN: 100-200"}},
                {"id": "4", "name": "Dist-Switch-2", "shape_type": "switch",
                 "properties": {"text": "DS-02\nIP: 10.1.0.2\nVLAN: 100-200"}},
                
                # Security
                {"id": "5", "name": "Firewall-1", "shape_type": "firewall",
                 "properties": {"text": "FW-01\nIP: 10.254.0.1\nHA: Active"}},
                {"id": "6", "name": "Firewall-2", "shape_type": "firewall",
                 "properties": {"text": "FW-02\nIP: 10.254.0.2\nHA: Standby"}},
                
                # Servers
                {"id": "7", "name": "Web-Server-1", "shape_type": "server",
                 "properties": {"text": "WEB-01\nIP: 10.10.1.10\nOS: Linux"}},
                {"id": "8", "name": "DB-Server-1", "shape_type": "server",
                 "properties": {"text": "DB-01\nIP: 10.10.2.10\nDB: PostgreSQL"}},
                
                # Cloud
                {"id": "9", "name": "AWS-VPC", "shape_type": "cloud",
                 "properties": {"text": "AWS VPC\nRegion: us-east-1"}}
            ],
            "connections": [
                # Core redundancy
                {"id": "c1", "source_id": "1", "target_id": "2", 
                 "connection_type": "fiber", "properties": {"bandwidth": "40Gbps"}},
                
                # Core to distribution
                {"id": "c2", "source_id": "1", "target_id": "3",
                 "connection_type": "fiber", "properties": {"bandwidth": "10Gbps"}},
                {"id": "c3", "source_id": "2", "target_id": "4",
                 "connection_type": "fiber", "properties": {"bandwidth": "10Gbps"}},
                
                # Firewall connections
                {"id": "c4", "source_id": "1", "target_id": "5",
                 "connection_type": "ethernet", "properties": {"bandwidth": "10Gbps"}},
                {"id": "c5", "source_id": "5", "target_id": "6",
                 "connection_type": "ethernet", "properties": {"HA": "heartbeat"}},
                
                # Cloud VPN
                {"id": "c6", "source_id": "5", "target_id": "9",
                 "connection_type": "vpn", "properties": {"type": "IPSec"}}
            ],
            "metadata": {
                "total_shapes": 9,
                "total_connections": 6,
                "shape_types": {
                    "router": 2,
                    "switch": 2,
                    "firewall": 2,
                    "server": 2,
                    "cloud": 1
                }
            }
        }
    
    def test_complex_network_generation(self, generator, complex_network_data):
        """Test generation with complex network data."""
        # Add AI analysis
        complex_network_data["ai_analysis"] = {
            "summary": "Enterprise network with redundant core and security layers.",
            "security_assessment": "High-availability firewall configuration detected.",
            "recommendations": [
                "Consider adding redundant cloud connections",
                "Implement network monitoring on core devices"
            ]
        }
        
        # Test all formats
        for format_type in ["html", "markdown"]:
            content = generator.generate_documentation(complex_network_data, format_type)
            content_str = content.decode('utf-8')
            
            # Verify all devices are included
            assert "Core-Router-1" in content_str
            assert "Firewall-1" in content_str
            assert "AWS VPC" in content_str
            
            # Verify connections
            assert "40Gbps" in content_str
            assert "IPSec" in content_str
            
            # Verify AI analysis
            assert "redundant core" in content_str


class TestErrorHandling:
    """Test error handling in document generation."""
    
    def test_invalid_template_dir(self):
        """Test initialization with invalid template directory."""
        with pytest.raises(ValueError) as exc_info:
            DocumentGenerator(Path("/nonexistent/directory"))
        assert "does not exist" in str(exc_info.value)
    
    def test_malformed_data(self, generator):
        """Test generation with malformed data."""
        malformed_data = {
            "shapes": "not a list",  # Should be a list
            "connections": None
        }
        
        with pytest.raises(Exception):
            generator.generate_documentation(malformed_data, "html")
    
    def test_missing_required_fields(self, generator):
        """Test generation with missing required fields."""
        incomplete_data = {
            "project_name": "Test"
            # Missing shapes and connections
        }
        
        # Should handle gracefully or raise specific error
        try:
            content = generator.generate_documentation(incomplete_data, "html")
            # If it doesn't raise, verify it handles missing data
            assert isinstance(content, bytes)
        except KeyError:
            # Expected if template requires these fields
            pass