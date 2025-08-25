#!/bin/bash
# Template Self-Validation Framework
# Simple mechanics testing for AI-native Flask template

set -e

echo "🔍 AI-Native Template Validation"
echo "================================="

VALIDATION_ERRORS=0
VALIDATION_WARNINGS=0

# Helper functions
log_pass() { echo "✅ $1"; }
log_fail() { echo "❌ $1"; ((VALIDATION_ERRORS++)); }
log_warn() { echo "⚠️  $1"; ((VALIDATION_WARNINGS++)); }
log_info() { echo "ℹ️  $1"; }

# Test 1: Bash Script Syntax
echo ""
log_info "Testing bash script syntax..."
for script in scripts/*.sh; do
    if [ -f "$script" ]; then
        if bash -n "$script" 2>/dev/null; then
            log_pass "$(basename "$script") syntax valid"
        else
            log_fail "$(basename "$script") has syntax errors"
        fi
    fi
done

# Test 2: Python Script Syntax  
echo ""
log_info "Testing Python script syntax..."
for script in scripts/*.py init_project.py manage.py; do
    if [ -f "$script" ]; then
        if python3 -m py_compile "$script" 2>/dev/null; then
            log_pass "$(basename "$script") syntax valid"
        else
            log_fail "$(basename "$script") has syntax errors"
        fi
    fi
done

# Test 3: Required File Structure
echo ""
log_info "Validating template structure..."

REQUIRED_FILES=(
    "README.md"
    "requirements.txt" 
    "init_project.py"
    "manage.py"
    "manage.sh"
    "ROADMAP.md"
    "PROJECT_GOALS.md"
    "BOOTSTRAP_PROMPT.md"
    "scripts/create-branch.sh"
    "scripts/merge-to-main.sh"
    "scripts/run-tests.sh"
    "tests/test_template.py"
    "modules/{{MODULE_1}}.py"
    "modules/{{MODULE_2}}.py"
    "{{MAIN_FILE}}"
    "pytest.ini"
    ".coveragerc"
    "TESTING.md"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        log_pass "$file exists"
    else
        log_fail "$file missing"
    fi
done

# Test 4: Template Variable Documentation
echo ""
log_info "Checking template variables..."

TEMPLATE_VARS=(
    "{{PROJECT_NAME}}"
    "{{SERVER_URL}}"
    "{{MAIN_FILE}}"
    "{{MODULE_1}}"
    "{{MODULE_2}}"
    "{{HEALTH_ENDPOINT}}"
)

# Check if variables are documented somewhere
if [ -f "README.md" ] || [ -f "BOOTSTRAP_PROMPT.md" ]; then
    log_pass "Template documentation files exist"
else
    log_warn "No template documentation found"
fi

# Test 5: Requirements.txt Format
echo ""
log_info "Validating requirements.txt format..."

if [ -f "requirements.txt" ]; then
    if grep -q "^flask" requirements.txt && grep -q "^pytest" requirements.txt; then
        log_pass "requirements.txt has core dependencies"
    else
        log_warn "requirements.txt missing core dependencies"
    fi
    
    # Check for version pinning
    if grep -q ">=" requirements.txt; then
        log_pass "requirements.txt uses version pinning"
    else
        log_warn "requirements.txt has no version constraints"
    fi
else
    log_fail "requirements.txt not found"
fi

# Test 6: Test Framework Validation
echo ""
log_info "Testing pytest configuration..."

if [ -f "pytest.ini" ]; then
    log_pass "pytest.ini exists"
    if grep -q "testpaths" pytest.ini && grep -q "addopts" pytest.ini; then
        log_pass "pytest.ini properly configured"
    else
        log_warn "pytest.ini missing key configurations"
    fi
else
    log_fail "pytest.ini missing"
fi

if [ -f ".coveragerc" ]; then
    log_pass ".coveragerc exists"
    if grep -q "source = modules" .coveragerc; then
        log_pass ".coveragerc properly configured"
    else
        log_warn ".coveragerc missing modules configuration"
    fi
else
    log_fail ".coveragerc missing"
fi

# Test 7: Mock Roadmap Update Test
echo ""
log_info "Testing roadmap update mechanism..."

if [ -f "scripts/update-roadmap.sh" ]; then
    log_pass "update-roadmap.sh exists"
    # Create a test roadmap
    TEST_ROADMAP=$(mktemp)
    cat > "$TEST_ROADMAP" << 'EOF'
- [ ] **test-feature** - Test feature description
- [x] **completed-feature** - Already done
EOF
    
    # Test the script (dry run style)
    if bash -n scripts/update-roadmap.sh 2>/dev/null; then
        log_pass "update-roadmap.sh syntax valid"
    else
        log_fail "update-roadmap.sh has syntax errors"
    fi
    
    rm -f "$TEST_ROADMAP"
else
    log_warn "update-roadmap.sh not found (may not be implemented yet)"
fi

# Test 8: Cross-Platform Compatibility
echo ""
log_info "Checking cross-platform support..."

if [ -f "scripts/run-tests.bat" ] && [ -f "manage.bat" ]; then
    log_pass "Windows batch files present"
else
    log_warn "Windows batch files missing"
fi

# Summary
echo ""
echo "🏁 Validation Summary"
echo "===================="

if [ $VALIDATION_ERRORS -eq 0 ]; then
    log_pass "All critical validations passed!"
    if [ $VALIDATION_WARNINGS -eq 0 ]; then
        echo "🎉 Template is in excellent condition!"
        exit 0
    else
        echo "⚠️  $VALIDATION_WARNINGS warnings found - template is functional but could be improved"
        exit 0
    fi
else
    echo "❌ $VALIDATION_ERRORS critical errors found"
    if [ $VALIDATION_WARNINGS -gt 0 ]; then
        echo "⚠️  $VALIDATION_WARNINGS warnings found"
    fi
    echo ""
    echo "🔧 Fix critical errors before using template"
    exit 1
fi
