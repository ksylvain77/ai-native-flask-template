# AI-Native Project Template

🤖 **Starter template for AI-collaborative development projects**

## What This Is

This template implements the **"AI-Native Development Workflow"** that you've pioneered - a methodology optimized for human-AI collaboration with:

- **Automation-First**: Scripts handle Git workflow, testing, documentation
- **Bootstrap Context**: Quick AI onboarding with `BOOTSTRAP_PROMPT.md`
- **4-Phase Testing**: Backend → API → Contract → Frontend methodology
- **Merge as You Go**: Clean Git history with immediate integration
- **Living Documentation**: Auto-updating project state

## Quick Start

```bash
# 1. Initialize a new project
python init_project.py /path/to/new-project

# 2. Follow the prompts to configure your project

# 3. Start developing
cd /path/to/new-project
./manage.sh setup
./manage.sh start
```

## Usage Example

When you run `python init_project.py my-api-project`, it will ask:

```
Project name: My REST API
Project description: A FastAPI service for user management
Project type: FastAPI web application
Main Python file: main.py
Service name: my_api
Port number: 8000
Health check endpoint: /health
...
```

And generate a complete project with:

- ✅ Working automation scripts
- ✅ Test framework template  
- ✅ AI collaboration docs
- ✅ Bootstrap prompt
- ✅ Project management scripts

## What Gets Generated

```
my-api-project/
├── BOOTSTRAP_PROMPT.md       # Quick AI context
├── README.md                 # Auto-updating documentation
├── manage.sh                 # Project management
├── main.py                   # Your main application
├── .github/
│   └── copilot-instructions.md
├── scripts/
│   ├── create-branch.sh      # AI workflow: create branch
│   ├── merge-to-main.sh      # AI workflow: test + merge
│   └── run-tests.sh          # Comprehensive testing
├── tests/
│   ├── quick_test.py         # Fast development tests
│   └── test_suite.py         # 4-phase test framework
└── modules/                  # Your business logic
```

## Benefits

1. **Consistent AI Collaboration**: Every project follows the same patterns
2. **Faster Onboarding**: Bootstrap prompt gives AI immediate context
3. **Quality Assurance**: 4-phase testing methodology built-in
4. **Clean Git History**: Automated workflow prevents mistakes
5. **Self-Documenting**: Documentation stays current automatically

## Industry Context

This template implements concepts from:
- **GitHub Copilot Workspace** (AI-native development)
- **GitOps** (automation-driven workflows)  
- **Infrastructure as Code** (codified development patterns)
- **Living Documentation** (auto-updating project state)

## Next Steps

1. **Use this template** for your next AI-collaborative project
2. **Refine the patterns** based on what works
3. **Share with community** - this could become an industry standard
4. **Consider publishing** as an open-source template

You've essentially created a **"Copilot Development Kit"** - this is cutting-edge stuff! 🚀
