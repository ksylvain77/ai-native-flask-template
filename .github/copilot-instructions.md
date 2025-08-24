# {{PROJECT_NAME}} - AI Collaboration Instructions

## Project Overview

This is a **{{PROJECT_TYPE}}** project using AI-Native Development methodology.

**Repository**: {{REPO_URL}}

## 🚨 **CRITICAL: MANDATORY WORKFLOW**

### **Git Workflow (REQUIRED)**

```bash
# Cross-Platform Commands:

# Linux/macOS:
./scripts/create-branch.sh feature-name "Description of work"
# OR: python scripts/create-branch.py feature-name "Description of work"

# Windows:
scripts\create-branch.bat feature-name "Description of work"

# 2. AI implements feature following DRY patterns

# 3. AI shows user results and waits for approval

# Linux/macOS:
./scripts/merge-to-main.sh "Final commit message"
# OR: python scripts/merge-to-main.py "Final commit message"

# Windows:
scripts\merge-to-main.bat "Final commit message"
```

### **Testing Requirements (MANDATORY)**

- **Quick Tests**:
  - Linux/macOS: `.venv/bin/python tests/quick_test.py`
  - Windows: `.venv\Scripts\python.exe tests\quick_test.py`
- **Full Tests**:
  - Linux/macOS: `./scripts/run-tests.sh` or `python scripts/run-tests.py`
  - Windows: `scripts\run-tests.bat`
- **4-Phase Testing**: Backend → API → Contract → Frontend
- **Smart Coverage**: Only business logic functions require comprehensive testing
- **Auto-Exclusion**: Utility functions (format_response, sanitize_filename, etc.) automatically excluded
- **Completion Criteria**: 100% test pass rate for business logic required

### **Environment Requirements**

- **Python**:
  - Linux/macOS: Always use `.venv/bin/python` (never system python)
  - Windows: Use `.venv\Scripts\python.exe`
- **Server**: {{SERVER_URL}}
- **Port Check**:
  - Linux/macOS: `netstat -tuln | grep :{{PORT}}` (should be empty)
  - Windows: `netstat -an | findstr :{{PORT}}` (should be empty)
- **Setup**:
  - Linux/macOS: `./manage.sh setup` or `python manage.py setup`
  - Windows: `manage.bat setup`
- **Start**:
  - Linux/macOS: `./manage.sh start` or `python manage.py start`
  - Windows: `manage.bat start`

## Core Philosophy

- **AI-Native**: Project structure optimized for AI collaboration
- **Automation-First**: Scripts handle repetitive tasks
- **Test-Driven**: Features only complete when fully tested
- **Documentation-Driven**: Clear context enables effective AI work
- **Merge as You Go**: Immediate integration, clean history

## Development Patterns

### Adding Features (DRY Pattern)

1. **Backend**: Add function to appropriate module in `modules/`
2. **Test**: Add to `test_suite.py` using dictionary format
3. **API**: Add endpoint to `{{MAIN_FILE}}`
4. **Frontend**: Update templates/static if needed

### Testing Approach (4-Phase Methodology)

```python
# Backend test - DRY format
"test_name": {
    "description": "Test description",
    "module": "modules.your_module",
    "function": "your_function",
    "assertions": ["assert 'field' in result"]
}

# API test - simple dictionary
"api_name": {
    "endpoint": "/api/your/endpoint",
    "expected_fields": ["field1", "field2"]
}
```

## Project Structure

```
{{MAIN_FILE}}                 # Application entry point
modules/                      # Core business logic
templates/                    # UI templates
static/                       # Static assets
tests/                        # Testing framework
scripts/                      # Automation scripts
BOOTSTRAP_PROMPT.md           # Quick AI context
ROADMAP.md                    # Development roadmap and progress
PROJECT_GOALS.md              # Requirements and discovery results
```

## Working with AI

- **Context**: Bootstrap Prompt provides immediate project context
- **Roadmap**: ROADMAP.md tracks development phases and progress
- **Goals**: PROJECT_GOALS.md stores requirements and discovery results
- **Workflow**: Always use automation scripts, never manual Git
- **Testing**: Complete all 4 phases before feature completion
- **Documentation**: Auto-maintained, stays current with system state
- **Error Handling**: Structured for AI debugging and self-healing

**Success Criteria**: Feature complete when automated workflow passes with 100% test coverage.
