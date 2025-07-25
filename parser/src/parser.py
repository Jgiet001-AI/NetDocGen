import json
import logging
from typing import Dict, List, Any, Optional
from pathlib import Path
from datetime import datetime
import re

# Get logger before using it
logger = logging.getLogger(__name__)

try:
    from vsdx import VisioFile
    VSDX_AVAILABLE = True
except ImportError:
    VSDX_AVAILABLE = False
    logger.warning("vsdx library not available. VSDX parsing will be limited.")

from .shapes import NetworkShape, Connection, ShapeType
from .utils import is_visio_file, detect_shape_type

class VisioParser:
    """Parse Visio documents and extract network diagram information."""
    
    def __init__(self):
        self.shapes = []
        self.connections = []
        self.visio_file = None
        
    def parse_file(self, file_path: Path) -> Dict[str, Any]:
        """
        Parse a Visio file and extract network diagram data.
        
        Args:
            file_path: Path to the Visio file
            
        Returns:
            Dictionary containing parsed diagram data
        """
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
            
        if not is_visio_file(file_path):
            raise ValueError(f"Not a valid Visio file: {file_path}")
            
        logger.info(f"Parsing Visio file: {file_path}")
        
        # Use vsdx library for VSDX files
        if file_path.suffix.lower() == ".vsdx" and VSDX_AVAILABLE:
            return self._parse_vsdx(file_path)
        else:
            # Fallback to XML parsing or raise error
            raise NotImplementedError(f"Parsing for {file_path.suffix} files not yet implemented")
        
    def _parse_vsdx(self, file_path: Path) -> Dict[str, Any]:
        """Parse VSDX file using the vsdx library."""
        try:
            with VisioFile(str(file_path)) as vis:
                self.visio_file = vis
                
                # Extract metadata
                metadata = self._extract_metadata_vsdx(vis)
                
                # Process all pages
                all_shapes = []
                all_connections = []
                
                for page_index, page in enumerate(vis.pages):
                    logger.info(f"Processing page {page_index + 1}: {page.name}")
                    
                    # Extract shapes from this page
                    page_shapes = self._extract_shapes_vsdx(page)
                    all_shapes.extend(page_shapes)
                    
                    # Extract connections from this page
                    page_connections = self._extract_connections_vsdx(page)
                    all_connections.extend(page_connections)
                
                return {
                    "filename": file_path.name,
                    "shapes": [shape.dict() if hasattr(shape, 'dict') else shape for shape in all_shapes],
                    "connections": [conn.dict() if hasattr(conn, 'dict') else conn for conn in all_connections],
                    "metadata": metadata,
                    "page_count": len(vis.pages)
                }
                
        except Exception as e:
            logger.error(f"Error parsing VSDX file: {e}")
            raise
    
    def _extract_shapes_vsdx(self, page) -> List[NetworkShape]:
        """Extract shape information from a VSDX page."""
        shapes = []
        
        for shape in page.child_shapes:
            try:
                # Extract basic shape information with safe attribute access
                shape_data = {
                    "id": str(shape.ID) if hasattr(shape, 'ID') else f"shape_{id(shape)}",
                    "name": shape.text if hasattr(shape, 'text') and shape.text else f"Shape_{shape.ID if hasattr(shape, 'ID') else id(shape)}",
                    "master_name": shape.master_page.name if hasattr(shape, 'master_page') and shape.master_page and hasattr(shape.master_page, 'name') else None,
                    "x": float(shape.x) if hasattr(shape, 'x') and shape.x is not None else 0.0,
                    "y": float(shape.y) if hasattr(shape, 'y') and shape.y is not None else 0.0,
                    "width": float(shape.width) if hasattr(shape, 'width') and shape.width is not None else 0.0,
                    "height": float(shape.height) if hasattr(shape, 'height') and shape.height is not None else 0.0,
                    "text": shape.text if hasattr(shape, 'text') else None,
                }
                
                # Detect shape type based on master name and text
                shape_type = detect_shape_type(
                    shape_data.get("master_name", ""),
                    shape_data.get("text", "")
                )
                
                # Extract additional properties safely
                properties = {}
                if hasattr(shape, 'data_properties') and shape.data_properties:
                    try:
                        for prop in shape.data_properties:
                            if hasattr(prop, 'name') and hasattr(prop, 'value'):
                                prop_name = str(prop.name) if prop.name else 'unknown'
                                prop_value = str(prop.value) if prop.value is not None else ''
                                properties[prop_name] = prop_value
                    except Exception as e:
                        logger.debug(f"Could not extract data properties: {e}")
                
                # Create NetworkShape instance
                network_shape = NetworkShape(
                    id=shape_data["id"],
                    name=shape_data["name"],
                    shape_type=shape_type,
                    x=shape_data["x"],
                    y=shape_data["y"],
                    width=shape_data["width"],
                    height=shape_data["height"],
                    properties=properties
                )
                
                shapes.append(network_shape)
                logger.debug(f"Extracted shape: {network_shape.name} (Type: {shape_type.value})")
                
            except Exception as e:
                shape_id = shape.ID if hasattr(shape, 'ID') else 'unknown'
                logger.warning(f"Error extracting shape {shape_id}: {type(e).__name__}: {e}")
                logger.debug(f"Shape details: {vars(shape) if hasattr(shape, '__dict__') else 'No details available'}")
                
                # Log specific error types for better debugging
                if isinstance(e, TypeError) and "NoneType" in str(e):
                    logger.error(f"NoneType error in shape {shape_id}: Check data validation")
                elif isinstance(e, AttributeError):
                    logger.error(f"AttributeError in shape {shape_id}: Missing expected attribute")
                    
                continue
        
        return shapes
    
    def _extract_connections_vsdx(self, page) -> List[Connection]:
        """Extract connection information from a VSDX page."""
        connections = []
        
        for shape in page.child_shapes:
            # Check if shape is a connector
            if hasattr(shape, 'connects') and shape.connects:
                # Ensure connects is iterable
                connects_list = shape.connects if hasattr(shape.connects, '__iter__') else []
                for connect in connects_list:
                    try:
                        # Safely extract connection information
                        conn_id = str(shape.ID) if hasattr(shape, 'ID') else f"conn_{id(shape)}"
                        
                        # Extract source ID safely
                        source_id = None
                        if hasattr(connect, 'from_rel') and connect.from_rel:
                            if hasattr(connect.from_rel, 'shape') and connect.from_rel.shape:
                                if hasattr(connect.from_rel.shape, 'ID'):
                                    source_id = str(connect.from_rel.shape.ID)
                        
                        # Extract target ID safely
                        target_id = None
                        if hasattr(connect, 'to_rel') and connect.to_rel:
                            if hasattr(connect.to_rel, 'shape') and connect.to_rel.shape:
                                if hasattr(connect.to_rel.shape, 'ID'):
                                    target_id = str(connect.to_rel.shape.ID)
                        
                        # Extract connection properties
                        label = shape.text if hasattr(shape, 'text') else ""
                        from_part = None
                        to_part = None
                        
                        if hasattr(connect, 'from_rel') and connect.from_rel and hasattr(connect.from_rel, 'part'):
                            from_part = connect.from_rel.part
                        if hasattr(connect, 'to_rel') and connect.to_rel and hasattr(connect.to_rel, 'part'):
                            to_part = connect.to_rel.part
                        
                        connection = Connection(
                            id=conn_id,
                            source_id=source_id,
                            target_id=target_id,
                            connection_type="network_link",  # Default type
                            properties={
                                "label": label or "",
                                "from_part": from_part,
                                "to_part": to_part,
                            }
                        )
                        
                        if connection.source_id and connection.target_id:
                            connections.append(connection)
                            logger.debug(f"Extracted connection: {connection.source_id} -> {connection.target_id}")
                            
                    except Exception as e:
                        shape_id = shape.ID if hasattr(shape, 'ID') else 'unknown'
                        logger.warning(f"Error extracting connection from shape {shape_id}: {type(e).__name__}: {e}")
                        logger.debug(f"Connection details: from_rel={hasattr(connect, 'from_rel')}, to_rel={hasattr(connect, 'to_rel')}")
                        
                        # Log specific error types for better debugging
                        if isinstance(e, TypeError) and "NoneType" in str(e):
                            logger.error(f"NoneType error in connection {shape_id}: Check connection data")
                        elif isinstance(e, AttributeError):
                            logger.error(f"AttributeError in connection {shape_id}: {str(e)}")
                            
                        continue
        
        return connections
    
    def _extract_metadata_vsdx(self, vis_file) -> Dict[str, Any]:
        """Extract document metadata from VSDX file."""
        metadata = {
            "created": None,
            "modified": None,
            "author": None,
            "title": None,
            "subject": None,
            "manager": None,
            "company": None,
        }
        
        try:
            # Access document properties if available
            if hasattr(vis_file, 'document_properties'):
                props = vis_file.document_properties
                metadata.update({
                    "title": getattr(props, 'title', None),
                    "subject": getattr(props, 'subject', None),
                    "author": getattr(props, 'creator', None),
                    "manager": getattr(props, 'manager', None),
                    "company": getattr(props, 'company', None),
                })
        except Exception as e:
            logger.warning(f"Error extracting metadata: {e}")
        
        return metadata