"""
Generate test data for the Visio parser.

This script creates a mock parsed data structure that represents
what the parser would extract from a typical network diagram.
"""

import json
from pathlib import Path
from datetime import datetime

def generate_sample_network_data():
    """Generate a sample network diagram data structure."""
    
    # Sample shapes representing network devices
    shapes = [
        {
            "id": "1",
            "name": "Core Router",
            "shape_type": "router",
            "x": 400.0,
            "y": 100.0,
            "width": 80.0,
            "height": 80.0,
            "properties": {
                "ip_address": "10.0.0.1",
                "model": "Cisco ISR 4451",
                "location": "Data Center"
            }
        },
        {
            "id": "2",
            "name": "Distribution Switch 1",
            "shape_type": "switch",
            "x": 200.0,
            "y": 250.0,
            "width": 80.0,
            "height": 60.0,
            "properties": {
                "ip_address": "10.0.1.1",
                "model": "Cisco Catalyst 3850",
                "vlan_count": "12"
            }
        },
        {
            "id": "3",
            "name": "Distribution Switch 2",
            "shape_type": "switch",
            "x": 600.0,
            "y": 250.0,
            "width": 80.0,
            "height": 60.0,
            "properties": {
                "ip_address": "10.0.1.2",
                "model": "Cisco Catalyst 3850",
                "vlan_count": "12"
            }
        },
        {
            "id": "4",
            "name": "Firewall",
            "shape_type": "firewall",
            "x": 400.0,
            "y": 400.0,
            "width": 100.0,
            "height": 60.0,
            "properties": {
                "ip_address": "10.0.2.1",
                "model": "Palo Alto PA-3220",
                "zones": "DMZ, Internal, External"
            }
        },
        {
            "id": "5",
            "name": "Web Server",
            "shape_type": "server",
            "x": 200.0,
            "y": 550.0,
            "width": 60.0,
            "height": 80.0,
            "properties": {
                "ip_address": "10.0.10.10",
                "os": "Ubuntu 22.04",
                "services": "nginx, apache"
            }
        },
        {
            "id": "6",
            "name": "Database Server",
            "shape_type": "server",
            "x": 600.0,
            "y": 550.0,
            "width": 60.0,
            "height": 80.0,
            "properties": {
                "ip_address": "10.0.10.20",
                "os": "RHEL 8",
                "database": "PostgreSQL 14"
            }
        },
        {
            "id": "7",
            "name": "Internet",
            "shape_type": "cloud",
            "x": 400.0,
            "y": -100.0,
            "width": 120.0,
            "height": 80.0,
            "properties": {
                "provider": "ISP",
                "bandwidth": "1 Gbps"
            }
        }
    ]
    
    # Sample connections between devices
    connections = [
        {
            "id": "c1",
            "source_id": "7",
            "target_id": "1",
            "connection_type": "wan",
            "properties": {
                "label": "Internet Link",
                "bandwidth": "1 Gbps"
            }
        },
        {
            "id": "c2",
            "source_id": "1",
            "target_id": "2",
            "connection_type": "ethernet",
            "properties": {
                "label": "Trunk",
                "bandwidth": "10 Gbps"
            }
        },
        {
            "id": "c3",
            "source_id": "1",
            "target_id": "3",
            "connection_type": "ethernet",
            "properties": {
                "label": "Trunk",
                "bandwidth": "10 Gbps"
            }
        },
        {
            "id": "c4",
            "source_id": "2",
            "target_id": "4",
            "connection_type": "ethernet",
            "properties": {
                "label": "Internal Zone",
                "vlan": "100"
            }
        },
        {
            "id": "c5",
            "source_id": "3",
            "target_id": "4",
            "connection_type": "ethernet",
            "properties": {
                "label": "Internal Zone",
                "vlan": "100"
            }
        },
        {
            "id": "c6",
            "source_id": "4",
            "target_id": "5",
            "connection_type": "ethernet",
            "properties": {
                "label": "DMZ",
                "vlan": "200"
            }
        },
        {
            "id": "c7",
            "source_id": "4",
            "target_id": "6",
            "connection_type": "ethernet",
            "properties": {
                "label": "Database Zone",
                "vlan": "300"
            }
        }
    ]
    
    # Complete document structure
    document_data = {
        "filename": "sample_network_diagram.vsdx",
        "shapes": shapes,
        "connections": connections,
        "metadata": {
            "created": "2024-01-15T10:00:00Z",
            "modified": "2024-01-20T15:30:00Z",
            "author": "Network Administrator",
            "title": "Corporate Network Topology",
            "subject": "Network Documentation",
            "company": "Example Corp"
        },
        "page_count": 1,
        "document_id": "test-doc-123",
        "project_id": "test-project-456",
        "parsed_at": datetime.utcnow().isoformat()
    }
    
    return document_data

def save_test_data():
    """Save test data to a JSON file."""
    test_data = generate_sample_network_data()
    
    # Save to file
    output_path = Path(__file__).parent / "sample_parsed_data.json"
    with open(output_path, "w") as f:
        json.dump(test_data, f, indent=2)
    
    print(f"Test data saved to: {output_path}")
    print(f"Total shapes: {len(test_data['shapes'])}")
    print(f"Total connections: {len(test_data['connections'])}")
    
    # Print summary
    print("\nShape types:")
    shape_types = {}
    for shape in test_data['shapes']:
        shape_type = shape['shape_type']
        shape_types[shape_type] = shape_types.get(shape_type, 0) + 1
    
    for shape_type, count in shape_types.items():
        print(f"  - {shape_type}: {count}")

if __name__ == "__main__":
    save_test_data()