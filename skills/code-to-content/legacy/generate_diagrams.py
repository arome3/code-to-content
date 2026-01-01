#!/usr/bin/env python3
"""
generate_diagrams.py - Generate architecture diagrams from codebase analysis

Outputs ASCII and Mermaid diagram code for technical documentation.
Analyzes project structure, dependencies, and patterns to create
visual representations.

Usage:
    python generate_diagrams.py [directory] [--type TYPE] [--output FORMAT]

Options:
    --type      Diagram type: architecture, flow, erd, components, deps
    --output    Output format: ascii, mermaid, both (default: both)
    --depth     How deep to analyze (1-5, default: 2)
"""

import os
import sys
import json
import re
import argparse
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Optional

# ============================================================================
# CONFIGURATION
# ============================================================================

IGNORE_DIRS = {
    'node_modules', 'venv', '.venv', 'env', '.env',
    '__pycache__', '.git', '.svn', 'dist', 'build',
    'target', 'out', '.next', '.nuxt', 'coverage',
    '.pytest_cache', '.mypy_cache', 'vendor', 'packages'
}

IGNORE_FILES = {
    '.DS_Store', 'Thumbs.db', '.gitignore', '.gitattributes',
    'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml',
    'Pipfile.lock', 'poetry.lock', 'composer.lock'
}

LAYER_PATTERNS = {
    'presentation': ['controller', 'view', 'page', 'component', 'ui', 'screen', 'route', 'handler'],
    'api': ['api', 'endpoint', 'rest', 'graphql', 'grpc', 'route'],
    'business': ['service', 'usecase', 'use_case', 'domain', 'core', 'logic', 'interactor'],
    'data': ['repository', 'repo', 'dao', 'store', 'persistence', 'database', 'db', 'model', 'entity'],
    'infrastructure': ['config', 'middleware', 'util', 'helper', 'lib', 'common', 'shared'],
}

# ============================================================================
# ANALYSIS FUNCTIONS
# ============================================================================

def analyze_directory_structure(root_path: Path, depth: int = 2) -> Dict:
    """Analyze directory structure for diagram generation."""
    structure = {
        'name': root_path.name,
        'type': 'directory',
        'children': [],
        'file_count': 0,
        'layer': None
    }

    if depth <= 0:
        return structure

    try:
        items = sorted(root_path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    except PermissionError:
        return structure

    for item in items:
        if item.name in IGNORE_DIRS or item.name in IGNORE_FILES:
            continue
        if item.name.startswith('.'):
            continue

        if item.is_dir():
            child = analyze_directory_structure(item, depth - 1)
            child['layer'] = detect_layer(item.name)
            structure['children'].append(child)
        else:
            structure['file_count'] += 1

    return structure


def detect_layer(name: str) -> Optional[str]:
    """Detect architectural layer from directory/file name."""
    name_lower = name.lower()
    for layer, patterns in LAYER_PATTERNS.items():
        for pattern in patterns:
            if pattern in name_lower:
                return layer
    return None


def analyze_imports(root_path: Path) -> Dict[str, Set[str]]:
    """Analyze import relationships between modules."""
    imports = defaultdict(set)

    for ext in ['*.py', '*.ts', '*.tsx', '*.js', '*.jsx']:
        for filepath in root_path.rglob(ext):
            if any(ignored in filepath.parts for ignored in IGNORE_DIRS):
                continue

            try:
                content = filepath.read_text(encoding='utf-8', errors='ignore')
                module_name = filepath.stem

                # Python imports
                if filepath.suffix == '.py':
                    for match in re.finditer(r'^(?:from|import)\s+([\w.]+)', content, re.MULTILINE):
                        imported = match.group(1).split('.')[0]
                        if imported != module_name:
                            imports[module_name].add(imported)

                # JavaScript/TypeScript imports
                elif filepath.suffix in ['.js', '.jsx', '.ts', '.tsx']:
                    for match in re.finditer(r"import\s+.*?from\s+['\"](.+?)['\"]", content):
                        imported = match.group(1)
                        if imported.startswith('.'):
                            imported = Path(imported).stem
                        else:
                            imported = imported.split('/')[0]
                        if imported != module_name:
                            imports[module_name].add(imported)

            except Exception:
                continue

    return dict(imports)


def find_database_entities(root_path: Path) -> List[Dict]:
    """Find database models/entities in the codebase."""
    entities = []

    # Common ORM patterns
    entity_patterns = [
        # SQLAlchemy
        r'class\s+(\w+)\s*\([^)]*(?:Base|Model|db\.Model)',
        # Django
        r'class\s+(\w+)\s*\(\s*models\.Model\s*\)',
        # TypeORM
        r'@Entity\([^)]*\)\s*(?:export\s+)?class\s+(\w+)',
        # Prisma-like
        r'model\s+(\w+)\s*\{',
        # Mongoose
        r'(?:const|let|var)\s+(\w+)Schema\s*=\s*new\s+(?:mongoose\.)?Schema',
        # Sequelize
        r'(?:const|let|var)\s+(\w+)\s*=\s*sequelize\.define',
    ]

    field_patterns = [
        # Python class attribute
        r'(\w+)\s*=\s*(?:Column|Field|CharField|IntegerField|ForeignKey)',
        # TypeScript/JS property
        r'@Column\([^)]*\)\s*(\w+)\s*[!?]?\s*:',
        r'(\w+)\s*:\s*(?:string|number|boolean|Date)',
    ]

    for ext in ['*.py', '*.ts', '*.tsx', '*.js', '*.jsx', '*.prisma']:
        for filepath in root_path.rglob(ext):
            if any(ignored in filepath.parts for ignored in IGNORE_DIRS):
                continue

            try:
                content = filepath.read_text(encoding='utf-8', errors='ignore')

                for pattern in entity_patterns:
                    for match in re.finditer(pattern, content, re.MULTILINE):
                        entity_name = match.group(1)

                        # Try to find fields
                        fields = []
                        for fp in field_patterns:
                            fields.extend(re.findall(fp, content))

                        entities.append({
                            'name': entity_name,
                            'file': str(filepath.relative_to(root_path)),
                            'fields': list(set(fields))[:10]  # Limit fields
                        })

            except Exception:
                continue

    return entities


def find_api_endpoints(root_path: Path) -> List[Dict]:
    """Find API endpoints in the codebase."""
    endpoints = []

    endpoint_patterns = [
        # Express.js
        r'(?:app|router)\.(get|post|put|delete|patch)\s*\(\s*[\'"]([^\'"]+)[\'"]',
        # FastAPI
        r'@(?:app|router)\.(get|post|put|delete|patch)\s*\(\s*[\'"]([^\'"]+)[\'"]',
        # Flask
        r'@(?:app|bp|blueprint)\.route\s*\(\s*[\'"]([^\'"]+)[\'"].*methods=\[([^\]]+)\]',
        # Django
        r'path\s*\(\s*[\'"]([^\'"]+)[\'"]',
        # Spring-like
        r'@(?:Get|Post|Put|Delete|Patch)Mapping\s*\(\s*[\'"]?([^\'")\s]+)',
        # NestJS
        r'@(?:Get|Post|Put|Delete|Patch)\s*\(\s*[\'"]?([^\'")\s]*)',
    ]

    for ext in ['*.py', '*.ts', '*.tsx', '*.js', '*.jsx', '*.java', '*.kt']:
        for filepath in root_path.rglob(ext):
            if any(ignored in filepath.parts for ignored in IGNORE_DIRS):
                continue

            try:
                content = filepath.read_text(encoding='utf-8', errors='ignore')

                for pattern in endpoint_patterns:
                    for match in re.finditer(pattern, content, re.IGNORECASE):
                        groups = match.groups()
                        if len(groups) == 2:
                            method, path = groups
                        else:
                            method = 'GET'
                            path = groups[0]

                        endpoints.append({
                            'method': method.upper() if method else 'GET',
                            'path': path,
                            'file': str(filepath.relative_to(root_path))
                        })

            except Exception:
                continue

    return endpoints[:30]  # Limit results


def find_services(root_path: Path) -> List[str]:
    """Find service classes/modules."""
    services = []

    patterns = [
        r'class\s+(\w+Service)',
        r'class\s+(\w+UseCase)',
        r'class\s+(\w+Interactor)',
        r'class\s+(\w+Handler)',
        r'(?:const|let|var|export\s+(?:const|let|var)?)\s+(\w+Service)\s*=',
    ]

    for ext in ['*.py', '*.ts', '*.tsx', '*.js', '*.jsx']:
        for filepath in root_path.rglob(ext):
            if any(ignored in filepath.parts for ignored in IGNORE_DIRS):
                continue

            try:
                content = filepath.read_text(encoding='utf-8', errors='ignore')
                for pattern in patterns:
                    services.extend(re.findall(pattern, content))
            except Exception:
                continue

    return list(set(services))[:20]


# ============================================================================
# ASCII DIAGRAM GENERATORS
# ============================================================================

def generate_ascii_architecture(structure: Dict, layers: Dict[str, List[str]]) -> str:
    """Generate ASCII architecture diagram."""
    lines = []
    lines.append("```")
    lines.append("┌" + "─" * 60 + "┐")
    lines.append("│" + " PROJECT ARCHITECTURE ".center(60) + "│")
    lines.append("└" + "─" * 60 + "┘")
    lines.append("")

    # Group by layer
    layer_order = ['presentation', 'api', 'business', 'data', 'infrastructure']

    for layer in layer_order:
        items = layers.get(layer, [])
        if not items:
            continue

        layer_title = layer.upper()
        lines.append("┌" + "─" * 60 + "┐")
        lines.append("│" + f" {layer_title} ".center(60) + "│")
        lines.append("├" + "─" * 60 + "┤")

        # Show items in rows of 3
        row = []
        for item in items[:9]:  # Limit to 9 items
            item_display = item[:18].center(18)
            row.append(f"│{item_display}│")
            if len(row) == 3:
                lines.append(" ".join(row).center(62))
                row = []
        if row:
            lines.append(" ".join(row).center(62))

        lines.append("└" + "─" * 60 + "┘")
        lines.append("           │")
        lines.append("           ▼")

    # Remove last arrow
    lines = lines[:-2]
    lines.append("```")

    return "\n".join(lines)


def generate_ascii_directory_tree(structure: Dict, prefix: str = "", is_last: bool = True) -> str:
    """Generate ASCII directory tree."""
    lines = []

    connector = "└── " if is_last else "├── "
    lines.append(prefix + connector + structure['name'] + "/")

    children = structure.get('children', [])
    if structure.get('file_count', 0) > 0:
        new_prefix = prefix + ("    " if is_last else "│   ")
        lines.append(new_prefix + f"└── ({structure['file_count']} files)")

    for i, child in enumerate(children):
        is_child_last = i == len(children) - 1
        new_prefix = prefix + ("    " if is_last else "│   ")
        lines.append(generate_ascii_directory_tree(child, new_prefix, is_child_last))

    return "\n".join(lines)


def generate_ascii_flow(endpoints: List[Dict]) -> str:
    """Generate ASCII request flow diagram."""
    lines = []
    lines.append("```")
    lines.append("REQUEST FLOW")
    lines.append("=" * 50)
    lines.append("")
    lines.append("Client          Gateway         Service         Database")
    lines.append("  │                │               │               │")

    for endpoint in endpoints[:5]:
        method = endpoint['method']
        path = endpoint['path'][:20]
        lines.append(f"  │──{method} {path}──▶│               │               │")
        lines.append(f"  │                │───validate───▶│               │")
        lines.append(f"  │                │               │───query──────▶│")
        lines.append(f"  │                │               │◀──result──────│")
        lines.append(f"  │◀───response────│◀──────────────│               │")
        lines.append(f"  │                │               │               │")

    lines.append("```")
    return "\n".join(lines)


def generate_ascii_components(services: List[str]) -> str:
    """Generate ASCII component diagram."""
    lines = []
    lines.append("```")
    lines.append("COMPONENT DIAGRAM")
    lines.append("=" * 50)
    lines.append("")

    # Show services in a grid
    for i, service in enumerate(services[:12]):
        if i % 3 == 0:
            lines.append("")
        service_box = f"┌{'─' * (len(service) + 4)}┐"
        lines.append(service_box.ljust(20) if i % 3 < 2 else service_box)
        service_name = f"│  {service}  │"
        lines.append(service_name.ljust(20) if i % 3 < 2 else service_name)
        service_bottom = f"└{'─' * (len(service) + 4)}┘"
        lines.append(service_bottom.ljust(20) if i % 3 < 2 else service_bottom)

    lines.append("```")
    return "\n".join(lines)


# ============================================================================
# MERMAID DIAGRAM GENERATORS
# ============================================================================

def generate_mermaid_architecture(structure: Dict, layers: Dict[str, List[str]]) -> str:
    """Generate Mermaid architecture diagram."""
    lines = []
    lines.append("```mermaid")
    lines.append("flowchart TB")
    lines.append("    subgraph Project")

    layer_order = ['presentation', 'api', 'business', 'data', 'infrastructure']
    prev_layer = None

    for layer in layer_order:
        items = layers.get(layer, [])
        if not items:
            continue

        layer_id = layer.replace(' ', '_')
        lines.append(f"        subgraph {layer_id}[{layer.title()} Layer]")

        for item in items[:6]:
            item_id = re.sub(r'[^a-zA-Z0-9]', '', item)
            lines.append(f"            {item_id}[{item}]")

        lines.append("        end")

        if prev_layer:
            lines.append(f"        {prev_layer} --> {layer_id}")
        prev_layer = layer_id

    lines.append("    end")
    lines.append("```")

    return "\n".join(lines)


def generate_mermaid_erd(entities: List[Dict]) -> str:
    """Generate Mermaid ERD diagram."""
    lines = []
    lines.append("```mermaid")
    lines.append("erDiagram")

    for entity in entities[:10]:
        name = entity['name']
        lines.append(f"    {name} {{")
        for field in entity.get('fields', [])[:5]:
            lines.append(f"        string {field}")
        lines.append("    }")

    # Add some basic relationships if multiple entities
    if len(entities) > 1:
        for i, entity in enumerate(entities[1:5]):
            lines.append(f"    {entities[0]['name']} ||--o{{ {entity['name']} : has")

    lines.append("```")
    return "\n".join(lines)


def generate_mermaid_flow(endpoints: List[Dict]) -> str:
    """Generate Mermaid sequence diagram."""
    lines = []
    lines.append("```mermaid")
    lines.append("sequenceDiagram")
    lines.append("    participant C as Client")
    lines.append("    participant A as API")
    lines.append("    participant S as Service")
    lines.append("    participant D as Database")
    lines.append("")

    for endpoint in endpoints[:5]:
        method = endpoint['method']
        path = endpoint['path']
        lines.append(f"    C->>A: {method} {path}")
        lines.append("    A->>S: Process request")
        lines.append("    S->>D: Query data")
        lines.append("    D-->>S: Return data")
        lines.append("    S-->>A: Response")
        lines.append("    A-->>C: JSON response")
        lines.append("")

    lines.append("```")
    return "\n".join(lines)


def generate_mermaid_components(services: List[str]) -> str:
    """Generate Mermaid class diagram for services."""
    lines = []
    lines.append("```mermaid")
    lines.append("classDiagram")

    for service in services[:10]:
        lines.append(f"    class {service} {{")
        lines.append("        +execute()")
        lines.append("        +validate()")
        lines.append("    }")

    # Add relationships
    if len(services) > 1:
        for service in services[1:5]:
            lines.append(f"    {services[0]} --> {service}")

    lines.append("```")
    return "\n".join(lines)


def generate_mermaid_deps(imports: Dict[str, Set[str]]) -> str:
    """Generate Mermaid dependency graph."""
    lines = []
    lines.append("```mermaid")
    lines.append("flowchart LR")

    added = set()
    count = 0

    for module, deps in imports.items():
        if count >= 20:
            break
        for dep in deps:
            if count >= 20:
                break
            key = f"{module}->{dep}"
            if key not in added:
                module_id = re.sub(r'[^a-zA-Z0-9]', '', module)
                dep_id = re.sub(r'[^a-zA-Z0-9]', '', dep)
                lines.append(f"    {module_id}[{module}] --> {dep_id}[{dep}]")
                added.add(key)
                count += 1

    lines.append("```")
    return "\n".join(lines)


# ============================================================================
# MAIN OUTPUT
# ============================================================================

def generate_output(root_path: Path, diagram_type: str, output_format: str, depth: int) -> str:
    """Generate the requested diagram output."""
    output = []

    # Analyze codebase
    structure = analyze_directory_structure(root_path, depth)
    imports = analyze_imports(root_path)
    entities = find_database_entities(root_path)
    endpoints = find_api_endpoints(root_path)
    services = find_services(root_path)

    # Group directories by layer
    layers = defaultdict(list)
    for child in structure.get('children', []):
        layer = child.get('layer') or 'infrastructure'
        layers[layer].append(child['name'])

    # Generate header
    output.append(f"# {root_path.name} - Architecture Diagrams")
    output.append("")
    output.append(f"Generated from codebase analysis.")
    output.append("")

    # Generate requested diagrams
    if diagram_type in ['architecture', 'all']:
        output.append("## Architecture Overview")
        output.append("")
        if output_format in ['ascii', 'both']:
            output.append("### ASCII Diagram")
            output.append(generate_ascii_architecture(structure, layers))
            output.append("")
        if output_format in ['mermaid', 'both']:
            output.append("### Mermaid Diagram")
            output.append(generate_mermaid_architecture(structure, layers))
            output.append("")

    if diagram_type in ['flow', 'all'] and endpoints:
        output.append("## Request Flow")
        output.append("")
        if output_format in ['ascii', 'both']:
            output.append("### ASCII Diagram")
            output.append(generate_ascii_flow(endpoints))
            output.append("")
        if output_format in ['mermaid', 'both']:
            output.append("### Mermaid Diagram")
            output.append(generate_mermaid_flow(endpoints))
            output.append("")

    if diagram_type in ['erd', 'all'] and entities:
        output.append("## Entity Relationships")
        output.append("")
        if output_format in ['mermaid', 'both']:
            output.append("### Mermaid ERD")
            output.append(generate_mermaid_erd(entities))
            output.append("")

    if diagram_type in ['components', 'all'] and services:
        output.append("## Components")
        output.append("")
        if output_format in ['ascii', 'both']:
            output.append("### ASCII Diagram")
            output.append(generate_ascii_components(services))
            output.append("")
        if output_format in ['mermaid', 'both']:
            output.append("### Mermaid Diagram")
            output.append(generate_mermaid_components(services))
            output.append("")

    if diagram_type in ['deps', 'all'] and imports:
        output.append("## Dependencies")
        output.append("")
        if output_format in ['mermaid', 'both']:
            output.append("### Mermaid Diagram")
            output.append(generate_mermaid_deps(imports))
            output.append("")

    # Directory tree
    if diagram_type == 'all':
        output.append("## Directory Structure")
        output.append("")
        output.append("```")
        output.append(generate_ascii_directory_tree(structure))
        output.append("```")
        output.append("")

    # Summary
    output.append("## Summary")
    output.append("")
    output.append(f"- **Entities found:** {len(entities)}")
    output.append(f"- **API endpoints:** {len(endpoints)}")
    output.append(f"- **Services/handlers:** {len(services)}")
    output.append(f"- **Module dependencies:** {len(imports)}")
    output.append("")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description='Generate architecture diagrams from codebase analysis'
    )
    parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help='Directory to analyze (default: current directory)'
    )
    parser.add_argument(
        '--type',
        choices=['architecture', 'flow', 'erd', 'components', 'deps', 'all'],
        default='all',
        help='Type of diagram to generate'
    )
    parser.add_argument(
        '--output',
        choices=['ascii', 'mermaid', 'both'],
        default='both',
        help='Output format'
    )
    parser.add_argument(
        '--depth',
        type=int,
        default=2,
        choices=range(1, 6),
        help='Analysis depth (1-5)'
    )

    args = parser.parse_args()

    root_path = Path(args.directory).resolve()

    if not root_path.exists():
        print(f"Error: Directory '{args.directory}' not found", file=sys.stderr)
        sys.exit(1)

    if not root_path.is_dir():
        print(f"Error: '{args.directory}' is not a directory", file=sys.stderr)
        sys.exit(1)

    output = generate_output(root_path, args.type, args.output, args.depth)
    print(output)


if __name__ == '__main__':
    main()
