# Documentation Generation Instructions

Instructions for generating README files, API documentation, and technical docs from user projects.

---

## README Generation

### Analyze the Project First

Before generating a README, extract these elements from the codebase:

1. **Project identity** - Scan package.json, pyproject.toml, Cargo.toml, or equivalent for name, description, version
2. **Entry points** - Identify main files, CLI commands, exported functions
3. **Dependencies** - Note key dependencies that indicate the tech stack
4. **Configuration** - Find config files, environment variables, options objects
5. **Examples** - Look for /examples, /demo, or inline usage in tests

### Structure README in Priority Order

Generate sections following this hierarchy. Include Level 1-2 always; add others based on project complexity:

**Level 1 - Identity (always include):**
- Project name with one-line description stating what it does and why
- The problem it solves (2-3 sentences)
- Who should use it

**Level 2 - Usage (always include):**
- Installation command (npm install, pip install, etc.)
- Quick start showing minimal working example
- Basic usage patterns

**Level 3 - Details (include for non-trivial projects):**
- Key concepts the user needs to understand
- Architecture overview if system has multiple components
- Configuration options in table format

**Level 4 - Contribution (include if open source):**
- Development setup commands
- Link to CONTRIBUTING.md if exists
- Testing commands

**Level 5 - Reference (include as needed):**
- Advanced usage patterns
- Troubleshooting common issues
- Link to changelog

### Format Configuration as Tables

When documenting options, use this structure:

```markdown
| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `optionName` | type | `defaultValue` | What it controls |
```

### Generate Working Code Examples

For every code example:
- Extract actual function signatures from the source
- Use realistic input values, not "foo" or "test"
- Show expected output as comments
- Include import/require statements

### Avoid These Patterns

- Do not start with "This is a project that..." - state what it does directly
- Do not include badges unless the user requests them
- Do not document every option inline - link to detailed docs for extensive configs
- Do not assume the reader knows the problem context - explain it

---

## API Documentation Generation

### Extract Endpoint Information

For each API endpoint, gather:

1. **HTTP method and path** from route definitions
2. **Authentication requirements** from middleware/decorators
3. **Request schema** from validation, types, or body parsing
4. **Response schema** from return types or serializers
5. **Error codes** from error handlers or thrown exceptions

### Structure Each Endpoint As

```markdown
## [Action Description]

`[METHOD] [path]`

[One sentence describing what this endpoint does]

### Authentication

[Required/Optional, method (Bearer token, API key, etc.)]

### Request

**Headers:**
| Header | Required | Description |
|--------|----------|-------------|

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|

**Body:**
```json
{
  "field": "example_value"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|

### Response

**Success ([status code]):**
```json
{
  "response": "example"
}
```

**Errors:**
| Code | Description |
|------|-------------|

### Example

**Request:**
```bash
curl -X [METHOD] [url] \
  -H "Header: value" \
  -d '{"body": "data"}'
```

**Response:**
```json
{
  "example": "response"
}
```
```

### Generate Accurate Request/Response Examples

- Use realistic data matching field types (valid emails, UUIDs, timestamps)
- Include all required fields in request examples
- Show complete response objects, not fragments
- Use ISO 8601 format for timestamps: `2024-01-15T10:30:00Z`

---

## Architecture Documentation Generation

### Identify System Components

Scan the project structure for:

1. **Services/modules** - Separate directories with their own purpose
2. **External dependencies** - Database connections, API clients, message queues
3. **Entry points** - Servers, workers, CLI tools
4. **Data models** - Schemas, types, entities

### Generate Component Descriptions

For each major component, document:

```markdown
### [Component Name]

**Purpose:** [One sentence on what it does]

**Responsibilities:**
- [Key responsibility 1]
- [Key responsibility 2]

**Technologies:** [Key libraries/frameworks used]

**Interfaces:**
- Exposes: [APIs, ports, exports]
- Consumes: [Dependencies, services called]
```

### Create Data Flow Descriptions

For key operations, describe the flow:

```markdown
### [Operation Name] Flow

1. [First step - what initiates it]
2. [Processing step - what happens]
3. [Data step - what's read/written]
4. [Result step - what's returned]
```

### Generate ASCII Diagrams

Use box-drawing characters for architecture diagrams:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Component  │────▶│  Component  │────▶│  Component  │
└─────────────┘     └─────────────┘     └─────────────┘
```

Arrow conventions:
- `────▶` for synchronous calls
- `- - -▶` for async/eventual
- `│` and `─` for connections

---

## Changelog Generation

### Use Keep a Changelog Format

Structure changelog entries as:

```markdown
## [Version] - YYYY-MM-DD

### Added
- New features (link to PR/issue if available)

### Changed
- Modifications to existing functionality

### Fixed
- Bug fixes (link to issue if available)

### Removed
- Deprecated features that were removed

### Security
- Security patches (link to advisory if available)
```

### Categorize Changes Correctly

- **Added** - Entirely new functionality
- **Changed** - Modifications to existing behavior
- **Deprecated** - Features marked for future removal
- **Removed** - Features that no longer exist
- **Fixed** - Bug corrections
- **Security** - Vulnerability patches

### Write User-Focused Entries

- Describe what changed from the user's perspective
- Include issue/PR references when available: `(#123)`
- Be specific: "Fixed memory leak in connection pool" not "Fixed bug"

---

## Quality Verification

Before delivering documentation, verify:

**README:**
- [ ] One-line description conveys value proposition
- [ ] Problem statement is clear and specific
- [ ] Quick start example is complete and runnable
- [ ] All code examples include necessary imports
- [ ] Configuration options have types and defaults

**API Docs:**
- [ ] Every endpoint has method, path, and description
- [ ] Request/response examples use realistic data
- [ ] All error codes are documented
- [ ] Authentication requirements are stated

**Architecture:**
- [ ] High-level diagram shows major components
- [ ] Each component has clear responsibilities
- [ ] Data flows are traceable
- [ ] External dependencies are identified
