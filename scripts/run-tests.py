#!/usr/bin/env python3
"""
Cross-Platform Test Runner
Replaces run-tests.sh with Python for Windows/macOS/Linux compatibility
"""

import sys
import subprocess
import platform
from pathlib import Path

def run_command(command, cwd=None):
    """Run a command and return result"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, check=False, 
                              capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def main():
    project_root = Path(__file__).parent.parent
    is_windows = platform.system() == "Windows"
    
    # Determine Python executable
    if is_windows:
        python_exe = project_root / ".venv" / "Scripts" / "python.exe"
    else:
        python_exe = project_root / ".venv" / "bin" / "python"
    
    # Fallback to system python if venv doesn't exist
    if not python_exe.exists():
        python_exe = "python"
    
    print("🧪 Running Test Suite")
    print("====================")
    print("")
    
    test_files = []
    
    # Check for quick tests
    quick_test = project_root / "tests" / "quick_test.py"
    if quick_test.exists():
        test_files.append(("Quick Tests", str(quick_test)))
    
    # Check for main test suite
    test_suite = project_root / "tests" / "test_suite.py"
    if test_suite.exists():
        test_files.append(("Test Suite", str(test_suite)))
    
    # Run pytest if available
    pytest_tests = list((project_root / "tests").glob("test_*.py"))
    if pytest_tests:
        test_files.append(("Pytest Suite", "pytest tests/"))
    
    if not test_files:
        print("⚠️  No test files found")
        print("Expected: tests/quick_test.py or tests/test_suite.py")
        return
    
    all_passed = True
    
    for test_name, test_command in test_files:
        print(f"🔍 Running {test_name}...")
        
        if test_command.startswith("pytest"):
            success, stdout, stderr = run_command(f"{python_exe} -m {test_command}", 
                                                 cwd=project_root)
        else:
            success, stdout, stderr = run_command(f"{python_exe} {test_command}", 
                                                 cwd=project_root)
        
        if success:
            print(f"✅ {test_name}: PASSED")
            if stdout and "--verbose" in sys.argv:
                print(stdout)
        else:
            print(f"❌ {test_name}: FAILED")
            if stderr:
                print(f"Error: {stderr}")
            if stdout:
                print(f"Output: {stdout}")
            all_passed = False
        
        print("")
    
    # Run coverage check if available
    coverage_script = project_root / "scripts" / "check-test-coverage.py"
    if coverage_script.exists():
        print("📊 Checking test coverage...")
        success, stdout, stderr = run_command(f"{python_exe} {coverage_script}", 
                                             cwd=project_root)
        if success:
            print("✅ Coverage check: PASSED")
            if stdout and "--verbose" in sys.argv:
                print(stdout)
        else:
            print("⚠️  Coverage check: Issues found")
            if stderr:
                print(f"Error: {stderr}")
            if stdout:
                print(stdout)
    
    # Final result
    if all_passed:
        print("🎉 All tests passed!")
        sys.exit(0)
    else:
        print("💥 Some tests failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
