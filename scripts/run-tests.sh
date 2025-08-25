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
    PYTHON_CMD="python"
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
