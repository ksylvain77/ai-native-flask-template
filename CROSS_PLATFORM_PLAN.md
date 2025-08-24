# Cross-Platform Support Plan

## Current OS Dependencies (Linux/Unix Only)

### 1. Shell Scripts (\*.sh)

- **Issue**: Bash scripts don't work on Windows
- **Solution**: Create Python equivalents or batch/PowerShell alternatives

### 2. Python Virtual Environment Paths

- **Issue**: `.venv/bin/python` vs `.venv\Scripts\python.exe`
- **Solution**: Use `python -m venv` and platform detection

### 3. Process Management Commands

- **Issue**: `ps`, `kill`, `netstat` are Unix-only
- **Solution**: Use Python `psutil` library or platform-specific equivalents

### 4. File Permissions

- **Issue**: `chmod +x` doesn't exist on Windows
- **Solution**: Skip on Windows or use Python os.chmod()

### 5. Path Handling

- **Issue**: Hard-coded forward slashes
- **Solution**: Use `pathlib` or `os.path.join()`

## Implementation Strategy

### Phase 1: Core Management Script

- [ ] Convert `manage.sh` to `manage.py`
- [ ] Add platform detection
- [ ] Use cross-platform libraries (psutil, pathlib)

### Phase 2: Git Workflow Scripts

- [ ] Convert all `.sh` scripts to `.py`
- [ ] Maintain same interface/commands
- [ ] Add Windows batch file wrappers

### Phase 3: Documentation Updates

- [ ] Update copilot-instructions.md
- [ ] Add platform-specific setup instructions
- [ ] Update all path references

### Phase 4: Testing

- [ ] Test on Windows, macOS, Linux
- [ ] Add platform detection to test suite
- [ ] Document platform-specific gotchas

## Cross-Platform Libraries to Use

- **psutil**: Process management
- **pathlib**: Path handling
- **platform**: OS detection
- **subprocess**: Command execution
- **shutil**: File operations

## Backward Compatibility

- Keep existing `.sh` files for Linux users
- Add deprecation warnings
- Provide migration guide
