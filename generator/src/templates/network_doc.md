# {{ title or "Network Documentation" }}

**Generated:** {{ generated_date }}  
**Source:** {{ diagram_data.filename or "Visio Diagram" }}

---

## Executive Summary

This network documentation provides a comprehensive overview of the network infrastructure captured from the Visio diagram. The network consists of **{{ diagram_data.shapes|length }}** devices connected through **{{ diagram_data.connections|length }}** connections.

### Key Statistics

| Metric | Value |
|--------|-------|
| Total Devices | {{ diagram_data.shapes|length }} |
| Total Connections | {{ diagram_data.connections|length }} |
| Device Types | {{ device_types|length }} |
| Most Common Device Type | {{ most_common_device_type|default("N/A") }} |
| Average Connections per Device | {{ avg_connections_per_device|round(2) }} |
| Network Density | {{ network_density|round(3) }} |

---

## Network Overview

### Device Distribution by Type

{% for device_type, count in device_type_distribution.items() %}
- **{{ device_type }}**: {{ count }} devices ({{ (count / diagram_data.shapes|length * 100)|round(1) }}%)
{% endfor %}

### Critical Network Components

{% if most_connected_devices %}
#### Highly Connected Devices (Network Hubs)
{% for device in most_connected_devices[:5] %}
1. **{{ device.name }}** ({{ device.type }}) - {{ device.connections }} connections
{% endfor %}
{% endif %}

{% if isolated_devices %}
#### Isolated Devices
{% for device in isolated_devices %}
- {{ device.name }} ({{ device.type }})
{% endfor %}
{% endif %}

---

## Device Inventory

{% for device_type, devices in devices_by_type.items() %}
### {{ device_type }} ({{ devices|length }} devices)

{% for device in devices %}
#### {{ device.name }}

- **Device ID:** `{{ device.id }}`
- **Type:** {{ device.type }}
{% if device.connections_count %}
- **Number of Connections:** {{ device.connections_count }}
{% endif %}
{% if device.properties %}
- **Properties:**
{% for key, value in device.properties.items() %}
  - {{ key }}: {{ value }}
{% endfor %}
{% endif %}
{% if device.connected_to %}
- **Connected to:**
{% for connection in device.connected_to %}
  - {{ connection.device_name }} ({{ connection.connection_type }})
{% endfor %}
{% endif %}

{% endfor %}
{% endfor %}

---

## Network Connections

### Connection Matrix

| Source Device | Target Device | Connection Type | Properties |
|---------------|---------------|-----------------|------------|
{% for conn in connections_enhanced %}
| {{ conn.source_name }} | {{ conn.target_name }} | {{ conn.connection_type }} | {% if conn.properties %}{% for key, value in conn.properties.items() %}{{ key }}: {{ value }}{% if not loop.last %}, {% endif %}{% endfor %}{% else %}-{% endif %} |
{% endfor %}

### Connection Types Summary

{% for conn_type, count in connection_types.items() %}
- **{{ conn_type }}**: {{ count }} connections
{% endfor %}

---

## Network Topology Analysis

### Network Characteristics

- **Network Type:** {{ network_type|default("Mixed") }}
- **Topology Pattern:** {{ topology_pattern|default("Custom") }}
- **Redundancy Level:** {{ redundancy_level|default("Unknown") }}

### Network Segments

{% if network_segments_list %}
{% for segment in network_segments_list %}
#### Segment {{ loop.index }}: {{ segment.name }}

- **Devices:** {{ segment.device_count }}
- **Internal Connections:** {{ segment.internal_connections }}
- **External Connections:** {{ segment.external_connections }}
- **Key Devices:**
{% for device in segment.key_devices[:3] %}
  - {{ device.name }} ({{ device.type }})
{% endfor %}

{% endfor %}
{% else %}
The network appears to be a single unified segment.
{% endif %}

---

## Recommendations

Based on the network analysis, here are some observations and recommendations:

### Connectivity Analysis

{% if isolated_devices %}
1. **Isolated Devices:** There are {{ isolated_devices|length }} isolated devices that may need to be connected to the network or removed if they are no longer in use.
{% endif %}

{% if high_density_areas %}
2. **High-Density Areas:** Some network areas show high connection density, which might indicate:
   - Critical network chokepoints
   - Potential single points of failure
   - Areas requiring redundancy improvements
{% endif %}

### Scalability Considerations

3. **Network Growth:** With {{ diagram_data.shapes|length }} devices and an average of {{ avg_connections_per_device|round(2) }} connections per device, consider:
   - Implementing hierarchical network design
   - Adding redundant paths for critical connections
   - Segmenting the network for better management

### Documentation Maintenance

4. **Keep Documentation Updated:** This documentation reflects the network state as of {{ generated_date }}. Regular updates are recommended to maintain accuracy.

---

## Appendices

### A. Device Type Definitions

{% for device_type in device_types %}
- **{{ device_type }}**: Description of {{ device_type }} devices and their role in the network
{% endfor %}

### B. Connection Type Definitions

{% for conn_type in connection_types.keys() %}
- **{{ conn_type }}**: Description of {{ conn_type }} connections
{% endfor %}

### C. Metadata

{% if diagram_data.metadata %}
**Diagram Properties:**
{% for key, value in diagram_data.metadata.items() %}
- {{ key }}: {{ value }}
{% endfor %}
{% endif %}

---

*This document was automatically generated by NetDocGen from a Visio network diagram.*  
*Generated on: {{ generated_date }}*