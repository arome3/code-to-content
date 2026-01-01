#!/usr/bin/env python3
"""
Context-Aware Readability Analyzer for Technical Writing (Enhanced)

Analyzes markdown/text files with audience-aware readability metrics.
Unlike generic readability tools, this adjusts expectations based on
the target audience and content type.

Features:
    - Audience-aware thresholds (beginner vs expert expects different density)
    - Domain-specific jargon detection with context
    - Improved syllable counting with exceptions dictionary
    - Actionable suggestions tailored to audience
    - Content structure analysis for technical docs

Usage:
    python analyze_readability.py /path/to/file.md
    python analyze_readability.py /path/to/file.md --audience beginner
    python analyze_readability.py /path/to/file.md --audience expert
    python analyze_readability.py /path/to/file.md --json
    python analyze_readability.py /path/to/file.md --validate

Output:
    - Context-aware readability scores
    - Audience-calibrated suggestions
    - Jargon analysis with definitions check
    - Code-to-prose ratio analysis
    - Structural quality assessment
"""

import os
import sys
import re
import json
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional
from collections import Counter
from dataclasses import dataclass, asdict
from enum import Enum


# =============================================================================
# Audience Profiles
# =============================================================================

class Audience(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    EXPERT = "expert"
    MIXED = "mixed"


@dataclass
class AudienceProfile:
    """Target audience configuration."""
    name: str
    max_flesch_kincaid_grade: float  # Maximum acceptable grade level
    target_flesch_ease: float        # Target readability score
    max_sentence_length: int         # Max words per sentence
    max_paragraph_length: int        # Max words per paragraph
    jargon_tolerance: float          # Acceptable jargon density %
    code_explanation_ratio: float    # Expected prose lines per code line
    requires_definitions: bool       # Should jargon be defined on first use
    allows_assumed_knowledge: List[str]  # Terms that don't need explanation


AUDIENCE_PROFILES = {
    Audience.BEGINNER: AudienceProfile(
        name="Beginner",
        max_flesch_kincaid_grade=8.0,
        target_flesch_ease=70.0,
        max_sentence_length=20,
        max_paragraph_length=100,
        jargon_tolerance=2.0,
        code_explanation_ratio=2.0,  # 2 lines of prose per code line
        requires_definitions=True,
        allows_assumed_knowledge=['computer', 'file', 'folder', 'click', 'type'],
    ),
    Audience.INTERMEDIATE: AudienceProfile(
        name="Intermediate",
        max_flesch_kincaid_grade=12.0,
        target_flesch_ease=55.0,
        max_sentence_length=25,
        max_paragraph_length=150,
        jargon_tolerance=4.0,
        code_explanation_ratio=1.0,
        requires_definitions=True,
        allows_assumed_knowledge=[
            'API', 'function', 'variable', 'loop', 'array', 'object',
            'class', 'method', 'parameter', 'return', 'import', 'export',
        ],
    ),
    Audience.EXPERT: AudienceProfile(
        name="Expert",
        max_flesch_kincaid_grade=16.0,
        target_flesch_ease=40.0,
        max_sentence_length=35,
        max_paragraph_length=200,
        jargon_tolerance=8.0,
        code_explanation_ratio=0.5,
        requires_definitions=False,
        allows_assumed_knowledge=[
            'API', 'REST', 'GraphQL', 'microservices', 'containerization',
            'CI/CD', 'dependency injection', 'singleton', 'factory pattern',
            'async', 'await', 'promise', 'callback', 'middleware',
            'ORM', 'schema', 'migration', 'index', 'query optimization',
        ],
    ),
    Audience.MIXED: AudienceProfile(
        name="Mixed",
        max_flesch_kincaid_grade=10.0,
        target_flesch_ease=60.0,
        max_sentence_length=22,
        max_paragraph_length=120,
        jargon_tolerance=3.0,
        code_explanation_ratio=1.5,
        requires_definitions=True,
        allows_assumed_knowledge=['computer', 'file', 'code'],
    ),
}


# =============================================================================
# Syllable Counting with Exceptions
# =============================================================================

# Common words with irregular syllable counts
SYLLABLE_EXCEPTIONS = {
    # Tech terms often mispronounced by algorithms
    'api': 3, 'apis': 3, 'ui': 2, 'ux': 2, 'cli': 3,
    'async': 2, 'await': 2, 'io': 2, 'ide': 3,
    'html': 4, 'css': 3, 'json': 2, 'xml': 3, 'yaml': 2,
    'sql': 3, 'nosql': 3, 'url': 3, 'uri': 3,
    'oauth': 2, 'saas': 1, 'paas': 1, 'iaas': 2,
    'devops': 2, 'devsecops': 3, 'ci': 2, 'cd': 2,
    'npm': 3, 'yarn': 1, 'pip': 1, 'gem': 1,
    'git': 1, 'github': 2, 'gitlab': 2, 'bitbucket': 3,
    'aws': 3, 'gcp': 3, 'azure': 2,
    'docker': 2, 'kubernetes': 4, 'k8s': 3,
    'react': 2, 'vue': 1, 'angular': 3, 'svelte': 1,
    'node': 1, 'deno': 2, 'bun': 1,
    'python': 2, 'javascript': 3, 'typescript': 3,
    'golang': 2, 'rust': 1, 'java': 2,
    # Common words with tricky counts
    'area': 3, 'idea': 3, 'create': 2, 'created': 3,
    'business': 2, 'every': 2, 'different': 3,
    'interesting': 4, 'basically': 4, 'actually': 4,
    'usually': 4, 'probably': 3, 'definitely': 4,
    'environment': 4, 'development': 4, 'application': 4,
    'implementation': 5, 'configuration': 5, 'authentication': 5,
    'authorization': 5, 'documentation': 5, 'initialization': 6,
    'queue': 1, 'queued': 1, 'queuing': 2,
    'cache': 1, 'cached': 1, 'caching': 2,
    'schema': 2, 'schemas': 2,
    'data': 2, 'database': 3, 'metadata': 4,
    'boolean': 3, 'integer': 3, 'string': 1,
    'array': 2, 'object': 2, 'function': 2,
}


def count_syllables(word: str) -> int:
    """
    Count syllables with improved accuracy using exceptions dictionary
    and better heuristics.
    """
    word = word.lower().strip()

    # Check exceptions first
    if word in SYLLABLE_EXCEPTIONS:
        return SYLLABLE_EXCEPTIONS[word]

    # Handle very short words
    if len(word) <= 2:
        return 1

    # Remove trailing punctuation
    word = re.sub(r'[^a-z]', '', word)
    if not word:
        return 1

    # Special case: -ed endings that don't add syllable
    if word.endswith('ed') and len(word) > 2:
        base = word[:-2]
        if base.endswith(('t', 'd')):
            pass  # -ted, -ded add syllable
        elif base.endswith('e'):
            word = base  # -eed -> count base
        else:
            word = base  # Most -ed don't add syllable

    # Count vowel groups with better handling
    vowels = 'aeiouy'
    count = 0
    prev_vowel = False

    for i, char in enumerate(word):
        is_vowel = char in vowels

        # Handle 'y' as vowel only in certain positions
        if char == 'y':
            is_vowel = i > 0 and word[i-1] not in vowels

        if is_vowel and not prev_vowel:
            count += 1

        prev_vowel = is_vowel

    # Adjustments for common patterns
    # Silent 'e' at end
    if word.endswith('e') and count > 1:
        count -= 1

    # -le at end with consonant before it
    if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
        count += 1

    # -es, -ed endings
    if word.endswith(('es', 'ed')) and len(word) > 2:
        if word[-3] in ('s', 'x', 'z', 'ch', 'sh'):
            count += 1

    # Ensure at least one syllable
    return max(1, count)


# =============================================================================
# Jargon Detection with Context
# =============================================================================

@dataclass
class JargonTerm:
    """A technical term with metadata."""
    term: str
    category: str
    complexity: int  # 1=basic, 2=intermediate, 3=advanced
    requires_definition: bool
    common_in: List[str]  # Domains where this is common


# Comprehensive jargon database with complexity levels
JARGON_DATABASE = {
    # Level 1: Basic tech terms most developers know
    'api': JargonTerm('API', 'web', 1, True, ['web', 'backend', 'mobile']),
    'json': JargonTerm('JSON', 'data', 1, True, ['web', 'backend']),
    'html': JargonTerm('HTML', 'web', 1, False, ['web', 'frontend']),
    'css': JargonTerm('CSS', 'web', 1, False, ['web', 'frontend']),
    'url': JargonTerm('URL', 'web', 1, False, ['web']),
    'http': JargonTerm('HTTP', 'web', 1, True, ['web', 'backend']),
    'https': JargonTerm('HTTPS', 'web', 1, True, ['web', 'security']),
    'database': JargonTerm('database', 'data', 1, False, ['backend', 'data']),
    'server': JargonTerm('server', 'infrastructure', 1, False, ['backend', 'devops']),
    'client': JargonTerm('client', 'architecture', 1, False, ['web', 'mobile']),

    # Level 2: Intermediate terms
    'rest': JargonTerm('REST', 'web', 2, True, ['web', 'backend']),
    'graphql': JargonTerm('GraphQL', 'web', 2, True, ['web', 'backend']),
    'sdk': JargonTerm('SDK', 'development', 2, True, ['mobile', 'integration']),
    'cli': JargonTerm('CLI', 'development', 2, True, ['devops', 'tools']),
    'orm': JargonTerm('ORM', 'data', 2, True, ['backend', 'data']),
    'crud': JargonTerm('CRUD', 'data', 2, True, ['backend', 'web']),
    'mvc': JargonTerm('MVC', 'architecture', 2, True, ['web', 'backend']),
    'sql': JargonTerm('SQL', 'data', 2, True, ['backend', 'data']),
    'async': JargonTerm('async', 'programming', 2, True, ['backend', 'frontend']),
    'callback': JargonTerm('callback', 'programming', 2, True, ['frontend', 'backend']),
    'promise': JargonTerm('promise', 'programming', 2, True, ['frontend', 'backend']),
    'middleware': JargonTerm('middleware', 'architecture', 2, True, ['backend', 'web']),
    'endpoint': JargonTerm('endpoint', 'web', 2, True, ['web', 'backend']),
    'payload': JargonTerm('payload', 'web', 2, True, ['web', 'backend']),
    'schema': JargonTerm('schema', 'data', 2, True, ['backend', 'data']),
    'migration': JargonTerm('migration', 'data', 2, True, ['backend', 'data']),
    'webhook': JargonTerm('webhook', 'web', 2, True, ['web', 'integration']),
    'docker': JargonTerm('Docker', 'devops', 2, True, ['devops', 'backend']),
    'container': JargonTerm('container', 'devops', 2, True, ['devops', 'backend']),

    # Level 3: Advanced terms
    'kubernetes': JargonTerm('Kubernetes', 'devops', 3, True, ['devops']),
    'microservices': JargonTerm('microservices', 'architecture', 3, True, ['backend', 'devops']),
    'ci/cd': JargonTerm('CI/CD', 'devops', 3, True, ['devops']),
    'idempotent': JargonTerm('idempotent', 'architecture', 3, True, ['backend', 'api']),
    'polymorphism': JargonTerm('polymorphism', 'programming', 3, True, ['oop']),
    'encapsulation': JargonTerm('encapsulation', 'programming', 3, True, ['oop']),
    'abstraction': JargonTerm('abstraction', 'programming', 3, True, ['oop', 'architecture']),
    'singleton': JargonTerm('singleton', 'patterns', 3, True, ['oop', 'architecture']),
    'factory': JargonTerm('factory', 'patterns', 3, True, ['oop', 'architecture']),
    'observer': JargonTerm('observer', 'patterns', 3, True, ['oop', 'architecture']),
    'decorator': JargonTerm('decorator', 'patterns', 3, True, ['oop', 'python']),
    'sharding': JargonTerm('sharding', 'data', 3, True, ['data', 'scaling']),
    'replication': JargonTerm('replication', 'data', 3, True, ['data', 'scaling']),
    'normalization': JargonTerm('normalization', 'data', 3, True, ['data']),
    'denormalization': JargonTerm('denormalization', 'data', 3, True, ['data']),
    'terraform': JargonTerm('Terraform', 'devops', 3, True, ['devops', 'iac']),
    'observability': JargonTerm('observability', 'devops', 3, True, ['devops', 'monitoring']),
    'telemetry': JargonTerm('telemetry', 'devops', 3, True, ['devops', 'monitoring']),
}

# Patterns for detecting jargon in text
JARGON_PATTERNS = [
    # Acronyms (2-5 uppercase letters)
    (r'\b[A-Z]{2,5}\b', 'acronym'),
    # CamelCase terms (likely class/function names)
    (r'\b[A-Z][a-z]+(?:[A-Z][a-z]+)+\b', 'camelcase'),
    # Terms with numbers (like k8s, s3, ec2)
    (r'\b[a-z]+\d+[a-z]*\b', 'alphanumeric'),
    # Hyphenated technical terms
    (r'\b\w+-(?:based|driven|first|native|ready|aware|safe)\b', 'compound'),
]


# =============================================================================
# Passive Voice Detection (Improved)
# =============================================================================

# More precise passive voice patterns
PASSIVE_PATTERNS = [
    # Standard passive: "is/was/were + past participle"
    r'\b(is|are|was|were|be|been|being)\s+(\w+ed)\b',
    # Perfect passive: "has/have/had been + past participle"
    r'\b(has|have|had)\s+been\s+(\w+ed)\b',
    # Modal passive: "will/would/should/could/might be + past participle"
    r'\b(will|would|should|could|might|may|must)\s+be\s+(\w+ed)\b',
    # Getting passive: "got/gets + past participle"
    r'\b(got|gets|getting)\s+(\w+ed)\b',
]

# Words that look passive but aren't
PASSIVE_EXCEPTIONS = {
    'used', 'based', 'called', 'named', 'required', 'needed',
    'interested', 'excited', 'concerned', 'supposed', 'expected',
    'tired', 'bored', 'worried', 'pleased', 'satisfied',
}


# =============================================================================
# Hedge Words and Filler Phrases
# =============================================================================

HEDGE_WORDS = {
    # Uncertainty markers
    'maybe': 'uncertainty',
    'perhaps': 'uncertainty',
    'possibly': 'uncertainty',
    'probably': 'uncertainty',
    'might': 'uncertainty',

    # Qualifiers that weaken statements
    'somewhat': 'qualifier',
    'slightly': 'qualifier',
    'fairly': 'qualifier',
    'rather': 'qualifier',
    'quite': 'qualifier',
    'relatively': 'qualifier',

    # Vague intensifiers
    'very': 'intensifier',
    'really': 'intensifier',
    'just': 'minimizer',
    'simply': 'minimizer',
    'basically': 'minimizer',
    'essentially': 'minimizer',
    'actually': 'filler',

    # Approximations
    'kind of': 'approximation',
    'sort of': 'approximation',
    'a bit': 'approximation',
    'a little': 'approximation',
}

FILLER_PHRASES = {
    'in order to': 'to',
    'due to the fact that': 'because',
    'it is important to note that': '[cut - start with the point]',
    'it should be noted that': '[cut - state directly]',
    'at the end of the day': '[cut - be specific]',
    'in terms of': 'regarding',
    'with respect to': 'about',
    'for the purpose of': 'to',
    'in the event that': 'if',
    'in this article': '[cut - they know where they are]',
    'in this tutorial': '[cut - they know where they are]',
    'in this guide': '[cut - they know where they are]',
    'as previously mentioned': '[cut or use specific reference]',
    'needless to say': '[cut - if needless, don\'t say it]',
    'it goes without saying': '[cut - just say it]',
    'as a matter of fact': '[cut - just state the fact]',
    'the fact that': '[rephrase to remove]',
    'in my opinion': '[cut - it\'s your writing]',
    'i think that': '[cut - be direct]',
    'i believe that': '[cut - be direct]',
}


# =============================================================================
# Main Analysis Class
# =============================================================================

class ReadabilityAnalyzer:
    """Context-aware readability analyzer."""

    def __init__(self, audience: Audience = Audience.INTERMEDIATE):
        self.audience = audience
        self.profile = AUDIENCE_PROFILES[audience]

    def analyze(self, content: str, file_name: str = "content") -> Dict[str, Any]:
        """Perform comprehensive readability analysis."""
        # Separate code from prose
        prose, code_blocks = self._separate_code_and_prose(content)

        # Calculate all metrics
        readability = self._calculate_readability(prose)
        sentences = self._analyze_sentences(prose)
        paragraphs = self._analyze_paragraphs(prose)
        passive = self._detect_passive_voice(prose)
        jargon = self._analyze_jargon(prose)
        hedge = self._find_hedge_words(prose)
        filler = self._find_filler_phrases(prose)
        code = self._analyze_code_blocks(code_blocks, prose)
        structure = self._analyze_structure(content)

        # Generate audience-aware assessment
        assessment = self._generate_assessment(
            readability, sentences, paragraphs, passive, jargon, code
        )

        # Generate suggestions
        suggestions = self._generate_suggestions(
            readability, sentences, paragraphs, passive, jargon, hedge, filler, code, structure
        )

        return {
            "file_name": file_name,
            "audience": self.audience.value,
            "audience_profile": asdict(self.profile),
            "total_characters": len(content),
            "prose_characters": len(prose),
            "readability_scores": readability,
            "sentence_analysis": sentences,
            "paragraph_analysis": paragraphs,
            "passive_voice": passive,
            "jargon_analysis": jargon,
            "hedge_words": hedge,
            "filler_phrases": filler,
            "code_analysis": code,
            "structure_analysis": structure,
            "assessment": assessment,
            "suggestions": suggestions,
            "validation_passed": self._validate_content(assessment),
        }

    def _separate_code_and_prose(self, content: str) -> Tuple[str, List[str]]:
        """Separate code blocks from prose content."""
        code_blocks = []

        # Extract fenced code blocks
        code_pattern = r'```[\s\S]*?```'
        matches = re.findall(code_pattern, content)
        code_blocks.extend(matches)

        # Remove code blocks from prose
        prose = re.sub(code_pattern, ' [CODE_BLOCK] ', content)

        # Extract inline code
        inline_pattern = r'`[^`]+`'
        prose = re.sub(inline_pattern, ' [INLINE_CODE] ', prose)

        return prose, code_blocks

    def _calculate_readability(self, prose: str) -> Dict[str, Any]:
        """Calculate readability scores with improved accuracy."""
        # Clean prose
        clean = re.sub(r'\[CODE_BLOCK\]|\[INLINE_CODE\]', '', prose)
        clean = re.sub(r'[#*_\[\]()]', '', clean)
        clean = re.sub(r'\s+', ' ', clean).strip()

        if not clean:
            return {"error": "No prose content to analyze"}

        # Extract words and sentences
        words = [w for w in re.findall(r'\b[a-zA-Z]+\b', clean) if len(w) > 1]
        sentences = [s.strip() for s in re.split(r'[.!?]+', clean) if s.strip()]

        if not words or not sentences:
            return {"error": "Insufficient content for analysis"}

        word_count = len(words)
        sentence_count = len(sentences)
        syllable_count = sum(count_syllables(w) for w in words)

        # Calculate scores
        avg_sentence_length = word_count / sentence_count
        avg_syllables_per_word = syllable_count / word_count

        # Flesch Reading Ease
        flesch_ease = 206.835 - (1.015 * avg_sentence_length) - (84.6 * avg_syllables_per_word)
        flesch_ease = max(0, min(100, flesch_ease))

        # Flesch-Kincaid Grade Level
        fk_grade = (0.39 * avg_sentence_length) + (11.8 * avg_syllables_per_word) - 15.59
        fk_grade = max(0, fk_grade)

        # Interpretation based on audience
        interpretation = self._interpret_readability(flesch_ease, fk_grade)

        return {
            "word_count": word_count,
            "sentence_count": sentence_count,
            "syllable_count": syllable_count,
            "avg_sentence_length": round(avg_sentence_length, 1),
            "avg_syllables_per_word": round(avg_syllables_per_word, 2),
            "flesch_reading_ease": round(flesch_ease, 1),
            "flesch_kincaid_grade": round(fk_grade, 1),
            "interpretation": interpretation,
            "meets_audience_target": fk_grade <= self.profile.max_flesch_kincaid_grade,
        }

    def _interpret_readability(self, ease: float, grade: float) -> Dict[str, str]:
        """Interpret readability relative to target audience."""
        # General interpretation
        if ease >= 80:
            general = "Very easy to read (conversational)"
        elif ease >= 70:
            general = "Easy to read (plain English)"
        elif ease >= 60:
            general = "Standard (general audience)"
        elif ease >= 50:
            general = "Fairly difficult (educated audience)"
        elif ease >= 30:
            general = "Difficult (technical/academic)"
        else:
            general = "Very difficult (specialized)"

        # Audience-specific interpretation
        target_grade = self.profile.max_flesch_kincaid_grade
        target_ease = self.profile.target_flesch_ease

        if grade <= target_grade and ease >= target_ease:
            audience_fit = f"Good fit for {self.profile.name} audience"
        elif grade <= target_grade + 2:
            audience_fit = f"Slightly advanced for {self.profile.name} audience"
        else:
            audience_fit = f"Too complex for {self.profile.name} audience - simplify"

        return {
            "general": general,
            "audience_fit": audience_fit,
            "grade_level": f"Grade {round(grade, 1)}",
        }

    def _analyze_sentences(self, prose: str) -> Dict[str, Any]:
        """Analyze sentence structure with audience awareness."""
        clean = re.sub(r'\[CODE_BLOCK\]|\[INLINE_CODE\]', '', prose)
        clean = re.sub(r'[#*_\[\]()]', '', clean)

        sentences = [s.strip() for s in re.split(r'[.!?]+', clean) if s.strip()]

        if not sentences:
            return {"error": "No sentences found"}

        lengths = [len(s.split()) for s in sentences]
        max_length = self.profile.max_sentence_length

        # Find problematic sentences
        long_sentences = []
        for s in sentences:
            word_count = len(s.split())
            if word_count > max_length:
                long_sentences.append({
                    "sentence": s[:100] + "..." if len(s) > 100 else s,
                    "word_count": word_count,
                    "over_limit_by": word_count - max_length,
                })

        # Calculate variation (good writing has varied sentence lengths)
        avg_length = sum(lengths) / len(lengths)
        variance = sum((l - avg_length) ** 2 for l in lengths) / len(lengths)
        std_dev = variance ** 0.5
        variation_score = min(1.0, std_dev / avg_length) if avg_length > 0 else 0

        return {
            "total_sentences": len(sentences),
            "avg_sentence_length": round(avg_length, 1),
            "max_allowed_for_audience": max_length,
            "shortest_sentence": min(lengths),
            "longest_sentence": max(lengths),
            "sentences_over_limit": len(long_sentences),
            "long_sentences": long_sentences[:5],
            "length_variation_score": round(variation_score, 2),
            "variation_assessment": "Good variety" if variation_score > 0.3 else "Could use more variety",
        }

    def _analyze_paragraphs(self, prose: str) -> Dict[str, Any]:
        """Analyze paragraph structure."""
        paragraphs = re.split(r'\n\s*\n', prose)
        paragraphs = [p.strip() for p in paragraphs
                      if p.strip() and not p.strip().startswith('#')]

        if not paragraphs:
            return {"error": "No paragraphs found"}

        lengths = [len(p.split()) for p in paragraphs]
        max_length = self.profile.max_paragraph_length

        long_paragraphs = []
        for p in paragraphs:
            word_count = len(p.split())
            if word_count > max_length:
                long_paragraphs.append({
                    "preview": p[:80] + "..." if len(p) > 80 else p,
                    "word_count": word_count,
                    "over_limit_by": word_count - max_length,
                })

        return {
            "total_paragraphs": len(paragraphs),
            "avg_paragraph_length": round(sum(lengths) / len(lengths), 1),
            "max_allowed_for_audience": max_length,
            "shortest_paragraph": min(lengths),
            "longest_paragraph": max(lengths),
            "paragraphs_over_limit": len(long_paragraphs),
            "long_paragraphs": long_paragraphs[:3],
        }

    def _detect_passive_voice(self, prose: str) -> Dict[str, Any]:
        """Detect passive voice with improved accuracy."""
        clean = re.sub(r'\[CODE_BLOCK\]|\[INLINE_CODE\]', '', prose)

        passive_instances = []

        for pattern in PASSIVE_PATTERNS:
            for match in re.finditer(pattern, clean, re.IGNORECASE):
                # Check if the past participle is an exception
                groups = match.groups()
                if len(groups) >= 2:
                    participle = groups[1].lower()
                    if participle in PASSIVE_EXCEPTIONS:
                        continue

                # Get context
                start = max(0, match.start() - 30)
                end = min(len(clean), match.end() + 30)
                context = clean[start:end].strip()

                passive_instances.append({
                    "match": match.group(),
                    "context": context,
                })

        # Deduplicate by context
        seen = set()
        unique_instances = []
        for inst in passive_instances:
            key = inst["context"][:50]
            if key not in seen:
                seen.add(key)
                unique_instances.append(inst)

        # Calculate percentage
        sentences = [s.strip() for s in re.split(r'[.!?]+', clean) if s.strip()]
        passive_sentences = 0

        for sentence in sentences:
            for pattern in PASSIVE_PATTERNS:
                if re.search(pattern, sentence, re.IGNORECASE):
                    # Check exceptions
                    match = re.search(pattern, sentence, re.IGNORECASE)
                    if match and len(match.groups()) >= 2:
                        if match.groups()[1].lower() not in PASSIVE_EXCEPTIONS:
                            passive_sentences += 1
                            break

        passive_percentage = (passive_sentences / len(sentences) * 100) if sentences else 0

        # Assessment relative to audience
        # Technical writing often uses passive appropriately
        if self.audience == Audience.EXPERT:
            threshold = 25
        else:
            threshold = 15

        assessment = "High" if passive_percentage > threshold else \
                     "Medium" if passive_percentage > threshold / 2 else "Low"

        return {
            "passive_instances_found": len(unique_instances),
            "passive_percentage": round(passive_percentage, 1),
            "examples": unique_instances[:5],
            "assessment": assessment,
            "threshold_for_audience": threshold,
            "within_threshold": passive_percentage <= threshold,
        }

    def _analyze_jargon(self, prose: str) -> Dict[str, Any]:
        """Analyze jargon with context awareness."""
        clean = re.sub(r'\[CODE_BLOCK\]|\[INLINE_CODE\]', '', prose)
        words = re.findall(r'\b[a-zA-Z]+\b', clean.lower())

        jargon_found = []
        jargon_counts = Counter()
        undefined_jargon = []

        # Check against jargon database
        for word in words:
            if word in JARGON_DATABASE:
                jargon = JARGON_DATABASE[word]
                jargon_counts[jargon.term] += 1

                # Check if term is allowed for this audience
                is_allowed = word in [w.lower() for w in self.profile.allows_assumed_knowledge]

                if not is_allowed and self.profile.requires_definitions:
                    # Check if it's defined in the text (look for "X is" or "X, which" patterns)
                    definition_patterns = [
                        rf'\b{word}\b[,\s]+(?:is|are|refers? to|means?)',
                        rf'\b{word}\b[,\s]+(?:which|that)\s+(?:is|are)',
                        rf'(?:called|known as|termed)\s+\b{word}\b',
                    ]
                    is_defined = any(re.search(p, clean, re.IGNORECASE) for p in definition_patterns)

                    if not is_defined and jargon.term not in [j['term'] for j in undefined_jargon]:
                        undefined_jargon.append({
                            "term": jargon.term,
                            "category": jargon.category,
                            "complexity": jargon.complexity,
                            "suggestion": f"Define '{jargon.term}' on first use",
                        })

        # Calculate jargon density
        jargon_instances = sum(jargon_counts.values())
        jargon_density = (jargon_instances / len(words) * 100) if words else 0

        # Assessment relative to audience tolerance
        tolerance = self.profile.jargon_tolerance

        if jargon_density > tolerance * 1.5:
            assessment = "High"
        elif jargon_density > tolerance:
            assessment = "Medium"
        else:
            assessment = "Low"

        return {
            "total_jargon_instances": jargon_instances,
            "unique_jargon_terms": len(jargon_counts),
            "jargon_density_percentage": round(jargon_density, 2),
            "tolerance_for_audience": tolerance,
            "within_tolerance": jargon_density <= tolerance,
            "most_used_jargon": [{"term": t, "count": c}
                                 for t, c in jargon_counts.most_common(10)],
            "undefined_jargon": undefined_jargon[:10],
            "assessment": assessment,
        }

    def _find_hedge_words(self, prose: str) -> Dict[str, Any]:
        """Find hedge words that weaken writing."""
        clean = re.sub(r'\[CODE_BLOCK\]|\[INLINE_CODE\]', '', prose)
        clean_lower = clean.lower()

        found = Counter()
        by_category = Counter()

        for word, category in HEDGE_WORDS.items():
            # Handle multi-word phrases
            if ' ' in word:
                count = len(re.findall(rf'\b{re.escape(word)}\b', clean_lower))
            else:
                count = len(re.findall(rf'\b{word}\b', clean_lower))

            if count > 0:
                found[word] = count
                by_category[category] += count

        total = sum(found.values())
        words = len(re.findall(r'\b[a-zA-Z]+\b', clean))
        density = (total / words * 100) if words else 0

        # Assessment
        if density > 3:
            assessment = "High - writing sounds uncertain"
        elif density > 1.5:
            assessment = "Medium - some hedging present"
        else:
            assessment = "Low - direct writing"

        return {
            "total_hedge_words": total,
            "hedge_density_percentage": round(density, 2),
            "by_category": dict(by_category),
            "most_common": [{"word": w, "count": c} for w, c in found.most_common(5)],
            "assessment": assessment,
        }

    def _find_filler_phrases(self, prose: str) -> Dict[str, Any]:
        """Find filler phrases that could be cut."""
        clean = re.sub(r'\[CODE_BLOCK\]|\[INLINE_CODE\]', '', prose)
        clean_lower = clean.lower()

        found = []

        for phrase, replacement in FILLER_PHRASES.items():
            matches = list(re.finditer(rf'\b{re.escape(phrase)}\b', clean_lower))
            for match in matches:
                found.append({
                    "phrase": phrase,
                    "replacement": replacement,
                    "position": match.start(),
                })

        # Estimate words that could be saved
        words_saveable = sum(len(f["phrase"].split()) - 1 for f in found)

        return {
            "total_filler_phrases": len(found),
            "words_saveable": words_saveable,
            "phrases_found": found[:10],
        }

    def _analyze_code_blocks(self, code_blocks: List[str], prose: str) -> Dict[str, Any]:
        """Analyze code-to-prose ratio."""
        if not code_blocks:
            return {
                "code_blocks": 0,
                "note": "No code blocks found",
                "ratio_assessment": "N/A - no code",
            }

        total_code_lines = sum(block.count('\n') for block in code_blocks)
        prose_lines = len([l for l in prose.split('\n') if l.strip() and not l.strip().startswith('#')])

        # Calculate ratio
        if total_code_lines > 0:
            ratio = prose_lines / total_code_lines
        else:
            ratio = float('inf')

        # Compare to audience expectation
        expected_ratio = self.profile.code_explanation_ratio

        if ratio >= expected_ratio:
            ratio_assessment = f"Good - {ratio:.1f} prose lines per code line (target: {expected_ratio})"
        elif ratio >= expected_ratio * 0.5:
            ratio_assessment = f"Low - {ratio:.1f} prose lines per code line (target: {expected_ratio})"
        else:
            ratio_assessment = f"Very low - {ratio:.1f} prose lines per code line (target: {expected_ratio})"

        # Detect languages
        languages = Counter()
        for block in code_blocks:
            first_line = block.split('\n')[0]
            lang_match = re.match(r'```(\w+)', first_line)
            if lang_match:
                languages[lang_match.group(1)] += 1

        return {
            "code_blocks": len(code_blocks),
            "total_code_lines": total_code_lines,
            "prose_lines": prose_lines,
            "prose_to_code_ratio": round(ratio, 2) if ratio != float('inf') else "N/A",
            "expected_ratio_for_audience": expected_ratio,
            "ratio_assessment": ratio_assessment,
            "languages_used": dict(languages),
        }

    def _analyze_structure(self, content: str) -> Dict[str, Any]:
        """Analyze document structure."""
        # Count headings
        h1 = len(re.findall(r'^# [^#]', content, re.MULTILINE))
        h2 = len(re.findall(r'^## [^#]', content, re.MULTILINE))
        h3 = len(re.findall(r'^### [^#]', content, re.MULTILINE))
        h4 = len(re.findall(r'^#### ', content, re.MULTILINE))

        # Count lists
        bullet_lists = len(re.findall(r'^[\s]*[-*] ', content, re.MULTILINE))
        numbered_lists = len(re.findall(r'^[\s]*\d+\. ', content, re.MULTILINE))

        # Count links and images
        links = len(re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content))
        images = len(re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content))

        # Calculate scannability score
        word_count = len(re.findall(r'\b\w+\b', content))
        structural_elements = h1 + h2 + h3 + h4 + bullet_lists + numbered_lists

        if word_count > 0:
            scannability = min(1.0, structural_elements / (word_count / 100))
        else:
            scannability = 0

        return {
            "headings": {
                "h1": h1,
                "h2": h2,
                "h3": h3,
                "h4": h4,
                "total": h1 + h2 + h3 + h4,
            },
            "lists": {
                "bullet_items": bullet_lists,
                "numbered_items": numbered_lists,
                "total": bullet_lists + numbered_lists,
            },
            "links": links,
            "images": images,
            "scannability_score": round(scannability, 2),
            "scannability_assessment": "Good" if scannability > 0.3 else "Could improve",
        }

    def _generate_assessment(self, readability: Dict, sentences: Dict,
                            paragraphs: Dict, passive: Dict, jargon: Dict,
                            code: Dict) -> Dict[str, Any]:
        """Generate overall assessment for the target audience."""
        issues = []
        strengths = []

        # Check readability
        if readability.get("meets_audience_target"):
            strengths.append("Readability matches audience level")
        else:
            issues.append(f"Content may be too complex for {self.profile.name} audience")

        # Check sentences
        if sentences.get("sentences_over_limit", 0) == 0:
            strengths.append("Sentence lengths are appropriate")
        else:
            issues.append(f"{sentences['sentences_over_limit']} sentences exceed recommended length")

        # Check paragraphs
        if paragraphs.get("paragraphs_over_limit", 0) == 0:
            strengths.append("Paragraph lengths are appropriate")
        else:
            issues.append(f"{paragraphs['paragraphs_over_limit']} paragraphs are too long")

        # Check passive voice
        if passive.get("within_threshold"):
            strengths.append("Active voice usage is good")
        else:
            issues.append("Consider reducing passive voice")

        # Check jargon
        if jargon.get("within_tolerance"):
            strengths.append("Jargon level is appropriate for audience")
        else:
            issues.append("Jargon density may be too high for audience")

        if jargon.get("undefined_jargon"):
            issues.append(f"{len(jargon['undefined_jargon'])} terms may need definitions")

        # Check code ratio
        if "ratio_assessment" in code and "Good" in code.get("ratio_assessment", ""):
            strengths.append("Good balance of code and explanation")
        elif code.get("code_blocks", 0) > 0:
            issues.append("May need more explanation around code blocks")

        # Overall score
        total_checks = 6
        passed = len(strengths)
        score = (passed / total_checks) * 100

        if score >= 80:
            overall = "Excellent"
        elif score >= 60:
            overall = "Good"
        elif score >= 40:
            overall = "Needs improvement"
        else:
            overall = "Significant revision needed"

        return {
            "overall": overall,
            "score": round(score, 1),
            "checks_passed": passed,
            "total_checks": total_checks,
            "strengths": strengths,
            "issues": issues,
        }

    def _generate_suggestions(self, readability: Dict, sentences: Dict,
                             paragraphs: Dict, passive: Dict, jargon: Dict,
                             hedge: Dict, filler: Dict, code: Dict,
                             structure: Dict) -> List[Dict]:
        """Generate actionable suggestions."""
        suggestions = []

        # Readability suggestions
        if not readability.get("meets_audience_target"):
            suggestions.append({
                "category": "Readability",
                "priority": "high",
                "issue": f"Grade level {readability.get('flesch_kincaid_grade')} exceeds target {self.profile.max_flesch_kincaid_grade}",
                "suggestion": "Use shorter sentences and simpler words. Break complex ideas into steps.",
            })

        # Sentence suggestions
        if sentences.get("sentences_over_limit", 0) > 0:
            suggestions.append({
                "category": "Sentence Length",
                "priority": "medium",
                "issue": f"{sentences['sentences_over_limit']} sentences exceed {self.profile.max_sentence_length} words",
                "suggestion": "Break long sentences at natural pause points. One idea per sentence.",
            })

        if sentences.get("variation_score", 0) < 0.3:
            suggestions.append({
                "category": "Sentence Variety",
                "priority": "low",
                "issue": "Sentences have similar lengths",
                "suggestion": "Mix short punchy sentences with longer explanatory ones.",
            })

        # Paragraph suggestions
        if paragraphs.get("paragraphs_over_limit", 0) > 0:
            suggestions.append({
                "category": "Paragraph Length",
                "priority": "medium",
                "issue": f"{paragraphs['paragraphs_over_limit']} paragraphs exceed {self.profile.max_paragraph_length} words",
                "suggestion": "Break paragraphs at topic shifts. One main point per paragraph.",
            })

        # Passive voice suggestions
        if not passive.get("within_threshold"):
            suggestions.append({
                "category": "Active Voice",
                "priority": "medium",
                "issue": f"{passive.get('passive_percentage')}% passive voice (target: <{passive.get('threshold_for_audience')}%)",
                "suggestion": "Rewrite passive sentences. 'X is done by Y' → 'Y does X'",
            })

        # Jargon suggestions
        if not jargon.get("within_tolerance"):
            suggestions.append({
                "category": "Jargon",
                "priority": "high",
                "issue": f"Jargon density {jargon.get('jargon_density_percentage')}% exceeds tolerance {self.profile.jargon_tolerance}%",
                "suggestion": "Define technical terms on first use or use simpler alternatives.",
            })

        undefined = jargon.get("undefined_jargon", [])
        if undefined and self.profile.requires_definitions:
            terms = [u["term"] for u in undefined[:3]]
            suggestions.append({
                "category": "Definitions",
                "priority": "medium",
                "issue": f"Terms may need definitions: {', '.join(terms)}",
                "suggestion": "Add brief definitions on first use: 'X (a type of Y that does Z)'",
            })

        # Hedge words suggestions
        if hedge.get("hedge_density_percentage", 0) > 2:
            suggestions.append({
                "category": "Confidence",
                "priority": "low",
                "issue": "Writing contains many hedge words (maybe, perhaps, somewhat)",
                "suggestion": "Be more direct. State things confidently or omit uncertain claims.",
            })

        # Filler phrase suggestions
        if filler.get("total_filler_phrases", 0) > 2:
            suggestions.append({
                "category": "Conciseness",
                "priority": "low",
                "issue": f"{filler['total_filler_phrases']} filler phrases found",
                "suggestion": "Replace wordy phrases: 'in order to' → 'to', 'due to the fact that' → 'because'",
            })

        # Structure suggestions
        total_headings = structure.get("headings", {}).get("total", 0)
        word_count = readability.get("word_count", 0)

        if word_count > 500 and total_headings < 3:
            suggestions.append({
                "category": "Structure",
                "priority": "medium",
                "issue": "Few headings for content length",
                "suggestion": "Add subheadings every 200-300 words for scannability.",
            })

        if word_count > 300 and structure.get("lists", {}).get("total", 0) == 0:
            suggestions.append({
                "category": "Formatting",
                "priority": "low",
                "issue": "No lists found in long content",
                "suggestion": "Use bullet points for sequences, features, or key points.",
            })

        # Code explanation suggestions
        if code.get("code_blocks", 0) > 0 and "Very low" in code.get("ratio_assessment", ""):
            suggestions.append({
                "category": "Code Explanation",
                "priority": "high",
                "issue": "Insufficient explanation around code blocks",
                "suggestion": f"Add {self.profile.code_explanation_ratio:.0f} lines of explanation per line of code for {self.profile.name} audience.",
            })

        # Sort by priority
        priority_order = {"high": 0, "medium": 1, "low": 2}
        suggestions.sort(key=lambda x: priority_order.get(x["priority"], 3))

        return suggestions

    def _validate_content(self, assessment: Dict) -> bool:
        """Check if content passes validation for the target audience."""
        return assessment.get("score", 0) >= 60


# =============================================================================
# CLI Interface
# =============================================================================

def print_report(results: Dict, show_suggestions: bool = True):
    """Print a formatted report."""
    print("\n" + "=" * 70)
    print(f"READABILITY ANALYSIS: {results['file_name']}")
    print(f"Target Audience: {results['audience'].upper()}")
    print("=" * 70)

    # Assessment Summary
    assessment = results.get("assessment", {})
    print(f"\nOVERALL: {assessment.get('overall', 'N/A')} ({assessment.get('score', 0)}%)")

    if assessment.get("strengths"):
        print("\nStrengths:")
        for s in assessment["strengths"]:
            print(f"   • {s}")

    if assessment.get("issues"):
        print("\nIssues:")
        for i in assessment["issues"]:
            print(f"   • {i}")

    # Readability scores
    scores = results.get("readability_scores", {})
    if "error" not in scores:
        print("\n📖 READABILITY")
        print(f"   Flesch Reading Ease: {scores.get('flesch_reading_ease', 'N/A')}/100")
        print(f"   Flesch-Kincaid Grade: {scores.get('flesch_kincaid_grade', 'N/A')}")
        interp = scores.get("interpretation", {})
        print(f"   {interp.get('audience_fit', '')}")

    # Jargon analysis
    jargon = results.get("jargon_analysis", {})
    print(f"\n📚 JARGON: {jargon.get('jargon_density_percentage', 0)}% density ({jargon.get('assessment', 'N/A')})")
    if jargon.get("undefined_jargon"):
        print("   Terms needing definition:")
        for term in jargon["undefined_jargon"][:3]:
            print(f"      • {term['term']}")

    # Passive voice
    passive = results.get("passive_voice", {})
    print(f"\nPASSIVE VOICE: {passive.get('passive_percentage', 0)}% ({passive.get('assessment', 'N/A')})")

    # Code analysis
    code = results.get("code_analysis", {})
    if code.get("code_blocks", 0) > 0:
        print(f"\nCODE: {code['code_blocks']} blocks")
        print(f"   {code.get('ratio_assessment', '')}")

    # Suggestions
    if show_suggestions and results.get("suggestions"):
        print("\nSUGGESTIONS (by priority):")
        for i, sug in enumerate(results["suggestions"][:7], 1):
            priority = sug.get("priority", "").upper()
            print(f"\n   {i}. [{priority}] {sug['category']}")
            print(f"      Issue: {sug['issue']}")
            print(f"      Fix: {sug['suggestion']}")

    # Validation result
    print("\n" + "-" * 70)
    if results.get("validation_passed"):
        print(f"✅ Content PASSES validation for {results['audience']} audience")
    else:
        print(f"❌ Content NEEDS REVISION for {results['audience']} audience")

    print("=" * 70 + "\n")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python analyze_readability.py /path/to/file.md [options]")
        print("\nOptions:")
        print("  --audience LEVEL   Set target audience (beginner/intermediate/expert/mixed)")
        print("  --json             Output as JSON")
        print("  --validate         Only output pass/fail status")
        print("  --no-suggestions   Hide improvement suggestions")
        print("\nContext-aware readability analysis for technical writing.")
        print("Adjusts expectations based on target audience.")
        sys.exit(1)

    file_path = sys.argv[1]

    # Parse audience
    audience = Audience.INTERMEDIATE
    if "--audience" in sys.argv:
        idx = sys.argv.index("--audience")
        if idx + 1 < len(sys.argv):
            audience_str = sys.argv[idx + 1].lower()
            try:
                audience = Audience(audience_str)
            except ValueError:
                print(f"Invalid audience: {audience_str}")
                print("Valid options: beginner, intermediate, expert, mixed")
                sys.exit(1)

    # Read file
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    try:
        content = path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Analyze
    analyzer = ReadabilityAnalyzer(audience)
    results = analyzer.analyze(content, path.name)

    # Output
    if "--json" in sys.argv:
        print(json.dumps(results, indent=2, default=str))
    elif "--validate" in sys.argv:
        if results.get("validation_passed"):
            print(f"PASS: Content suitable for {audience.value} audience")
            sys.exit(0)
        else:
            print(f"FAIL: Content needs revision for {audience.value} audience")
            sys.exit(1)
    else:
        show_suggestions = "--no-suggestions" not in sys.argv
        print_report(results, show_suggestions=show_suggestions)


if __name__ == "__main__":
    main()
