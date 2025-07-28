#!/usr/bin/env python3
"""Initialize default system templates."""
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from app.models.document_template import DocumentTemplate, TemplateType
from app.models.organization import Organization
from app.database import engine
import uuid

DEFAULT_TEMPLATES = [
    {
        "name": "Professional Network Documentation",
        "description": "Comprehensive network documentation with executive summary and technical details",
        "template_type": TemplateType.NETWORK_DOCUMENTATION,
        "html_template": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title | default('Network Documentation') }}</title>
    <style>{{ css_styles }}</style>
</head>
<body>
    <!-- Cover Page -->
    <div class="cover-page">
        {% if organization.logo_url %}
        <img src="{{ organization.logo_url }}" alt="{{ organization.name }}" class="logo">
        {% endif %}
        <h1>{{ title | default('Network Infrastructure Documentation') }}</h1>
        <h2>{{ project_name }}</h2>
        <div class="cover-details">
            <p><strong>Customer:</strong> {{ customer_organization }}</p>
            <p><strong>Project Code:</strong> {{ project_code }}</p>
            <p><strong>Version:</strong> {{ version | default('1.0') }}</p>
            <p><strong>Date:</strong> {{ generated_date }}</p>
        </div>
    </div>

    <!-- Header for subsequent pages -->
    {{ header_template }}

    <!-- Executive Summary -->
    <section class="page-break">
        <h1>Executive Summary</h1>
        <div class="summary-box">
            <p>{{ network_summary | default('This document provides a comprehensive overview of the network infrastructure.') }}</p>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>Total Devices</h3>
                <p class="stat-number">{{ shapes | length }}</p>
            </div>
            <div class="stat-card">
                <h3>Network Connections</h3>
                <p class="stat-number">{{ connections | length }}</p>
            </div>
            <div class="stat-card">
                <h3>VLANs Configured</h3>
                <p class="stat-number">{{ vlans | length }}</p>
            </div>
        </div>
    </section>

    <!-- Network Topology -->
    <section class="page-break">
        <h1>Network Topology</h1>
        <p>The following section details the network topology and interconnections between devices.</p>
        
        <h2>Device Inventory</h2>
        <table class="device-table">
            <thead>
                <tr>
                    <th>Device Name</th>
                    <th>Type</th>
                    <th>Model</th>
                    <th>IP Address</th>
                    <th>Location</th>
                    <th>Connections</th>
                </tr>
            </thead>
            <tbody>
                {% for shape in shapes %}
                <tr>
                    <td>{{ shape.name }}</td>
                    <td>{{ shape.type | title }}</td>
                    <td>{{ shape.properties.model | default('N/A') }}</td>
                    <td>{{ shape.properties.ip_address | default('N/A') }}</td>
                    <td>{{ shape.properties.location | default('N/A') }}</td>
                    <td>{{ shape.connections_count }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </section>

    <!-- Network Connections -->
    <section class="page-break">
        <h1>Network Connections</h1>
        <table class="connection-table">
            <thead>
                <tr>
                    <th>Source Device</th>
                    <th>Target Device</th>
                    <th>Connection Type</th>
                    <th>VLAN</th>
                </tr>
            </thead>
            <tbody>
                {% for connection in connections %}
                <tr>
                    <td>{{ connection.source_name }}</td>
                    <td>{{ connection.target_name }}</td>
                    <td>{{ connection.connection_type }}</td>
                    <td>{{ connection.vlan | default('Trunk') }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </section>

    <!-- VLAN Configuration -->
    {% if vlans %}
    <section class="page-break">
        <h1>VLAN Configuration</h1>
        <table class="vlan-table">
            <thead>
                <tr>
                    <th>VLAN ID</th>
                    <th>Name</th>
                    <th>Subnet</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                {% for vlan in vlans %}
                <tr>
                    <td>{{ vlan.id }}</td>
                    <td>{{ vlan.name }}</td>
                    <td>{{ vlan.subnet }}</td>
                    <td>{{ vlan.description | default('') }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </section>
    {% endif %}

    <!-- Footer -->
    {{ footer_template }}
</body>
</html>""",
        "css_styles": """/* Professional Network Documentation Styles */
:root {
    --primary-color: #1e3c72;
    --secondary-color: #2a5298;
    --accent-color: #4CAF50;
    --text-color: #333;
    --border-color: #ddd;
    --bg-light: #f8f9fa;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: #fff;
}

/* Cover Page */
.cover-page {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    page-break-after: always;
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    color: white;
}

.cover-page .logo {
    max-height: 120px;
    margin-bottom: 40px;
}

.cover-page h1 {
    font-size: 3em;
    margin-bottom: 20px;
    font-weight: 300;
}

.cover-page h2 {
    font-size: 2em;
    margin-bottom: 40px;
    font-weight: 400;
}

.cover-details {
    background: rgba(255, 255, 255, 0.1);
    padding: 30px;
    border-radius: 10px;
    backdrop-filter: blur(10px);
}

.cover-details p {
    margin: 10px 0;
    font-size: 1.1em;
}

/* Page Breaks */
.page-break {
    page-break-before: always;
    padding: 40px;
}

/* Headers */
h1 {
    color: var(--primary-color);
    font-size: 2.5em;
    margin-bottom: 30px;
    border-bottom: 3px solid var(--primary-color);
    padding-bottom: 10px;
}

h2 {
    color: var(--secondary-color);
    font-size: 1.8em;
    margin-top: 30px;
    margin-bottom: 20px;
}

h3 {
    color: var(--text-color);
    font-size: 1.4em;
    margin-top: 25px;
    margin-bottom: 15px;
}

/* Summary Box */
.summary-box {
    background: var(--bg-light);
    border-left: 4px solid var(--primary-color);
    padding: 20px;
    margin: 20px 0;
    border-radius: 4px;
}

/* Stats Grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin: 30px 0;
}

.stat-card {
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.stat-card h3 {
    color: var(--secondary-color);
    font-size: 1em;
    margin: 0;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stat-number {
    font-size: 2.5em;
    font-weight: bold;
    color: var(--primary-color);
    margin: 10px 0;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    background: white;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

table th {
    background: var(--primary-color);
    color: white;
    padding: 15px;
    text-align: left;
    font-weight: 600;
}

table td {
    padding: 12px 15px;
    border-bottom: 1px solid var(--border-color);
}

table tr:nth-child(even) {
    background: var(--bg-light);
}

table tr:hover {
    background: #e8f4f8;
}

/* Header/Footer */
.document-header,
.document-footer {
    background: var(--bg-light);
    padding: 20px 40px;
    border-bottom: 1px solid var(--border-color);
}

.document-footer {
    border-bottom: none;
    border-top: 1px solid var(--border-color);
    text-align: center;
    font-size: 0.9em;
    color: #666;
}

/* Print Styles */
@media print {
    .page-break {
        page-break-before: always;
    }
    
    table {
        page-break-inside: avoid;
    }
}""",
        "header_template": """<header class="document-header">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <strong>{{ organization.display_name | default(organization.name) }}</strong>
        </div>
        <div>
            {{ project_name }} - {{ title }}
        </div>
    </div>
</header>""",
        "footer_template": """<footer class="document-footer">
    <div style="display: flex; justify-content: space-between;">
        <span>© {{ organization.name }} - Confidential</span>
        <span>Page <span class="page-number"></span></span>
        <span>Generated: {{ generated_date }}</span>
    </div>
</footer>""",
        "is_system_template": True,
        "is_default": True
    },
    {
        "name": "Executive Summary Report",
        "description": "High-level overview focused on business stakeholders",
        "template_type": TemplateType.EXECUTIVE_SUMMARY,
        "html_template": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Executive Summary - {{ project_name }}</title>
    <style>{{ css_styles }}</style>
</head>
<body>
    <div class="executive-header">
        {% if organization.logo_url %}
        <img src="{{ organization.logo_url }}" alt="{{ organization.name }}" class="logo">
        {% endif %}
        <h1>Executive Summary</h1>
        <h2>{{ project_name }}</h2>
        <p class="subtitle">{{ customer_organization }}</p>
    </div>

    <div class="content">
        <section class="overview">
            <h2>Project Overview</h2>
            <div class="info-grid">
                <div class="info-item">
                    <label>Project Code:</label>
                    <span>{{ project_code }}</span>
                </div>
                <div class="info-item">
                    <label>Project Manager:</label>
                    <span>{{ project_manager }}</span>
                </div>
                <div class="info-item">
                    <label>Date:</label>
                    <span>{{ generated_date }}</span>
                </div>
            </div>
        </section>

        <section class="key-findings">
            <h2>Key Findings</h2>
            <div class="summary-box">
                <p>{{ network_summary }}</p>
            </div>
            
            <div class="metrics">
                <div class="metric">
                    <div class="metric-value">{{ shapes | length }}</div>
                    <div class="metric-label">Network Devices</div>
                </div>
                <div class="metric">
                    <div class="metric-value">{{ connections | length }}</div>
                    <div class="metric-label">Connections</div>
                </div>
                <div class="metric">
                    <div class="metric-value">{{ vlans | length }}</div>
                    <div class="metric-label">VLANs</div>
                </div>
            </div>
        </section>

        <section class="recommendations">
            <h2>Infrastructure Summary</h2>
            <ul class="device-summary">
                {% for shape in shapes[:5] %}
                <li>
                    <strong>{{ shape.name }}</strong> - {{ shape.type | title }}
                    {% if shape.properties.model %}({{ shape.properties.model }}){% endif %}
                </li>
                {% endfor %}
            </ul>
        </section>
    </div>

    {{ footer_template }}
</body>
</html>""",
        "css_styles": """/* Executive Summary Styles */
body {
    font-family: Georgia, 'Times New Roman', serif;
    line-height: 1.8;
    color: #333;
    max-width: 800px;
    margin: 0 auto;
    padding: 40px;
}

.executive-header {
    text-align: center;
    margin-bottom: 50px;
    padding-bottom: 30px;
    border-bottom: 2px solid #ddd;
}

.executive-header .logo {
    max-height: 80px;
    margin-bottom: 20px;
}

.executive-header h1 {
    font-size: 2.5em;
    color: #1e3c72;
    margin-bottom: 10px;
    font-weight: normal;
}

.executive-header h2 {
    font-size: 1.8em;
    color: #666;
    margin-bottom: 5px;
    font-weight: normal;
}

.subtitle {
    color: #888;
    font-style: italic;
}

.content section {
    margin-bottom: 40px;
}

h2 {
    color: #1e3c72;
    font-size: 1.6em;
    margin-bottom: 20px;
    font-weight: normal;
}

.info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 15px;
    margin-bottom: 30px;
}

.info-item {
    display: flex;
    gap: 10px;
}

.info-item label {
    font-weight: bold;
    color: #666;
}

.summary-box {
    background: #f8f9fa;
    padding: 25px;
    border-left: 4px solid #1e3c72;
    margin: 20px 0;
    font-style: italic;
}

.metrics {
    display: flex;
    justify-content: space-around;
    margin: 40px 0;
}

.metric {
    text-align: center;
}

.metric-value {
    font-size: 3em;
    color: #1e3c72;
    font-weight: bold;
}

.metric-label {
    color: #666;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-size: 0.9em;
}

.device-summary {
    list-style: none;
    padding: 0;
}

.device-summary li {
    padding: 10px 0;
    border-bottom: 1px solid #eee;
}""",
        "is_system_template": True
    },
    {
        "name": "Technical Report",
        "description": "Detailed technical documentation for IT teams",
        "template_type": TemplateType.TECHNICAL_REPORT,
        "html_template": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Technical Report - {{ project_name }}</title>
    <style>{{ css_styles }}</style>
</head>
<body>
    <div class="report-header">
        <h1>Technical Network Report</h1>
        <div class="metadata">
            <span>Project: {{ project_name }}</span>
            <span>Date: {{ generated_date }}</span>
            <span>Version: {{ version | default('1.0') }}</span>
        </div>
    </div>

    <section>
        <h2>1. Network Architecture</h2>
        <p>{{ network_summary }}</p>
        
        <h3>1.1 Device Inventory</h3>
        <table class="technical-table">
            <thead>
                <tr>
                    <th>Device</th>
                    <th>Type</th>
                    <th>Model</th>
                    <th>IP</th>
                    <th>MAC</th>
                    <th>Firmware</th>
                </tr>
            </thead>
            <tbody>
                {% for shape in shapes %}
                <tr>
                    <td><code>{{ shape.name }}</code></td>
                    <td>{{ shape.type }}</td>
                    <td>{{ shape.properties.model | default('-') }}</td>
                    <td><code>{{ shape.properties.ip_address | default('-') }}</code></td>
                    <td><code>{{ shape.properties.mac_address | default('-') }}</code></td>
                    <td>{{ shape.properties.firmware | default('-') }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </section>

    <section>
        <h2>2. Network Connectivity Matrix</h2>
        <table class="technical-table">
            <thead>
                <tr>
                    <th>Source</th>
                    <th>Source Port</th>
                    <th>Target</th>
                    <th>Target Port</th>
                    <th>Link Type</th>
                    <th>VLAN/Trunk</th>
                </tr>
            </thead>
            <tbody>
                {% for conn in connections %}
                <tr>
                    <td><code>{{ conn.source_name }}</code></td>
                    <td>{{ conn.source_port | default('-') }}</td>
                    <td><code>{{ conn.target_name }}</code></td>
                    <td>{{ conn.target_port | default('-') }}</td>
                    <td>{{ conn.connection_type }}</td>
                    <td>{{ conn.vlan | default('Trunk') }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </section>

    <section>
        <h2>3. VLAN Database</h2>
        <table class="technical-table">
            <thead>
                <tr>
                    <th>VLAN ID</th>
                    <th>Name</th>
                    <th>Network</th>
                    <th>Gateway</th>
                    <th>DHCP</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                {% for vlan in vlans %}
                <tr>
                    <td><code>{{ vlan.id }}</code></td>
                    <td><code>{{ vlan.name }}</code></td>
                    <td><code>{{ vlan.subnet }}</code></td>
                    <td><code>{{ vlan.gateway | default('-') }}</code></td>
                    <td>{{ vlan.dhcp_enabled | default('No') }}</td>
                    <td>{{ vlan.description | default('-') }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </section>

    {{ footer_template }}
</body>
</html>""",
        "css_styles": """/* Technical Report Styles */
body {
    font-family: 'Consolas', 'Monaco', monospace;
    line-height: 1.6;
    color: #000;
    background: #fff;
    padding: 20px;
    max-width: 1400px;
    margin: 0 auto;
}

.report-header {
    border-bottom: 2px solid #000;
    padding-bottom: 20px;
    margin-bottom: 30px;
}

.report-header h1 {
    font-size: 24px;
    margin: 0;
}

.metadata {
    margin-top: 10px;
    font-size: 12px;
}

.metadata span {
    margin-right: 20px;
}

h2 {
    font-size: 18px;
    margin-top: 30px;
    margin-bottom: 15px;
    background: #f0f0f0;
    padding: 8px;
}

h3 {
    font-size: 14px;
    margin-top: 20px;
    margin-bottom: 10px;
}

.technical-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 12px;
}

.technical-table th {
    background: #333;
    color: #fff;
    padding: 8px;
    text-align: left;
    font-weight: normal;
}

.technical-table td {
    border: 1px solid #ddd;
    padding: 6px 8px;
}

.technical-table tr:nth-child(even) {
    background: #f9f9f9;
}

code {
    background: #f0f0f0;
    padding: 1px 4px;
    border-radius: 3px;
    font-family: inherit;
}

section {
    page-break-inside: avoid;
    margin-bottom: 30px;
}""",
        "is_system_template": True
    }
]

async def init_templates():
    # Create async session
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    
    async with async_session() as session:
        # Check if templates already exist
        result = await session.execute(
            select(DocumentTemplate).where(DocumentTemplate.is_system_template == True)
        )
        existing_templates = result.scalars().all()
        
        if existing_templates:
            print(f"System templates already exist ({len(existing_templates)} found). Skipping initialization.")
            return
        
        # Create system organization ID (fixed UUID for system templates)
        system_org_id = uuid.UUID('00000000-0000-0000-0000-000000000001')
        
        # Check if system organization exists
        result = await session.execute(
            select(Organization).where(Organization.id == system_org_id)
        )
        system_org = result.scalar_one_or_none()
        
        if not system_org:
            # Create system organization
            system_org = Organization(
                id=system_org_id,
                name="NetDocGen System",
                display_name="NetDocGen System Templates",
                description="System organization for default templates",
                is_active=True
            )
            session.add(system_org)
            print("Created system organization")
        
        # Create templates
        for template_data in DEFAULT_TEMPLATES:
            template = DocumentTemplate(
                id=uuid.uuid4(),
                organization_id=system_org_id,
                **template_data
            )
            session.add(template)
            print(f"Created template: {template.name}")
        
        await session.commit()
        print(f"\nSuccessfully created {len(DEFAULT_TEMPLATES)} system templates.")

if __name__ == "__main__":
    asyncio.run(init_templates())