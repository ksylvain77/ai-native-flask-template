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
  - Linux/macOS: `./scripts/run-tests.sh quick`
  - Windows: `scripts\run-tests.bat quick`
- **Full Tests**:
  - Linux/macOS: `./scripts/run-tests.sh`
  - Windows: `scripts\run-tests.bat`
- **4-Phase Testing**: Backend → API → Contract → Frontend using pytest
- **Industry Standard**: pytest + coverage.py for reliable testing
- **Smart Coverage**: 70% coverage target for business logic in `modules/`
- **Auto-Exclusion**: Test files, scripts, venv automatically excluded
- **Completion Criteria**: All pytest tests pass with coverage threshold met

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
2. **Test**: Add pytest tests to `tests/test_template.py` using standard format
3. **API**: Add endpoint to `{{MAIN_FILE}}`
4. **Frontend**: Update templates/static if needed

### Testing Approach (4-Phase Methodology with Pytest)

```python
# Backend test - pytest format
@pytest.mark.unit
def test_your_function():
    """Test description"""
    from modules.your_module import your_function
    result = your_function()
    assert 'field' in result

# API test - integration testing
@pytest.mark.integration
def test_api_endpoint(service_check):
    """Test API endpoint"""
    response = requests.get(f"{BASE_URL}/api/your/endpoint")
    assert response.status_code == 200
    assert 'expected_field' in response.json()
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
