# Cross-Platform Setup Guide

This AI-Native Project Template now supports **Windows**, **macOS**, and **Linux**!

## Quick Start (Any Platform)

### 1. Initial Setup

```bash
# Clone the repository
git clone <your-repo>
cd <your-project>

# Set up environment (cross-platform)
python manage.py setup
```

### 2. Start Development

```bash
# Start the server (cross-platform)
python manage.py start

# Check status
python manage.py status
```

### 3. Development Workflow

```bash
# Create feature branch (cross-platform)
python scripts/create-branch.py feature-name "Description"

# Run tests (cross-platform)
python scripts/run-tests.py

# Merge when ready (cross-platform)
python scripts/merge-to-main.py "Final commit message"
```

## Platform-Specific Instructions

### 🐧 Linux / 🍎 macOS

**Traditional Unix approach (still supported):**

```bash
# Make scripts executable (first time only)
chmod +x manage.sh scripts/*.sh

# Use shell scripts
./manage.sh setup
./manage.sh start
./scripts/create-branch.sh feature-name "Description"
./scripts/run-tests.sh
./scripts/merge-to-main.sh "Message"
```

**Modern Python approach (recommended):**

```bash
# Direct Python execution
python manage.py setup
python manage.py start
python scripts/create-branch.py feature-name "Description"
python scripts/run-tests.py
python scripts/merge-to-main.py "Message"
```

### 🪟 Windows

**Using Batch Files:**

```cmd
REM Setup and start
manage.bat setup
manage.bat start

REM Development workflow
scripts\create-branch.bat feature-name "Description"
scripts\run-tests.bat
scripts\merge-to-main.bat "Message"
```

**Using Python Directly:**

```cmd
REM Setup and start
python manage.py setup
python manage.py start

REM Development workflow
python scripts\create-branch.py feature-name "Description"
python scripts\run-tests.py
python scripts\merge-to-main.py "Message"
```

## Environment Requirements

### Python Virtual Environment

The system automatically detects your platform and uses the correct paths:

- **Linux/macOS**: `.venv/bin/python`
- **Windows**: `.venv\Scripts\python.exe`

### Required Dependencies

All platforms need these Python packages (automatically installed):

```
flask>=3.0.0
pytest>=7.0.0
requests>=2.31.0
psutil>=5.9.0  # Cross-platform process management
```

### Port Management

The system uses `psutil` for cross-platform port detection instead of platform-specific commands like `netstat`.

## Troubleshooting

### Windows-Specific Issues

1. **Python not found**: Make sure Python is in your PATH
2. **Permission errors**: Run Command Prompt as Administrator if needed
3. **Path issues**: Use forward slashes in Python code, backslashes in batch files

### macOS-Specific Issues

1. **Xcode tools**: You may need `xcode-select --install`
2. **Homebrew Python**: Prefer system Python or pyenv

### Linux-Specific Issues

1. **Missing python3-venv**: Install with `sudo apt install python3-venv`
2. **Permission issues**: Ensure scripts are executable with `chmod +x`

## Migration from Shell Scripts

If you have an existing project using the old shell scripts:

1. **Backup your work**: `git commit -am "backup before migration"`
2. **Update the template**: Copy new Python scripts
3. **Test the new system**: Run `python manage.py status`
4. **Update your workflow**: Use Python commands instead of shell commands
5. **Update documentation**: Replace shell commands in READMEs

## Advanced Features

### Background Processes

```bash
# Start server in background (Linux/macOS)
python manage.py start

# Check if running
python manage.py status

# View logs
python manage.py logs

# Stop cleanly
python manage.py stop
```

### Development Tools

```bash
# Clean up temporary files
python manage.py clean

# Check test coverage
python scripts/check-test-coverage.py

# Update roadmap
python scripts/update-roadmap.py
```

## IDE Integration

### VS Code

The template includes `.vscode/` settings that work across all platforms.

### PyCharm

Works out of the box with the Python virtual environment.

### Other IDEs

Point your IDE to use `.venv/bin/python` (Unix) or `.venv\Scripts\python.exe` (Windows).

## Continuous Integration

The Python scripts work seamlessly in CI environments:

```yaml
# GitHub Actions example
- name: Setup
  run: python manage.py setup

- name: Test
  run: python scripts/run-tests.py

- name: Deploy
  run: python manage.py start
```

## Benefits of Cross-Platform Support

✅ **Unified Workflow**: Same commands work everywhere  
✅ **Better Process Management**: `psutil` is more reliable than shell commands  
✅ **Path Handling**: Python handles paths correctly on all platforms  
✅ **Error Handling**: Better error messages and recovery  
✅ **IDE Integration**: Works with all major IDEs  
✅ **CI/CD Ready**: Consistent behavior in automated environments

## Legacy Support

The original shell scripts (`.sh`) are still included for backward compatibility, but the Python scripts (`.py`) are now the recommended approach for all platforms.
