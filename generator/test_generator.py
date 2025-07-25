#!/usr/bin/env python3
"""
Test script for the document generator service.
Tests document generation with sample parsed data.
"""

import asyncio
import json
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from generator.src.generator import DocumentGenerator

# Sample parsed data
SAMPLE_DATA = {
    "title": "Test Network Documentation",
    "filename": "test_network.vsdx",
    "created_date": "2024-01-20",
    "modified_date": "2024-01-20",
    "author": "Test User",
    "pages": ["Network Topology"],
    "shapes": [
        {
            "id": "shape1",
            "name": "Core Router 1",
            "type": "router",
            "text": "Core Router 1\n192.168.1.1",
            "master_shape": "Router"
        },
        {
            "id": "shape2",
            "name": "Core Switch 1",
            "type": "switch",
            "text": "Core Switch 1\n192.168.1.10",
            "master_shape": "Switch"
        },
        {
            "id": "shape3",
            "name": "Firewall 1",
            "type": "firewall",
            "text": "Firewall 1\n192.168.1.254",
            "master_shape": "Firewall"
        },
        {
            "id": "shape4",
            "name": "Server 1",
            "type": "server",
            "text": "Server 1\n192.168.10.10",
            "master_shape": "Server"
        },
        {
            "id": "shape5",
            "name": "Server 2",
            "type": "server",
            "text": "Server 2\n192.168.10.20",
            "master_shape": "Server"
        }
    ],
    "connections": [
        {
            "id": "conn1",
            "source": "shape1",
            "target": "shape2",
            "type": "ethernet",
            "properties": {"bandwidth": "10Gbps"}
        },
        {
            "id": "conn2",
            "source": "shape1",
            "target": "shape3",
            "type": "ethernet",
            "properties": {"bandwidth": "10Gbps"}
        },
        {
            "id": "conn3",
            "source": "shape2",
            "target": "shape4",
            "type": "ethernet",
            "properties": {"bandwidth": "1Gbps"}
        },
        {
            "id": "conn4",
            "source": "shape2",
            "target": "shape5",
            "type": "ethernet",
            "properties": {"bandwidth": "1Gbps"}
        }
    ]
}

def test_generator():
    """Test document generation."""
    print("Testing Document Generator...")
    
    # Initialize generator
    template_dir = Path(__file__).parent / "src" / "templates"
    generator = DocumentGenerator(template_dir)
    
    # Test all formats
    formats = ["html", "markdown", "docx", "pdf"]
    output_dir = Path(__file__).parent / "test_output"
    output_dir.mkdir(exist_ok=True)
    
    for format_type in formats:
        try:
            print(f"\nGenerating {format_type} document...")
            
            # Skip PDF if WeasyPrint not installed
            if format_type == "pdf":
                try:
                    import weasyprint
                except ImportError:
                    print("  WeasyPrint not installed, skipping PDF generation")
                    continue
            
            # Generate document
            doc_bytes = generator.generate_documentation(SAMPLE_DATA, format_type)
            
            # Save to file
            extension = format_type if format_type != "docx" else "docx"
            output_file = output_dir / f"test_document.{extension}"
            output_file.write_bytes(doc_bytes)
            
            print(f"  ✓ Generated {format_type} document: {output_file}")
            print(f"    Size: {len(doc_bytes):,} bytes")
            
        except Exception as e:
            print(f"  ✗ Error generating {format_type}: {e}")
    
    print(f"\nTest complete! Generated documents saved to: {output_dir}")

if __name__ == "__main__":
    test_generator()