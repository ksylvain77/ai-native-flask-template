# AI-Native Project Template

A project template designed for AI-collaborative development with smart defaults, automated workflows, and comprehensive testing.

## Features

- 🤖 **AI-Optimized**: Structured for seamless AI collaboration
- 🚀 **Smart Defaults**: Only asks for project name - handles the rest
- 📁 **Project-Based Naming**: Uses your project name instead of generic `main.py`
- 🧪 **4-Phase Testing**: Backend → API → Contract → Frontend
- 🔄 **Automated Workflows**: Git branching, testing, and merging scripts
- 📦 **Complete Setup**: Virtual environment, dependencies, and structure

## Prerequisites

- Python 3.8+ installed on your system
- Git (for cloning and project workflows)
- Terminal/Command line access

## Quick Start

### Option 1: Clone and Use (Recommended)
```bash
# 1. Clone this template repository
git clone https://github.com/ksylvain77/ai-native-project-template.git

# 2. Create a new project from the template
cd ai-native-project-template
python3 init_project.py my-awesome-project

# 3. Switch to your new project and start developing
cd my-awesome-project
./manage.sh setup
./manage.sh start
```

### Option 2: Download and Use
```bash
# 1. Download the template
wget https://github.com/ksylvain77/ai-native-project-template/archive/main.zip
unzip main.zip
cd ai-native-project-template-main

# 2. Create your project
python3 init_project.py my-awesome-project

# 3. Start developing
cd my-awesome-project
./manage.sh setup
./manage.sh start
```

**That's it!** Your project will be running at `http://localhost:5000` with a complete development environment ready for AI collaboration.

## What Gets Generated

```
my-awesome-project/
├── my_awesome_project.py    # Main Flask application (named after your project)
├── modules/
│   ├── core.py             # Core business logic
│   └── utils.py            # Utility functions
├── tests/
│   ├── quick_test.py       # Fast development tests (2s)
│   └── test_suite.py       # Comprehensive testing (30s+)
├── scripts/
│   ├── create-branch.sh    # AI workflow: create feature branch
│   ├── merge-to-main.sh    # AI workflow: test + merge + cleanup
│   └── run-tests.sh        # Comprehensive test runner
├── .github/
│   └── copilot-instructions.md  # AI collaboration guide
├── requirements.txt        # Python dependencies
├── manage.sh              # Project management script
├── .gitignore             # Comprehensive Git ignore rules
└── README.md              # Project-specific documentation
```

## AI-Native Development Workflow

The generated projects follow an AI-collaborative workflow:

1. **AI creates feature branch**: `./scripts/create-branch.sh feature-name "Description"`
2. **AI implements feature** with immediate testing feedback
3. **User approves** the implementation
4. **AI merges automatically**: `./scripts/merge-to-main.sh "Final message"`

### Key Principles

- **Merge as You Go**: Main branch always working, immediate integration
- **Test-Driven**: 100% test pass rate required before merge
- **Documentation-Driven**: Auto-maintained docs with live system data

## Template Customization

The template uses placeholder replacement for full customization:

- `{{PROJECT_NAME}}` → Your project name
- `{{PROJECT_DESCRIPTION}}` → Your project description
- `{{MAIN_FILE}}` → `your_project_name.py`
- `{{SERVICE_NAME}}` → `your_project_name`

All generated files are fully functional with proper Flask setup, testing framework, and development scripts.

## Requirements

- Python 3.8+
- Git (for generated project workflows)

## Generated Project Features

Each generated project includes:

- ✅ **Working Flask application** with health endpoints
- ✅ **Complete test suite** with 4-phase methodology
- ✅ **Virtual environment setup** with dependencies
- ✅ **Git workflow automation** for AI collaboration
- ✅ **Proper .gitignore** for Python projects
- ✅ **AI collaboration guides** in `.github/copilot-instructions.md`

## Examples

```bash
# Create a blog API
python3 init_project.py blog-api
# Generates: blog_api.py as main file

# Create a data processor
python3 init_project.py data-processor
# Generates: data_processor.py as main file

# Create any project
python3 init_project.py my-project
# Generates: my_project.py as main file
```

The template automatically converts your project name into valid Python module names and file structures.

## Contributing

This template itself follows the AI-native methodology. To improve the template:

1. Create issues for template improvements
2. Test changes with multiple generated projects
3. Ensure 100% success rate for generated project workflows
4. Update documentation to reflect changes

**Philosophy**: The template should generate projects that work perfectly out-of-the-box with zero manual intervention required.
