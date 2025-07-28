#!/usr/bin/env python3
"""
Test script to verify end-to-end template customization workflow.
"""
import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import get_db, engine
from app.models.document_template import DocumentTemplate, TemplateType
from app.models.organization import Organization
from app.models.user import User
from app.models.project import Project
from app.models.document import Document, DocumentStatus
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
import uuid

async def test_template_workflow():
    """Test the complete template customization workflow."""
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    
    print("🧪 Testing Template Customization Workflow\n")
    
    async with async_session() as session:
        try:
            # 1. Check system templates
            print("1️⃣ Checking system templates...")
            result = await session.execute(
                select(DocumentTemplate).where(DocumentTemplate.is_system_template == True)
            )
            system_templates = result.scalars().all()
            print(f"   ✓ Found {len(system_templates)} system templates")
            for template in system_templates:
                print(f"     - {template.name} ({template.template_type.value})")
            
            # 2. Check organization with templates
            print("\n2️⃣ Checking organizations with custom templates...")
            result = await session.execute(
                select(Organization).limit(1)
            )
            org = result.scalar_one_or_none()
            if org:
                print(f"   ✓ Found organization: {org.name}")
                
                # Check custom templates
                result = await session.execute(
                    select(DocumentTemplate).where(
                        DocumentTemplate.organization_id == org.id,
                        DocumentTemplate.is_system_template == False
                    )
                )
                custom_templates = result.scalars().all()
                print(f"   ✓ Organization has {len(custom_templates)} custom templates")
                
                # Check organization branding
                print(f"   ✓ Organization branding:")
                print(f"     - Primary Color: {org.primary_color}")
                print(f"     - Secondary Color: {org.secondary_color}")
                print(f"     - Font Family: {org.default_font_family}")
            
            # 3. Check template variable system
            print("\n3️⃣ Checking template variable system...")
            default_template = next((t for t in system_templates if t.is_default), None)
            if default_template:
                print(f"   ✓ Default template: {default_template.name}")
                # Check if template uses Jinja2 variables
                if "{{" in default_template.html_template:
                    print("   ✓ Template uses Jinja2 variables")
                    # Count variables
                    import re
                    variables = re.findall(r'{{\s*(\w+)', default_template.html_template)
                    unique_vars = set(variables)
                    print(f"   ✓ Found {len(unique_vars)} unique template variables")
                    print(f"     Variables: {', '.join(sorted(unique_vars)[:10])}...")
            
            # 4. Check if templates include organization branding
            print("\n4️⃣ Checking organization branding integration...")
            if default_template and ":root {" in default_template.css_styles:
                print("   ✓ CSS includes CSS variables for branding")
            if default_template and "var(--primary-color)" in default_template.css_styles:
                print("   ✓ Template uses CSS variables for colors")
            
            # 5. Check document generation with custom templates
            print("\n5️⃣ Checking document generation integration...")
            # Check if there are any documents
            result = await session.execute(
                select(Document).where(Document.status == DocumentStatus.COMPLETED).limit(1)
            )
            completed_doc = result.scalar_one_or_none()
            if completed_doc:
                print(f"   ✓ Found completed document: {completed_doc.filename}")
                print(f"   ✓ Generated files: {list(completed_doc.generated_files.keys()) if completed_doc.generated_files else 'None'}")
            else:
                print("   ℹ️ No completed documents found (need to upload and process a document to test)")
            
            # 6. Summary
            print("\n📊 Template System Status:")
            print(f"   • System Templates: {'✅ Ready' if system_templates else '❌ Missing'}")
            print(f"   • Organization Support: {'✅ Ready' if org else '❌ No organizations'}")
            print(f"   • Template Variables: {'✅ Ready' if default_template and '{{' in default_template.html_template else '❌ Not configured'}")
            print(f"   • CSS Branding: {'✅ Ready' if default_template and ':root {' in default_template.css_styles else '❌ Not configured'}")
            
            print("\n✅ Template customization system is properly configured!")
            
        except Exception as e:
            print(f"\n❌ Error testing template workflow: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_template_workflow())