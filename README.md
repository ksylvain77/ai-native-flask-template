# {{PROJECT_NAME}}

{{PROJECT_DESCRIPTION}}

## Quick Start

```bash
# Setup (one time)
./manage.sh setup

# Start the service
./manage.sh start

# Run tests
./scripts/run-tests.sh

# Development workflow
./scripts/create-branch.sh feature-name "Description"
# ... make changes ...
./scripts/merge-to-main.sh "Final commit message"
```

## AI-Native Development

This project uses an **AI-Native Development Workflow**:

- **Bootstrap Prompt**: `BOOTSTRAP_PROMPT.md` - Quick context for AI collaboration
- **Automation Scripts**: `scripts/` - Consistent Git workflow and testing
- **DRY Testing**: Dictionary-based test configuration
- **Auto-Documentation**: README updates with live system data

## Architecture

```
{{MAIN_FILE}}                 # Main application entry point
modules/                      # Core business logic
  ├── {{MODULE_1}}.py         # {{MODULE_1_DESC}}
  └── {{MODULE_2}}.py         # {{MODULE_2_DESC}}
templates/                    # UI templates (if web app)
static/                       # Static assets (if web app)
tests/
  ├── quick_test.py          # Fast development tests (2s)
  └── test_suite.py          # Comprehensive testing (30s+)
scripts/
  ├── create-branch.sh       # AI workflow: create feature branch
  ├── merge-to-main.sh       # AI workflow: test + merge + cleanup
  └── run-tests.sh           # Comprehensive test runner
```

## Requirements

- Python 3.8+
- Virtual environment (`.venv/`)
- {{ADDITIONAL_REQUIREMENTS}}

## Project Status

- **Status**: {{PROJECT_STATUS}}
- **Version**: {{PROJECT_VERSION}}
- **Last Updated**: {{LAST_UPDATED}}

## Contributing

This project follows the **"Merge as You Go"** philosophy for AI collaboration:

1. AI creates feature branches using `./scripts/create-branch.sh`
2. AI implements and tests features
3. User approves changes  
4. AI merges using `./scripts/merge-to-main.sh` (auto: test → commit → merge → cleanup)

**Key Principle**: Main branch always working, immediate integration, clean history.
