#!/bin/bash
# {{PROJECT_NAME}} Test Runner - Pytest Implementation
# Industry-standard testing replacing custom framework

set -e

PROJECT_NAME="{{PROJECT_NAME}}"
BASE_URL="{{SERVER_URL}}"
HEALTH_ENDPOINT="{{HEALTH_ENDPOINT}}"

echo "🧪 $PROJECT_NAME - Pytest Test Runner"
echo "========================================"

# Check if virtual environment is active
if [ -z "$VIRTUAL_ENV" ] && [ -d ".venv" ]; then
    echo "⚠️  Virtual environment not active. Using .venv/bin/python"
    PYTHON_CMD=".venv/bin/python"
else
    # Try python3 first, fall back to python
    if command -v python3 >/dev/null 2>&1; then
        PYTHON_CMD="python3"
    elif command -v python >/dev/null 2>&1; then
        PYTHON_CMD="python"
    else
        echo "❌ No Python interpreter found"
        exit 1
    fi
fi

# Check if service is running (for integration tests)
echo "🔍 Checking if $PROJECT_NAME is running..."
if curl -s "$BASE_URL$HEALTH_ENDPOINT" > /dev/null 2>&1; then
    echo "✅ $PROJECT_NAME is responding at $BASE_URL"
    SERVICE_RUNNING=true
else
    echo "⚠️  $PROJECT_NAME is not responding - will run unit tests only"
    echo "💡 Start service with: ./manage.sh start"
    SERVICE_RUNNING=false
fi

# Quick development tests (no coverage)
if [ "$1" = "quick" ]; then
    echo "🚀 Running quick unit tests (no coverage)..."
    $PYTHON_CMD -m pytest tests/ -m "unit" --tb=short -q --no-cov
    exit 0
fi

# Template mode (for template itself - has placeholder tests)
if [ "$1" = "template" ]; then
    echo "🎭 Running template validation tests (no coverage requirement)..."
    if [ -d "tests/" ]; then
        $PYTHON_CMD -m pytest tests/ -m "unit" --tb=short -q --no-cov
    else
        echo "✅ No tests directory - template validation mode"
        echo "📋 Template tests will be in generated projects"
    fi
    exit 0
fi

# AI Project Inception Template mode - check template components
if [ ! -d "tests/" ] && [ -f "inception.py" ]; then
    echo "🤖 AI Project Inception Template Mode"
    echo "🧪 Running template component validation..."
    
    # Test inception.py syntax
    if $PYTHON_CMD -m py_compile inception.py; then
        echo "✅ inception.py syntax valid"
    else
        echo "❌ inception.py syntax errors"
        exit 1
    fi
    
    # Test that template generates valid documentation
    if [ -f "PROJECT_README.md" ] && [ -f "BOOTSTRAP_PROMPT.md" ]; then
        echo "✅ Template documentation structure valid"
    else
        echo "❌ Missing template documentation"
        exit 1
    fi
    
    echo "✅ Template validation passed"
    echo "📋 This template will generate projects with full test suites"
    exit 0
fi

# Run appropriate test suite based on service availability
if [ "$SERVICE_RUNNING" = true ]; then
    echo "🧪 Running full test suite with coverage..."
    $PYTHON_CMD -m pytest tests/ --cov-fail-under=70
else
    echo "🧪 Running unit tests only with coverage..."
    $PYTHON_CMD -m pytest tests/ -m "unit" --cov-fail-under=50
fi

echo ""
echo "📊 Coverage report generated in htmlcov/index.html"
echo "💡 Tips:"
echo "   • Run './scripts/run-tests.sh quick' for fast development testing"
echo "   • Run './scripts/run-tests.sh template' for template validation"
echo "   • Start service first for full integration testing"
echo "   • View detailed coverage: open htmlcov/index.html"

# Post-test health check
if [ "$SERVICE_RUNNING" = true ]; then
    echo ""
    echo "🔄 Post-test service check..."
    if curl -s "$BASE_URL$HEALTH_ENDPOINT" > /dev/null 2>&1; then
        echo "✅ Service still responding after tests"
    else
        echo "⚠️  Service may have stopped during testing"
    fi
fi
if [ "$1" = "quick" ]; then
    echo "� Running quick unit tests (no coverage)..."
    $PYTHON_CMD -m pytest tests/ -m "unit" --tb=short -q --no-cov
    exit 0
fi

# Run appropriate test suite based on service availability
if [ "$SERVICE_RUNNING" = true ]; then
    echo "🧪 Running full test suite with coverage..."
    $PYTHON_CMD -m pytest tests/ --cov-fail-under=70
else
    echo "🧪 Running unit tests only with coverage..."
    $PYTHON_CMD -m pytest tests/ -m "unit" --cov-fail-under=50
fi

echo ""
echo "📊 Coverage report generated in htmlcov/index.html"
echo "💡 Tips:"
echo "   • Run './scripts/run-tests.sh quick' for fast development testing"
echo "   • Start service first for full integration testing"
echo "   • View detailed coverage: open htmlcov/index.html"

# Post-test health check
if [ "$SERVICE_RUNNING" = true ]; then
    echo ""
    echo "� Post-test service check..."
    if curl -s "$BASE_URL$HEALTH_ENDPOINT" > /dev/null 2>&1; then
        echo "✅ Service still responding after tests"
    else
        echo "⚠️  Service may have stopped during testing"
    fi
fi
