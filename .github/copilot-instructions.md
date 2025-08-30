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

# 2. AI implements feature following project patterns

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
  - Windows: `scripts
un-tests.bat quick`
- **Full Tests**:
  - Linux/macOS: `./scripts/run-tests.sh`
  - Windows: `scripts
un-tests.bat`
- **Testing Strategy**: Appropriate to project type ({{TECH_STACK}} + {{PROJECT_TYPE}})
- **Quality Standards**: Maintain test coverage appropriate for project complexity
- **Completion Criteria**: All tests pass before merge

### **Environment Requirements**

- **Technology Stack**: {{TECH_STACK}}
- **Environment Setup**:
  - Linux/macOS: `./manage.sh setup` or `python manage.py setup`
  - Windows: `manage.bat setup`
- **Project Start**:
  - Linux/macOS: `./manage.sh start` or `python manage.py start`
  - Windows: `manage.bat start`

## Core Philosophy

- **AI-Native**: Project structure optimized for AI collaboration
- **Automation-First**: Scripts handle repetitive tasks
- **Test-Driven**: Features only complete when fully tested
- **Documentation-Driven**: Clear context enables effective AI work
- **Merge as You Go**: Immediate integration, clean history

## Development Patterns

### Adding Features

1. **Core Logic**: Add functionality to appropriate modules
2. **Testing**: Create tests appropriate for {{PROJECT_TYPE}}
3. **Integration**: Connect components following {{TECH_STACK}} patterns
4. **Documentation**: Update relevant documentation

### Project Structure

```
{{PROJECT_STRUCTURE}}         # Generated based on project type and tech stack
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
- **Testing**: Complete testing appropriate to project type before feature completion
- **Documentation**: Auto-maintained, stays current with system state
- **Error Handling**: Structured for AI debugging and self-healing

**Success Criteria**: Feature complete when automated workflow passes with appropriate test coverage.
