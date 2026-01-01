#!/usr/bin/env python3
"""
Codebase Analyzer for Technical Writing (Enhanced)

Deep analysis of codebases using AST parsing, semantic git history analysis,
and design pattern detection to extract genuinely useful content angles.

Features:
    - AST-based design pattern detection (Python, JavaScript, TypeScript)
    - Semantic git history analysis (commit narratives, architectural pivots)
    - Dependency graph extraction
    - Class hierarchy and module coupling analysis
    - Real story extraction from code evolution

Usage:
    python analyze_codebase.py /path/to/project
    python analyze_codebase.py /path/to/project --json
    python analyze_codebase.py /path/to/project --full
    python analyze_codebase.py /path/to/project --deep  # Full AST + git analysis
"""

import os
import sys
import re
import ast
import json
import subprocess
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
import hashlib

# =============================================================================
# Configuration
# =============================================================================

LANGUAGE_MAP = {
    '.py': 'Python',
    '.js': 'JavaScript',
    '.ts': 'TypeScript',
    '.jsx': 'React',
    '.tsx': 'React TypeScript',
    '.go': 'Go',
    '.rs': 'Rust',
    '.java': 'Java',
    '.kt': 'Kotlin',
    '.rb': 'Ruby',
    '.php': 'PHP',
    '.cs': 'C#',
    '.cpp': 'C++',
    '.c': 'C',
    '.swift': 'Swift',
    '.sol': 'Solidity',
    '.vue': 'Vue',
    '.svelte': 'Svelte',
    '.scala': 'Scala',
    '.ex': 'Elixir',
    '.exs': 'Elixir',
    '.clj': 'Clojure',
    '.hs': 'Haskell',
}

FRAMEWORK_INDICATORS = {
    'package.json': ['next', 'react', 'vue', 'express', 'fastify', 'nest', 'nuxt',
                     'gatsby', 'remix', 'svelte', 'angular', 'electron', 'prisma'],
    'requirements.txt': ['django', 'flask', 'fastapi', 'streamlit', 'langchain',
                         'celery', 'sqlalchemy', 'pytest', 'pandas'],
    'pyproject.toml': ['django', 'flask', 'fastapi', 'poetry', 'pytest'],
    'Cargo.toml': ['actix', 'rocket', 'axum', 'tokio', 'serde', 'diesel'],
    'go.mod': ['gin', 'echo', 'fiber', 'gorm', 'cobra'],
    'Gemfile': ['rails', 'sinatra', 'sidekiq', 'rspec'],
    'composer.json': ['laravel', 'symfony', 'wordpress'],
}

SKIP_DIRS = {
    'node_modules', '.git', '__pycache__', '.next', 'dist', 'build',
    'venv', '.venv', 'env', '.env', 'vendor', 'target', '.idea', '.vscode',
    'coverage', '.coverage', '.pytest_cache', '.mypy_cache', '.tox',
    'egg-info', '.eggs', 'htmlcov', '.cache', 'tmp', 'temp'
}

# =============================================================================
# Data Classes for Structured Analysis
# =============================================================================

@dataclass
class ClassInfo:
    """Information about a class/type definition."""
    name: str
    file: str
    line: int
    bases: List[str]
    methods: List[str]
    decorators: List[str]
    docstring: Optional[str]
    is_abstract: bool = False
    is_dataclass: bool = False


@dataclass
class FunctionInfo:
    """Information about a function/method."""
    name: str
    file: str
    line: int
    args: List[str]
    decorators: List[str]
    docstring: Optional[str]
    calls: List[str]
    complexity: int = 1


@dataclass
class ImportInfo:
    """Information about imports."""
    module: str
    names: List[str]
    file: str
    is_relative: bool = False


@dataclass
class DesignPattern:
    """Detected design pattern."""
    name: str
    confidence: float  # 0.0 to 1.0
    evidence: List[str]
    files: List[str]
    description: str


@dataclass
class GitCommitNarrative:
    """Semantic analysis of git commit."""
    sha: str
    message: str
    date: str
    author: str
    category: str  # feature, fix, refactor, docs, test, chore
    impact: str    # major, minor, patch
    files_changed: int
    insertions: int
    deletions: int
    story_value: float  # 0.0 to 1.0 - how interesting for content


@dataclass
class ArchitecturalPivot:
    """Significant architectural change detected in history."""
    date: str
    description: str
    before_pattern: str
    after_pattern: str
    commits: List[str]
    significance: str  # high, medium, low


# =============================================================================
# AST Analysis - Python
# =============================================================================

class PythonASTAnalyzer(ast.NodeVisitor):
    """Deep AST analysis for Python files."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.classes: List[ClassInfo] = []
        self.functions: List[FunctionInfo] = []
        self.imports: List[ImportInfo] = []
        self.global_vars: List[str] = []
        self.complexity_score = 0
        self._current_class = None

    def analyze(self, source: str) -> Dict[str, Any]:
        """Parse and analyze Python source code."""
        try:
            tree = ast.parse(source)
            self.visit(tree)
            return {
                "classes": [asdict(c) for c in self.classes],
                "functions": [asdict(f) for f in self.functions],
                "imports": [asdict(i) for i in self.imports],
                "global_vars": self.global_vars,
                "complexity_score": self.complexity_score,
            }
        except SyntaxError:
            return {"error": "Syntax error in file"}

    def visit_ClassDef(self, node: ast.ClassDef):
        """Extract class information."""
        bases = [self._get_name(b) for b in node.bases]
        decorators = [self._get_decorator_name(d) for d in node.decorator_list]
        methods = [n.name for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]

        docstring = ast.get_docstring(node)

        is_abstract = any('abstract' in d.lower() for d in decorators) or \
                      any('ABC' in b or 'Abstract' in b for b in bases)
        is_dataclass = 'dataclass' in decorators

        class_info = ClassInfo(
            name=node.name,
            file=self.file_path,
            line=node.lineno,
            bases=bases,
            methods=methods,
            decorators=decorators,
            docstring=docstring[:200] if docstring else None,
            is_abstract=is_abstract,
            is_dataclass=is_dataclass,
        )
        self.classes.append(class_info)

        # Visit methods within class
        old_class = self._current_class
        self._current_class = node.name
        self.generic_visit(node)
        self._current_class = old_class

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self._process_function(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self._process_function(node, is_async=True)

    def _process_function(self, node, is_async: bool = False):
        """Extract function information."""
        if self._current_class and node.name.startswith('_') and node.name != '__init__':
            # Skip private methods for brevity
            self.generic_visit(node)
            return

        decorators = [self._get_decorator_name(d) for d in node.decorator_list]
        args = [arg.arg for arg in node.args.args if arg.arg != 'self']
        docstring = ast.get_docstring(node)

        # Calculate cyclomatic complexity (simplified)
        complexity = self._calculate_complexity(node)
        self.complexity_score += complexity

        # Extract function calls
        calls = self._extract_calls(node)

        func_info = FunctionInfo(
            name=node.name,
            file=self.file_path,
            line=node.lineno,
            args=args,
            decorators=decorators,
            docstring=docstring[:200] if docstring else None,
            calls=calls[:10],  # Limit to 10 most important calls
            complexity=complexity,
        )

        if not self._current_class:  # Only add module-level functions
            self.functions.append(func_info)

        self.generic_visit(node)

    def visit_Import(self, node: ast.Import):
        for alias in node.names:
            self.imports.append(ImportInfo(
                module=alias.name,
                names=[alias.asname or alias.name],
                file=self.file_path,
                is_relative=False,
            ))

    def visit_ImportFrom(self, node: ast.ImportFrom):
        if node.module:
            self.imports.append(ImportInfo(
                module=node.module,
                names=[alias.name for alias in node.names],
                file=self.file_path,
                is_relative=node.level > 0,
            ))

    def visit_Assign(self, node: ast.Assign):
        """Track global variable assignments."""
        if not self._current_class:
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id.isupper():
                    self.global_vars.append(target.id)
        self.generic_visit(node)

    def _get_name(self, node) -> str:
        """Get string representation of a node."""
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return f"{self._get_name(node.value)}.{node.attr}"
        elif isinstance(node, ast.Subscript):
            return f"{self._get_name(node.value)}[...]"
        return "unknown"

    def _get_decorator_name(self, node) -> str:
        """Get decorator name."""
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Call):
            return self._get_name(node.func)
        elif isinstance(node, ast.Attribute):
            return f"{self._get_name(node.value)}.{node.attr}"
        return "unknown"

    def _calculate_complexity(self, node) -> int:
        """Calculate cyclomatic complexity (simplified)."""
        complexity = 1
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.ExceptHandler,
                                  ast.With, ast.Assert, ast.comprehension)):
                complexity += 1
            elif isinstance(child, ast.BoolOp):
                complexity += len(child.values) - 1
        return complexity

    def _extract_calls(self, node) -> List[str]:
        """Extract function/method calls within a function."""
        calls = []
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                call_name = self._get_name(child.func)
                if call_name != "unknown" and not call_name.startswith("self."):
                    calls.append(call_name)
        return list(set(calls))


# =============================================================================
# JavaScript/TypeScript Analysis (Regex-based, more reliable than partial AST)
# =============================================================================

class JSAnalyzer:
    """JavaScript/TypeScript analysis using regex patterns."""

    # Patterns for JS/TS analysis
    CLASS_PATTERN = re.compile(
        r'(?:export\s+)?(?:abstract\s+)?class\s+(\w+)(?:\s+extends\s+(\w+))?(?:\s+implements\s+([\w,\s]+))?',
        re.MULTILINE
    )
    FUNCTION_PATTERN = re.compile(
        r'(?:export\s+)?(?:async\s+)?function\s+(\w+)\s*\(([^)]*)\)',
        re.MULTILINE
    )
    ARROW_FUNC_PATTERN = re.compile(
        r'(?:export\s+)?(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?\([^)]*\)\s*=>',
        re.MULTILINE
    )
    INTERFACE_PATTERN = re.compile(
        r'(?:export\s+)?interface\s+(\w+)(?:\s+extends\s+([\w,\s]+))?',
        re.MULTILINE
    )
    TYPE_PATTERN = re.compile(
        r'(?:export\s+)?type\s+(\w+)\s*=',
        re.MULTILINE
    )
    IMPORT_PATTERN = re.compile(
        r'import\s+(?:{([^}]+)}|(\w+))\s+from\s+[\'"]([^\'"]+)[\'"]',
        re.MULTILINE
    )
    REACT_COMPONENT_PATTERN = re.compile(
        r'(?:export\s+)?(?:default\s+)?(?:function|const)\s+(\w+).*?(?:React\.FC|JSX\.Element|=>.*?<)',
        re.MULTILINE | re.DOTALL
    )
    HOOK_PATTERN = re.compile(
        r'(?:export\s+)?(?:const|function)\s+(use\w+)',
        re.MULTILINE
    )

    def analyze(self, source: str, file_path: str) -> Dict[str, Any]:
        """Analyze JavaScript/TypeScript source."""
        results = {
            "classes": [],
            "functions": [],
            "interfaces": [],
            "types": [],
            "imports": [],
            "react_components": [],
            "hooks": [],
        }

        # Extract classes
        for match in self.CLASS_PATTERN.finditer(source):
            results["classes"].append({
                "name": match.group(1),
                "extends": match.group(2),
                "implements": match.group(3).split(',') if match.group(3) else [],
            })

        # Extract functions
        for match in self.FUNCTION_PATTERN.finditer(source):
            results["functions"].append({
                "name": match.group(1),
                "params": match.group(2),
            })

        # Extract arrow functions
        for match in self.ARROW_FUNC_PATTERN.finditer(source):
            results["functions"].append({
                "name": match.group(1),
                "type": "arrow",
            })

        # Extract interfaces (TypeScript)
        for match in self.INTERFACE_PATTERN.finditer(source):
            results["interfaces"].append({
                "name": match.group(1),
                "extends": match.group(2).split(',') if match.group(2) else [],
            })

        # Extract type aliases
        for match in self.TYPE_PATTERN.finditer(source):
            results["types"].append(match.group(1))

        # Extract imports
        for match in self.IMPORT_PATTERN.finditer(source):
            names = match.group(1) or match.group(2)
            results["imports"].append({
                "names": [n.strip() for n in names.split(',')] if names else [],
                "from": match.group(3),
            })

        # Extract React components
        for match in self.REACT_COMPONENT_PATTERN.finditer(source):
            name = match.group(1)
            if name[0].isupper():  # React components start with uppercase
                results["react_components"].append(name)

        # Extract hooks
        for match in self.HOOK_PATTERN.finditer(source):
            results["hooks"].append(match.group(1))

        return results


# =============================================================================
# Design Pattern Detection
# =============================================================================

class DesignPatternDetector:
    """Detect design patterns from AST analysis results."""

    def __init__(self):
        self.patterns: List[DesignPattern] = []

    def detect(self, all_classes: List[ClassInfo], all_functions: List[FunctionInfo],
               all_imports: List[ImportInfo], project_structure: Dict) -> List[DesignPattern]:
        """Detect design patterns from analyzed code."""
        self.patterns = []

        # Run all detection methods
        self._detect_singleton(all_classes)
        self._detect_factory(all_classes, all_functions)
        self._detect_observer(all_classes, all_functions)
        self._detect_strategy(all_classes)
        self._detect_decorator(all_classes)
        self._detect_repository(all_classes, project_structure)
        self._detect_dependency_injection(all_classes, all_functions)
        self._detect_mvc_layers(project_structure, all_classes)
        self._detect_event_driven(all_classes, all_functions)

        # Sort by confidence
        self.patterns.sort(key=lambda p: p.confidence, reverse=True)
        return self.patterns

    def _detect_singleton(self, classes: List[ClassInfo]):
        """Detect Singleton pattern."""
        evidence = []
        files = []

        for cls in classes:
            indicators = 0

            # Check for _instance attribute or similar
            if any('instance' in m.lower() for m in cls.methods):
                indicators += 1
                evidence.append(f"{cls.name} has instance-related method")

            # Check for __new__ override
            if '__new__' in cls.methods:
                indicators += 1
                evidence.append(f"{cls.name} overrides __new__")

            # Check for get_instance pattern
            if any('get_instance' in m.lower() or 'getinstance' in m.lower() for m in cls.methods):
                indicators += 2
                evidence.append(f"{cls.name} has get_instance method")
                files.append(cls.file)

        if evidence:
            confidence = min(1.0, len(evidence) * 0.3)
            self.patterns.append(DesignPattern(
                name="Singleton",
                confidence=confidence,
                evidence=evidence[:5],
                files=list(set(files)),
                description="Single instance management pattern"
            ))

    def _detect_factory(self, classes: List[ClassInfo], functions: List[FunctionInfo]):
        """Detect Factory pattern."""
        evidence = []
        files = []

        factory_indicators = ['factory', 'create', 'make', 'build', 'get_']

        for cls in classes:
            if any(ind in cls.name.lower() for ind in factory_indicators):
                evidence.append(f"Class {cls.name} suggests factory pattern")
                files.append(cls.file)

            # Check for create methods that return different types
            create_methods = [m for m in cls.methods if any(ind in m.lower() for ind in factory_indicators)]
            if len(create_methods) >= 2:
                evidence.append(f"{cls.name} has multiple creation methods: {create_methods[:3]}")
                files.append(cls.file)

        for func in functions:
            if any(ind in func.name.lower() for ind in factory_indicators):
                evidence.append(f"Function {func.name} suggests factory pattern")
                files.append(func.file)

        if evidence:
            confidence = min(1.0, len(evidence) * 0.25)
            self.patterns.append(DesignPattern(
                name="Factory",
                confidence=confidence,
                evidence=evidence[:5],
                files=list(set(files)),
                description="Object creation abstraction"
            ))

    def _detect_observer(self, classes: List[ClassInfo], functions: List[FunctionInfo]):
        """Detect Observer/Event pattern."""
        evidence = []
        files = []

        observer_indicators = ['observer', 'listener', 'subscribe', 'publish', 'emit',
                               'on_', 'notify', 'broadcast', 'event', 'handler']

        for cls in classes:
            matching_methods = [m for m in cls.methods
                               if any(ind in m.lower() for ind in observer_indicators)]
            if len(matching_methods) >= 2:
                evidence.append(f"{cls.name} has observer methods: {matching_methods[:3]}")
                files.append(cls.file)

        if evidence:
            confidence = min(1.0, len(evidence) * 0.3)
            self.patterns.append(DesignPattern(
                name="Observer/Event-Driven",
                confidence=confidence,
                evidence=evidence[:5],
                files=list(set(files)),
                description="Publish-subscribe communication pattern"
            ))

    def _detect_strategy(self, classes: List[ClassInfo]):
        """Detect Strategy pattern."""
        evidence = []
        files = []

        # Look for abstract base classes with concrete implementations
        abstract_classes = [c for c in classes if c.is_abstract or 'Base' in c.name or 'Abstract' in c.name]

        for abstract in abstract_classes:
            # Find classes that inherit from this abstract class
            implementations = [c for c in classes if abstract.name in c.bases]
            if len(implementations) >= 2:
                evidence.append(f"{abstract.name} has {len(implementations)} implementations: "
                              f"{[c.name for c in implementations[:3]]}")
                files.extend([c.file for c in implementations])
                files.append(abstract.file)

        if evidence:
            confidence = min(1.0, len(evidence) * 0.4)
            self.patterns.append(DesignPattern(
                name="Strategy",
                confidence=confidence,
                evidence=evidence[:5],
                files=list(set(files)),
                description="Interchangeable algorithm implementations"
            ))

    def _detect_decorator(self, classes: List[ClassInfo]):
        """Detect Decorator pattern."""
        evidence = []
        files = []

        for cls in classes:
            # Check if class wraps another class of same base type
            if cls.bases:
                for other in classes:
                    if other.name in cls.bases and cls.name != other.name:
                        # Check if constructor takes an instance of base type
                        if '__init__' in cls.methods:
                            evidence.append(f"{cls.name} may wrap {other.name}")
                            files.extend([cls.file, other.file])

        if evidence:
            confidence = min(1.0, len(evidence) * 0.35)
            self.patterns.append(DesignPattern(
                name="Decorator",
                confidence=confidence,
                evidence=evidence[:5],
                files=list(set(files)),
                description="Dynamic behavior extension"
            ))

    def _detect_repository(self, classes: List[ClassInfo], structure: Dict):
        """Detect Repository pattern."""
        evidence = []
        files = []

        repo_indicators = ['repository', 'repo', 'dao', 'store', 'storage']
        crud_methods = ['get', 'find', 'save', 'create', 'update', 'delete', 'list', 'all']

        for cls in classes:
            if any(ind in cls.name.lower() for ind in repo_indicators):
                evidence.append(f"Class {cls.name} follows repository naming")
                files.append(cls.file)

                # Check for CRUD methods
                crud_found = [m for m in cls.methods if any(c in m.lower() for c in crud_methods)]
                if len(crud_found) >= 3:
                    evidence.append(f"{cls.name} has CRUD methods: {crud_found[:4]}")

        # Check directory structure
        dirs = structure.get("directories", [])
        if any('repositories' in d.lower() or 'repos' in d.lower() for d in dirs):
            evidence.append("Project has repositories directory")

        if evidence:
            confidence = min(1.0, len(evidence) * 0.3)
            self.patterns.append(DesignPattern(
                name="Repository",
                confidence=confidence,
                evidence=evidence[:5],
                files=list(set(files)),
                description="Data access abstraction layer"
            ))

    def _detect_dependency_injection(self, classes: List[ClassInfo], functions: List[FunctionInfo]):
        """Detect Dependency Injection pattern."""
        evidence = []
        files = []

        di_indicators = ['inject', 'provider', 'container', 'resolve', 'bind']

        for cls in classes:
            # Check for DI decorators
            if any(any(ind in d.lower() for ind in di_indicators) for d in cls.decorators):
                evidence.append(f"{cls.name} uses DI decorators")
                files.append(cls.file)

            # Check for constructor injection (many constructor params)
            if '__init__' in cls.methods and len(cls.methods) > 1:
                # This is a heuristic - real detection would need param analysis
                evidence.append(f"{cls.name} may use constructor injection")
                files.append(cls.file)

        if evidence:
            confidence = min(1.0, len(evidence) * 0.25)
            self.patterns.append(DesignPattern(
                name="Dependency Injection",
                confidence=confidence,
                evidence=evidence[:5],
                files=list(set(files)),
                description="Inversion of control for dependencies"
            ))

    def _detect_mvc_layers(self, structure: Dict, classes: List[ClassInfo]):
        """Detect MVC/layered architecture."""
        evidence = []
        files = []
        dirs = structure.get("directories", [])

        # Layer detection
        layers_found = []
        layer_map = {
            'model': ['models', 'model', 'entities', 'domain'],
            'view': ['views', 'view', 'templates', 'pages', 'components'],
            'controller': ['controllers', 'controller', 'handlers', 'routes', 'api'],
            'service': ['services', 'service', 'usecases', 'business'],
            'repository': ['repositories', 'repos', 'dao', 'data'],
        }

        for layer, indicators in layer_map.items():
            if any(any(ind in d.lower() for ind in indicators) for d in dirs):
                layers_found.append(layer)
                evidence.append(f"Found {layer} layer in directory structure")

        if len(layers_found) >= 3:
            confidence = min(1.0, len(layers_found) * 0.2)
            self.patterns.append(DesignPattern(
                name="Layered Architecture",
                confidence=confidence,
                evidence=evidence[:5],
                files=files,
                description=f"Separation into layers: {', '.join(layers_found)}"
            ))

    def _detect_event_driven(self, classes: List[ClassInfo], functions: List[FunctionInfo]):
        """Detect event-driven architecture."""
        evidence = []
        files = []

        event_indicators = ['event', 'message', 'queue', 'bus', 'dispatch', 'emit', 'publish']

        for cls in classes:
            if any(ind in cls.name.lower() for ind in event_indicators):
                evidence.append(f"Class {cls.name} suggests event-driven pattern")
                files.append(cls.file)

        for func in functions:
            if any(ind in func.name.lower() for ind in event_indicators):
                evidence.append(f"Function {func.name} suggests event handling")
                files.append(func.file)

        if evidence:
            confidence = min(1.0, len(evidence) * 0.25)
            self.patterns.append(DesignPattern(
                name="Event-Driven",
                confidence=confidence,
                evidence=evidence[:5],
                files=list(set(files)),
                description="Asynchronous event-based communication"
            ))


# =============================================================================
# Semantic Git History Analysis
# =============================================================================

class GitHistoryAnalyzer:
    """Analyze git history for narrative extraction."""

    # Commit message patterns for categorization
    CATEGORY_PATTERNS = {
        'feature': [r'^feat', r'^add', r'^new', r'^implement', r'^create'],
        'fix': [r'^fix', r'^bug', r'^patch', r'^resolve', r'^correct'],
        'refactor': [r'^refactor', r'^restructure', r'^reorganize', r'^clean', r'^improve'],
        'docs': [r'^docs?', r'^readme', r'^comment', r'^documentation'],
        'test': [r'^test', r'^spec', r'^coverage'],
        'chore': [r'^chore', r'^build', r'^ci', r'^deps', r'^upgrade', r'^bump'],
        'style': [r'^style', r'^format', r'^lint'],
        'perf': [r'^perf', r'^optimize', r'^speed', r'^fast'],
    }

    # Keywords that indicate high story value
    STORY_KEYWORDS = [
        'finally', 'breakthrough', 'major', 'complete', 'milestone',
        'rewrite', 'migration', 'upgrade', 'security', 'critical',
        'performance', 'optimization', 'architecture', 'redesign',
        'launch', 'release', 'ship', 'deploy', 'production',
    ]

    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.commits: List[GitCommitNarrative] = []
        self.pivots: List[ArchitecturalPivot] = []

    def analyze(self, max_commits: int = 200) -> Dict[str, Any]:
        """Perform full git history analysis."""
        if not (self.project_path / '.git').exists():
            return {"error": "Not a git repository"}

        self._load_commits(max_commits)
        self._detect_pivots()
        self._extract_story_arcs()

        return {
            "total_commits": len(self.commits),
            "commit_narratives": [asdict(c) for c in self.commits[:50]],
            "pivots": [asdict(p) for p in self.pivots],
            "category_breakdown": self._get_category_breakdown(),
            "story_worthy_commits": self._get_story_worthy_commits(),
            "timeline_summary": self._get_timeline_summary(),
            "contributor_stories": self._get_contributor_stories(),
        }

    def _load_commits(self, max_commits: int):
        """Load and parse commit history."""
        try:
            # Get detailed commit info
            result = subprocess.run(
                ['git', 'log', f'-n{max_commits}', '--pretty=format:%H|%s|%ai|%an|%b|||'],
                cwd=self.project_path,
                capture_output=True, text=True, timeout=30
            )

            if result.returncode != 0:
                return

            commits_raw = result.stdout.split('|||')

            for commit_str in commits_raw:
                if not commit_str.strip():
                    continue

                parts = commit_str.strip().split('|')
                if len(parts) < 4:
                    continue

                sha = parts[0]
                message = parts[1]
                date = parts[2]
                author = parts[3]
                body = parts[4] if len(parts) > 4 else ""

                # Get stats for this commit
                stats = self._get_commit_stats(sha)

                # Categorize commit
                category = self._categorize_commit(message)
                impact = self._determine_impact(message, stats)
                story_value = self._calculate_story_value(message, body, stats)

                self.commits.append(GitCommitNarrative(
                    sha=sha[:8],
                    message=message[:200],
                    date=date[:10],
                    author=author,
                    category=category,
                    impact=impact,
                    files_changed=stats.get('files', 0),
                    insertions=stats.get('insertions', 0),
                    deletions=stats.get('deletions', 0),
                    story_value=story_value,
                ))

        except Exception as e:
            pass

    def _get_commit_stats(self, sha: str) -> Dict[str, int]:
        """Get stats for a specific commit."""
        try:
            result = subprocess.run(
                ['git', 'show', '--stat', '--format=', sha],
                cwd=self.project_path,
                capture_output=True, text=True, timeout=10
            )

            stats = {'files': 0, 'insertions': 0, 'deletions': 0}

            for line in result.stdout.split('\n'):
                if 'file' in line and 'changed' in line:
                    # Parse "X files changed, Y insertions(+), Z deletions(-)"
                    match = re.search(r'(\d+) files? changed', line)
                    if match:
                        stats['files'] = int(match.group(1))

                    match = re.search(r'(\d+) insertions?', line)
                    if match:
                        stats['insertions'] = int(match.group(1))

                    match = re.search(r'(\d+) deletions?', line)
                    if match:
                        stats['deletions'] = int(match.group(1))

            return stats

        except Exception:
            return {'files': 0, 'insertions': 0, 'deletions': 0}

    def _categorize_commit(self, message: str) -> str:
        """Categorize commit by message."""
        message_lower = message.lower()

        for category, patterns in self.CATEGORY_PATTERNS.items():
            for pattern in patterns:
                if re.match(pattern, message_lower):
                    return category

        return 'other'

    def _determine_impact(self, message: str, stats: Dict) -> str:
        """Determine commit impact level."""
        message_lower = message.lower()

        # Major indicators
        if any(word in message_lower for word in ['breaking', 'major', 'rewrite', 'migration']):
            return 'major'

        # Large file changes
        if stats.get('files', 0) > 20 or stats.get('insertions', 0) > 500:
            return 'major'

        # Minor indicators
        if stats.get('files', 0) > 5 or stats.get('insertions', 0) > 100:
            return 'minor'

        return 'patch'

    def _calculate_story_value(self, message: str, body: str, stats: Dict) -> float:
        """Calculate how story-worthy a commit is."""
        score = 0.0
        full_text = f"{message} {body}".lower()

        # Story keywords
        for keyword in self.STORY_KEYWORDS:
            if keyword in full_text:
                score += 0.15

        # Major changes
        if stats.get('files', 0) > 10:
            score += 0.2
        if stats.get('insertions', 0) > 300:
            score += 0.2

        # Narrative indicators
        if len(message) > 50:  # Detailed message
            score += 0.1
        if body and len(body) > 100:  # Has description
            score += 0.15

        return min(1.0, score)

    def _detect_pivots(self):
        """Detect architectural pivots in history."""
        if len(self.commits) < 10:
            return

        # Look for clusters of high-impact commits
        for i, commit in enumerate(self.commits):
            if commit.impact == 'major' and commit.story_value > 0.5:
                # Look for related commits nearby
                related = []
                for j in range(max(0, i-5), min(len(self.commits), i+5)):
                    if self.commits[j].category in ['refactor', 'feature'] and \
                       self.commits[j].impact in ['major', 'minor']:
                        related.append(self.commits[j].sha)

                if len(related) >= 2:
                    self.pivots.append(ArchitecturalPivot(
                        date=commit.date,
                        description=commit.message,
                        before_pattern="(requires manual analysis)",
                        after_pattern="(requires manual analysis)",
                        commits=related[:5],
                        significance='high' if len(related) >= 3 else 'medium',
                    ))

    def _extract_story_arcs(self):
        """Extract narrative arcs from commit history."""
        # This method identifies sequences that tell a story
        # (e.g., problem -> attempts -> solution)
        pass  # Placeholder for more sophisticated analysis

    def _get_category_breakdown(self) -> Dict[str, int]:
        """Get breakdown of commits by category."""
        breakdown = Counter(c.category for c in self.commits)
        return dict(breakdown)

    def _get_story_worthy_commits(self) -> List[Dict]:
        """Get commits with highest story value."""
        sorted_commits = sorted(self.commits, key=lambda c: c.story_value, reverse=True)
        return [asdict(c) for c in sorted_commits[:10]]

    def _get_timeline_summary(self) -> Dict[str, Any]:
        """Get timeline summary of project."""
        if not self.commits:
            return {}

        # Group by month
        monthly = defaultdict(lambda: {'commits': 0, 'features': 0, 'fixes': 0})

        for commit in self.commits:
            month = commit.date[:7]  # YYYY-MM
            monthly[month]['commits'] += 1
            if commit.category == 'feature':
                monthly[month]['features'] += 1
            elif commit.category == 'fix':
                monthly[month]['fixes'] += 1

        return {
            "first_commit": self.commits[-1].date if self.commits else None,
            "last_commit": self.commits[0].date if self.commits else None,
            "monthly_activity": dict(monthly),
        }

    def _get_contributor_stories(self) -> List[Dict]:
        """Get contributor contribution patterns."""
        contributors = defaultdict(lambda: {
            'commits': 0, 'features': 0, 'fixes': 0,
            'first_commit': None, 'last_commit': None
        })

        for commit in self.commits:
            c = contributors[commit.author]
            c['commits'] += 1
            if commit.category == 'feature':
                c['features'] += 1
            elif commit.category == 'fix':
                c['fixes'] += 1
            if c['first_commit'] is None:
                c['first_commit'] = commit.date
            c['last_commit'] = commit.date

        # Convert to list and sort by commit count
        result = [{'name': name, **stats} for name, stats in contributors.items()]
        result.sort(key=lambda x: x['commits'], reverse=True)

        return result[:10]


# =============================================================================
# Main Analysis Functions
# =============================================================================

def analyze_project(project_path: str, full_analysis: bool = False,
                    deep_analysis: bool = False) -> Dict[str, Any]:
    """Main analysis function with enhanced capabilities."""
    path = Path(project_path)
    if not path.exists():
        return {"error": f"Path not found: {project_path}"}

    results = {
        "project_name": path.name,
        "languages": defaultdict(int),
        "frameworks": [],
        "files": {"total": 0, "by_type": defaultdict(int)},
        "structure": {"directories": [], "tree": []},
        "key_files": [],
        "largest_files": [],
        "complexity": {},
        "architecture": {},
        "dependencies": {},
        "api_endpoints": [],
        "story_hooks": [],
        "git_insights": {},
        "test_info": {},
        "content_angles": [],
        # Enhanced analysis results
        "ast_analysis": {
            "classes": [],
            "functions": [],
            "imports": [],
            "design_patterns": [],
        },
        "git_narrative": {},
    }

    # Collect all files
    all_files = []
    all_dirs = set()

    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        rel_root = Path(root).relative_to(path)

        for d in dirs:
            all_dirs.add(str(rel_root / d))

        for file in files:
            file_path = Path(root) / file
            rel_path = rel_root / file
            ext = file_path.suffix.lower()

            results["files"]["total"] += 1
            results["files"]["by_type"][ext] += 1

            if ext in LANGUAGE_MAP:
                results["languages"][LANGUAGE_MAP[ext]] += 1

            try:
                size = file_path.stat().st_size
                lines = count_lines(file_path)
                file_info = {
                    "path": str(rel_path),
                    "size": size,
                    "lines": lines,
                    "ext": ext
                }
                all_files.append(file_info)
            except Exception:
                pass

    results["structure"]["directories"] = list(all_dirs)

    # Convert defaultdicts
    results["languages"] = dict(results["languages"])
    results["files"]["by_type"] = dict(results["files"]["by_type"])

    # Sort files by size
    all_files.sort(key=lambda x: x.get("lines", 0), reverse=True)
    results["largest_files"] = all_files[:10]

    # Basic analysis
    results["frameworks"] = detect_frameworks(path)
    results["structure"]["tree"] = generate_structure(path, max_depth=2)
    results["key_files"] = identify_key_files(path, all_files)
    results["complexity"] = calculate_complexity(all_files)
    results["dependencies"] = analyze_dependencies(path)
    results["test_info"] = analyze_tests(path, all_files)

    # Enhanced AST analysis
    if deep_analysis or full_analysis:
        ast_results = perform_ast_analysis(path, all_files)
        results["ast_analysis"] = ast_results

        # Design pattern detection
        detector = DesignPatternDetector()
        patterns = detector.detect(
            [ClassInfo(**c) for c in ast_results.get("classes", []) if isinstance(c, dict)],
            [FunctionInfo(**f) for f in ast_results.get("functions", []) if isinstance(f, dict)],
            [ImportInfo(**i) for i in ast_results.get("imports", []) if isinstance(i, dict)],
            results["structure"]
        )
        results["ast_analysis"]["design_patterns"] = [asdict(p) for p in patterns]

    # Git narrative analysis
    if deep_analysis:
        git_analyzer = GitHistoryAnalyzer(path)
        results["git_narrative"] = git_analyzer.analyze()
    else:
        results["git_insights"] = get_basic_git_insights(path)

    # Extract story hooks (enhanced)
    if full_analysis or deep_analysis:
        results["story_hooks"] = extract_enhanced_story_hooks(path, all_files)
        results["api_endpoints"] = extract_api_endpoints(path, all_files)

    # Generate content angles (using all analysis)
    results["content_angles"] = suggest_enhanced_angles(results, deep_analysis)

    return results


def perform_ast_analysis(path: Path, all_files: List[Dict]) -> Dict[str, Any]:
    """Perform AST analysis on Python and JS/TS files."""
    results = {
        "classes": [],
        "functions": [],
        "imports": [],
        "react_components": [],
        "hooks": [],
        "complexity_total": 0,
    }

    py_analyzer = PythonASTAnalyzer("")
    js_analyzer = JSAnalyzer()

    # Analyze Python files
    for file_info in all_files:
        if file_info["ext"] != ".py":
            continue
        if file_info.get("lines", 0) > 2000:  # Skip very large files
            continue

        try:
            full_path = path / file_info["path"]
            source = full_path.read_text(encoding='utf-8', errors='ignore')

            analyzer = PythonASTAnalyzer(file_info["path"])
            analysis = analyzer.analyze(source)

            if "error" not in analysis:
                results["classes"].extend(analysis.get("classes", []))
                results["functions"].extend(analysis.get("functions", []))
                results["imports"].extend(analysis.get("imports", []))
                results["complexity_total"] += analysis.get("complexity_score", 0)
        except Exception:
            pass

    # Analyze JS/TS files
    for file_info in all_files:
        if file_info["ext"] not in [".js", ".ts", ".jsx", ".tsx"]:
            continue
        if file_info.get("lines", 0) > 2000:
            continue

        try:
            full_path = path / file_info["path"]
            source = full_path.read_text(encoding='utf-8', errors='ignore')

            analysis = js_analyzer.analyze(source, file_info["path"])

            # Convert JS classes to common format
            for cls in analysis.get("classes", []):
                results["classes"].append({
                    "name": cls["name"],
                    "file": file_info["path"],
                    "line": 0,
                    "bases": [cls["extends"]] if cls.get("extends") else [],
                    "methods": [],
                    "decorators": [],
                    "docstring": None,
                })

            results["react_components"].extend(analysis.get("react_components", []))
            results["hooks"].extend(analysis.get("hooks", []))
        except Exception:
            pass

    # Limit results
    results["classes"] = results["classes"][:50]
    results["functions"] = results["functions"][:50]
    results["imports"] = results["imports"][:100]

    return results


def extract_enhanced_story_hooks(path: Path, all_files: List[Dict]) -> List[Dict]:
    """Extract story hooks with enhanced patterns."""
    hooks = []

    # Enhanced patterns
    patterns = [
        (r'TODO:?\s*(.+)', 'TODO', 5),
        (r'FIXME:?\s*(.+)', 'FIXME', 4),
        (r'HACK:?\s*(.+)', 'HACK', 3),
        (r'BUG:?\s*(.+)', 'BUG', 2),
        (r'SECURITY:?\s*(.+)', 'SECURITY', 1),
        (r'OPTIMIZE:?\s*(.+)', 'OPTIMIZE', 6),
        (r'REVIEW:?\s*(.+)', 'REVIEW', 7),
        (r'NOTE:?\s*(.+)', 'NOTE', 8),
        # New patterns for better story extraction
        (r'WARNING:?\s*(.+)', 'WARNING', 3),
        (r'IMPORTANT:?\s*(.+)', 'IMPORTANT', 2),
        (r'DECISION:?\s*(.+)', 'DECISION', 1),
        (r'WHY:?\s*(.+)', 'WHY', 1),  # Explanation comments
        (r'TRADEOFF:?\s*(.+)', 'TRADEOFF', 1),
    ]

    for file_info in all_files:
        if file_info["ext"] not in LANGUAGE_MAP:
            continue
        if file_info.get("lines", 0) > 2000:
            continue

        try:
            full_path = path / file_info["path"]
            content = full_path.read_text(encoding='utf-8', errors='ignore')

            for line_num, line in enumerate(content.split('\n'), 1):
                for pattern, hook_type, priority in patterns:
                    match = re.search(pattern, line, re.IGNORECASE)
                    if match:
                        hooks.append({
                            "type": hook_type,
                            "message": match.group(1).strip()[:150],
                            "file": file_info["path"],
                            "line": line_num,
                            "priority": priority,
                        })
        except Exception:
            pass

    # Sort by priority and limit
    hooks.sort(key=lambda x: x["priority"])
    return hooks[:20]


def extract_api_endpoints(path: Path, all_files: List[Dict]) -> List[Dict]:
    """Extract API endpoints from code."""
    endpoints = []

    patterns = {
        '.py': [
            (r'@app\.(get|post|put|delete|patch)\([\'"]([^\'"]+)', 'Flask/FastAPI'),
            (r'@router\.(get|post|put|delete|patch)\([\'"]([^\'"]+)', 'FastAPI Router'),
            (r'path\([\'"]([^\'"]+)[\'"]', 'Django'),
        ],
        '.js': [
            (r'app\.(get|post|put|delete|patch)\([\'"]([^\'"]+)', 'Express'),
            (r'router\.(get|post|put|delete|patch)\([\'"]([^\'"]+)', 'Express Router'),
        ],
        '.ts': [
            (r'app\.(get|post|put|delete|patch)\([\'"]([^\'"]+)', 'Express'),
            (r'@(Get|Post|Put|Delete|Patch)\([\'"]?([^\'")\s]+)?', 'NestJS'),
        ],
    }

    for file_info in all_files:
        ext = file_info["ext"]
        if ext not in patterns:
            continue

        try:
            full_path = path / file_info["path"]
            content = full_path.read_text(encoding='utf-8', errors='ignore')

            for pattern, framework in patterns[ext]:
                for match in re.finditer(pattern, content, re.IGNORECASE):
                    groups = match.groups()
                    if len(groups) >= 2:
                        endpoints.append({
                            "method": groups[0].upper(),
                            "path": groups[1] if groups[1] else "/",
                            "framework": framework,
                            "file": file_info["path"],
                        })
                    elif len(groups) == 1:
                        endpoints.append({
                            "method": "GET",
                            "path": groups[0],
                            "framework": framework,
                            "file": file_info["path"],
                        })
        except Exception:
            pass

    return endpoints[:30]


def suggest_enhanced_angles(results: Dict, deep_analysis: bool) -> List[str]:
    """Generate content angles based on deep analysis."""
    angles = []

    # Based on design patterns
    patterns = results.get("ast_analysis", {}).get("design_patterns", [])
    for pattern in patterns[:3]:
        if pattern.get("confidence", 0) > 0.5:
            angles.append(f"How we use {pattern['name']} pattern: {pattern['description']}")

    # Based on git narrative
    git_narrative = results.get("git_narrative", {})
    if git_narrative:
        pivots = git_narrative.get("pivots", [])
        for pivot in pivots[:2]:
            angles.append(f"Architectural pivot: {pivot['description'][:100]}")

        story_commits = git_narrative.get("story_worthy_commits", [])
        for commit in story_commits[:2]:
            if commit.get("story_value", 0) > 0.6:
                angles.append(f"The story behind: {commit['message'][:80]}")

    # Based on tech stack complexity
    if results.get("frameworks"):
        fw = ", ".join(results["frameworks"][:3])
        angles.append(f"Building with {fw}: Architecture decisions")

    # Based on class hierarchy
    classes = results.get("ast_analysis", {}).get("classes", [])
    abstract_classes = [c for c in classes if c.get("is_abstract")]
    if len(abstract_classes) >= 2:
        angles.append("Our abstraction layers: Why and how we use interfaces")

    # Based on React components
    react_components = results.get("ast_analysis", {}).get("react_components", [])
    if len(react_components) > 10:
        angles.append(f"Managing {len(react_components)}+ React components: Our organization strategy")

    # Based on hooks (React)
    hooks = results.get("ast_analysis", {}).get("hooks", [])
    if hooks:
        angles.append(f"Custom hooks we built: {', '.join(hooks[:3])}")

    # Based on story hooks in code
    story_hooks = results.get("story_hooks", [])
    security_hooks = [h for h in story_hooks if h["type"] == "SECURITY"]
    decision_hooks = [h for h in story_hooks if h["type"] in ["DECISION", "WHY", "TRADEOFF"]]

    if security_hooks:
        angles.append("Security considerations in our codebase")
    if decision_hooks:
        angles.append("Engineering decisions documented in our code")

    # Based on complexity
    complexity = results.get("complexity", {})
    if complexity.get("total_lines", 0) > 10000:
        angles.append("Scaling to 10,000+ lines: Lessons in codebase organization")

    # Based on test coverage
    test_info = results.get("test_info", {})
    if test_info.get("estimated_coverage") == "high":
        angles.append("How we achieved comprehensive test coverage")

    # Generic but valuable angles
    angles.extend([
        "What I'd do differently: Lessons from building this",
        "The evolution of our architecture",
    ])

    # Deduplicate and limit
    seen = set()
    unique_angles = []
    for angle in angles:
        normalized = angle.lower()[:50]
        if normalized not in seen:
            seen.add(normalized)
            unique_angles.append(angle)

    return unique_angles[:10]


# =============================================================================
# Helper Functions (from original)
# =============================================================================

def count_lines(file_path: Path) -> int:
    """Count non-empty lines in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for line in f if line.strip())
    except Exception:
        return 0


def detect_frameworks(path: Path) -> List[str]:
    """Detect frameworks from config files."""
    frameworks = []

    for config_file, framework_names in FRAMEWORK_INDICATORS.items():
        config_path = path / config_file
        if config_path.exists():
            try:
                content = config_path.read_text().lower()
                for fw in framework_names:
                    if fw in content:
                        frameworks.append(fw.title())
            except Exception:
                pass

    # Specific file checks
    specific_checks = [
        ('next.config.js', 'Next.js'), ('next.config.ts', 'Next.js'),
        ('next.config.mjs', 'Next.js'), ('nuxt.config.js', 'Nuxt'),
        ('nuxt.config.ts', 'Nuxt'), ('svelte.config.js', 'SvelteKit'),
        ('astro.config.mjs', 'Astro'), ('remix.config.js', 'Remix'),
        ('docker-compose.yml', 'Docker'), ('docker-compose.yaml', 'Docker'),
        ('Dockerfile', 'Docker'), ('.github/workflows', 'GitHub Actions'),
    ]

    for file_or_dir, framework in specific_checks:
        if (path / file_or_dir).exists():
            if framework not in frameworks:
                frameworks.append(framework)

    return list(set(frameworks))


def analyze_dependencies(path: Path) -> Dict[str, Any]:
    """Analyze project dependencies."""
    deps = {
        "package_managers": [],
        "main_dependencies": [],
        "dev_dependencies_count": 0,
        "prod_dependencies_count": 0,
    }

    # Check package.json
    pkg_json = path / 'package.json'
    if pkg_json.exists():
        deps["package_managers"].append("npm/yarn")
        try:
            data = json.loads(pkg_json.read_text())
            prod_deps = list(data.get('dependencies', {}).keys())[:10]
            dev_deps = data.get('devDependencies', {})
            deps["main_dependencies"].extend(prod_deps)
            deps["prod_dependencies_count"] = len(data.get('dependencies', {}))
            deps["dev_dependencies_count"] = len(dev_deps)
        except Exception:
            pass

    # Check requirements.txt
    reqs = path / 'requirements.txt'
    if reqs.exists():
        deps["package_managers"].append("pip")
        try:
            lines = reqs.read_text().strip().split('\n')
            for line in lines[:10]:
                if line.strip() and not line.startswith('#'):
                    pkg = line.split('==')[0].split('>=')[0].split('<=')[0].strip()
                    if pkg:
                        deps["main_dependencies"].append(pkg)
            deps["prod_dependencies_count"] = len([l for l in lines if l.strip() and not l.startswith('#')])
        except Exception:
            pass

    # Check pyproject.toml
    if (path / 'pyproject.toml').exists():
        deps["package_managers"].append("poetry/pip")

    # Check Cargo.toml
    if (path / 'Cargo.toml').exists():
        deps["package_managers"].append("cargo")

    # Check go.mod
    if (path / 'go.mod').exists():
        deps["package_managers"].append("go modules")

    return deps


def analyze_tests(path: Path, all_files: List[Dict]) -> Dict[str, Any]:
    """Analyze test coverage and structure."""
    test_info = {
        "test_files_count": 0,
        "test_frameworks": [],
        "test_directories": [],
        "estimated_coverage": "unknown"
    }

    test_patterns = ['test_', '_test.', '.test.', '.spec.', '_spec.']
    test_dirs = ['tests', 'test', '__tests__', 'spec', 'specs']

    test_files = []
    code_files = []

    for f in all_files:
        file_path = f['path'].lower()
        file_name = Path(file_path).name.lower()

        is_test = any(p in file_name for p in test_patterns)
        is_in_test_dir = any(d in file_path.split('/') for d in test_dirs)

        if is_test or is_in_test_dir:
            test_files.append(f)
        elif f.get('ext') in LANGUAGE_MAP:
            code_files.append(f)

    test_info["test_files_count"] = len(test_files)

    # Detect test frameworks
    for f in test_files[:50]:
        try:
            content = (path / f['path']).read_text(encoding='utf-8', errors='ignore')
            if 'pytest' in content or '@pytest' in content:
                test_info["test_frameworks"].append('pytest')
            if 'unittest' in content:
                test_info["test_frameworks"].append('unittest')
            if 'jest' in content.lower() or 'describe(' in content:
                test_info["test_frameworks"].append('jest')
            if 'vitest' in content.lower():
                test_info["test_frameworks"].append('vitest')
        except Exception:
            pass

    test_info["test_frameworks"] = list(set(test_info["test_frameworks"]))

    # Find test directories
    for d in test_dirs:
        if (path / d).is_dir():
            test_info["test_directories"].append(d)

    # Coverage estimate
    if code_files:
        ratio = len(test_files) / len(code_files)
        if ratio >= 0.8:
            test_info["estimated_coverage"] = "high"
        elif ratio >= 0.4:
            test_info["estimated_coverage"] = "medium"
        elif ratio >= 0.1:
            test_info["estimated_coverage"] = "low"
        else:
            test_info["estimated_coverage"] = "minimal"

    return test_info


def generate_structure(path: Path, max_depth: int = 2) -> List[str]:
    """Generate a tree structure of the project."""
    structure = []

    def walk(current: Path, depth: int, prefix: str = ""):
        if depth > max_depth:
            return

        try:
            items = sorted(current.iterdir(), key=lambda x: (x.is_file(), x.name))
        except PermissionError:
            return

        dirs = [i for i in items if i.is_dir() and i.name not in SKIP_DIRS]
        files = [i for i in items if i.is_file()]

        for i, d in enumerate(dirs[:10]):
            is_last = (i == len(dirs) - 1) and not files
            connector = "└── " if is_last else "├── "
            structure.append(f"{prefix}{connector}{d.name}/")
            new_prefix = prefix + ("    " if is_last else "│   ")
            walk(d, depth + 1, new_prefix)

        important_files = [f for f in files if f.name in [
            'README.md', 'package.json', 'requirements.txt', 'Cargo.toml',
            'go.mod', 'Makefile', 'Dockerfile', 'docker-compose.yml',
            'main.py', 'index.ts', 'index.js', 'app.py', 'App.tsx',
            'pyproject.toml', '.env.example', 'setup.py'
        ]]

        for i, f in enumerate(important_files[:5]):
            is_last = i == len(important_files) - 1
            connector = "└── " if is_last else "├── "
            structure.append(f"{prefix}{connector}{f.name}")

    structure.append(f"{path.name}/")
    walk(path, 0)
    return structure


def identify_key_files(path: Path, all_files: List[Dict]) -> List[Dict]:
    """Identify likely important files."""
    key_files = []

    entry_points = [
        'main.py', 'app.py', 'index.ts', 'index.js', 'main.go', 'main.rs',
        'App.tsx', 'App.jsx', 'server.py', 'server.ts', 'server.js',
        'cli.py', 'manage.py', 'run.py'
    ]

    for f in all_files:
        fname = Path(f["path"]).name
        if fname in entry_points:
            key_files.append({"type": "entry_point", **f})

    config_files = [
        'package.json', 'requirements.txt', 'Cargo.toml', 'go.mod',
        'tsconfig.json', 'pyproject.toml', 'setup.py', '.env.example',
        'docker-compose.yml', 'Dockerfile'
    ]

    for f in all_files:
        fname = Path(f["path"]).name
        if fname in config_files:
            key_files.append({"type": "config", **f})

    for f in all_files[:10]:
        if 'test' not in f["path"].lower() and 'spec' not in f["path"].lower():
            if f not in key_files:
                key_files.append({"type": "core_logic", **f})

    return key_files[:15]


def calculate_complexity(all_files: List[Dict]) -> Dict:
    """Calculate complexity metrics."""
    code_files = [f for f in all_files if f.get("ext") in LANGUAGE_MAP]

    if not code_files:
        return {"total_lines": 0, "avg_file_size": 0}

    total_lines = sum(f.get("lines", 0) for f in code_files)
    avg_lines = total_lines / len(code_files) if code_files else 0

    small = len([f for f in code_files if f.get("lines", 0) < 100])
    medium = len([f for f in code_files if 100 <= f.get("lines", 0) < 300])
    large = len([f for f in code_files if f.get("lines", 0) >= 300])

    return {
        "total_code_files": len(code_files),
        "total_lines": total_lines,
        "avg_lines_per_file": round(avg_lines, 1),
        "largest_file_lines": code_files[0].get("lines", 0) if code_files else 0,
        "file_size_distribution": {
            "small_under_100": small,
            "medium_100_to_300": medium,
            "large_over_300": large
        }
    }


def get_basic_git_insights(path: Path) -> Dict[str, Any]:
    """Get basic git insights without deep analysis."""
    insights = {
        "is_git_repo": False,
        "total_commits": 0,
        "contributors": [],
        "most_changed_files": [],
        "recent_activity": "",
        "age": ""
    }

    git_dir = path / '.git'
    if not git_dir.exists():
        return insights

    insights["is_git_repo"] = True

    try:
        result = subprocess.run(
            ['git', 'rev-list', '--count', 'HEAD'],
            cwd=path, capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            insights["total_commits"] = int(result.stdout.strip())

        result = subprocess.run(
            ['git', 'shortlog', '-sn', '--no-merges', 'HEAD'],
            cwd=path, capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')[:5]
            insights["contributors"] = [
                line.strip().split('\t')[-1] for line in lines if line.strip()
            ]

        result = subprocess.run(
            ['git', 'log', '--format=%cr', '-1'],
            cwd=path, capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            insights["recent_activity"] = result.stdout.strip()

        result = subprocess.run(
            ['git', 'log', '--reverse', '--format=%cr', '-1'],
            cwd=path, capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            insights["age"] = f"Started {result.stdout.strip()}"

    except Exception:
        pass

    return insights


# =============================================================================
# Output Formatting
# =============================================================================

def print_report(results: Dict, verbose: bool = False):
    """Print a formatted report."""
    print("\n" + "=" * 70)
    print(f"PROJECT ANALYSIS: {results['project_name']}")
    print("=" * 70)

    print("\nOVERVIEW")
    print(f"  Total files: {results['files']['total']}")
    print(f"  Code files: {results['complexity'].get('total_code_files', 0)}")
    print(f"  Total lines: {results['complexity'].get('total_lines', 0)}")

    print("\nLANGUAGES")
    for lang, count in sorted(results['languages'].items(), key=lambda x: -x[1]):
        print(f"  {lang}: {count} files")

    if results['frameworks']:
        print("\nFRAMEWORKS")
        for fw in results['frameworks']:
            print(f"  • {fw}")

    # Design Patterns (new)
    patterns = results.get('ast_analysis', {}).get('design_patterns', [])
    if patterns:
        print("\nDESIGN PATTERNS DETECTED")
        for p in patterns[:5]:
            conf = int(p['confidence'] * 100)
            print(f"  • {p['name']} ({conf}% confidence)")
            for ev in p.get('evidence', [])[:2]:
                print(f"    └─ {ev[:60]}")

    # Git Narrative (new)
    git_narrative = results.get('git_narrative', {})
    if git_narrative and git_narrative.get('pivots'):
        print("\n📜 ARCHITECTURAL PIVOTS")
        for pivot in git_narrative['pivots'][:3]:
            print(f"  [{pivot['date']}] {pivot['description'][:60]}...")

    if git_narrative and git_narrative.get('story_worthy_commits'):
        print("\nSTORY-WORTHY COMMITS")
        for commit in git_narrative['story_worthy_commits'][:5]:
            score = int(commit['story_value'] * 100)
            print(f"  [{commit['date']}] {commit['message'][:50]}... (story value: {score}%)")

    # Classes and Functions (new)
    ast_analysis = results.get('ast_analysis', {})
    classes = ast_analysis.get('classes', [])
    if classes:
        print(f"\nCLASSES DETECTED: {len(classes)}")
        for cls in classes[:5]:
            bases = f" extends {', '.join(cls['bases'])}" if cls.get('bases') else ""
            print(f"  • {cls['name']}{bases}")

    print("\n📁 STRUCTURE")
    for line in results['structure'].get('tree', [])[:20]:
        print(f"  {line}")

    # Story hooks
    hooks = results.get('story_hooks', [])
    if hooks and verbose:
        print("\nSTORY HOOKS")
        for hook in hooks[:10]:
            print(f"  [{hook['type']}] {hook['message'][:50]}...")
            print(f"         └─ {hook['file']}:{hook['line']}")

    print("\nSUGGESTED CONTENT ANGLES")
    for i, angle in enumerate(results['content_angles'], 1):
        print(f"  {i}. {angle}")

    print("\n" + "=" * 70)


# =============================================================================
# Main Entry Point
# =============================================================================

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_codebase.py /path/to/project [options]")
        print("\nOptions:")
        print("  --json     Output as JSON")
        print("  --full     Include story hooks and API endpoint extraction")
        print("  --deep     Full AST analysis + git narrative (slower)")
        print("  --verbose  Show all details in report")
        print("\nEnhanced analysis with AST parsing, design pattern detection,")
        print("and semantic git history analysis for technical writing.")
        sys.exit(1)

    project_path = sys.argv[1]
    full_analysis = "--full" in sys.argv
    deep_analysis = "--deep" in sys.argv
    verbose = "--verbose" in sys.argv

    results = analyze_project(
        project_path,
        full_analysis=full_analysis,
        deep_analysis=deep_analysis
    )

    if "error" in results:
        print(f"Error: {results['error']}")
        sys.exit(1)

    if "--json" not in sys.argv:
        print_report(results, verbose=verbose)

    if "--json" in sys.argv:
        if "--verbose" not in sys.argv:
            print("\n--- JSON OUTPUT ---")
        print(json.dumps(results, indent=2, default=str))
