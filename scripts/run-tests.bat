@echo off
REM {{PROJECT_NAME}} Test Runner - Windows Pytest Implementation
REM Industry-standard testing replacing custom framework

setlocal enabledelayedexpansion

set PROJECT_NAME={{PROJECT_NAME}}
set BASE_URL={{SERVER_URL}}
set HEALTH_ENDPOINT={{HEALTH_ENDPOINT}}

echo 🧪 %PROJECT_NAME% - Pytest Test Runner
echo ========================================

REM Check if virtual environment exists
if exist .venv\Scripts\python.exe (
    set PYTHON_CMD=.venv\Scripts\python.exe
    echo ⚠️  Using virtual environment: .venv\Scripts\python.exe
) else (
    set PYTHON_CMD=python
    echo ℹ️  Using system Python
)

REM Check if service is running (for integration tests)
echo 🔍 Checking if %PROJECT_NAME% is running...
curl -s "%BASE_URL%%HEALTH_ENDPOINT%" >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ %PROJECT_NAME% is responding at %BASE_URL%
    set SERVICE_RUNNING=true
) else (
    echo ⚠️  %PROJECT_NAME% is not responding - will run unit tests only
    echo 💡 Start service with: manage.bat start
    set SERVICE_RUNNING=false
)

REM Quick development tests (no coverage)
if "%1"=="quick" (
    echo 🚀 Running quick unit tests no coverage...
    %PYTHON_CMD% -m pytest tests/ -m "unit" --tb=short -q --no-cov
    exit /b 0
)

REM Run appropriate test suite based on service availability
if "!SERVICE_RUNNING!"=="true" (
    echo 🧪 Running full test suite with coverage...
    %PYTHON_CMD% -m pytest tests/ --cov-fail-under=70
) else (
    echo 🧪 Running unit tests only with coverage...
    %PYTHON_CMD% -m pytest tests/ -m "unit" --cov-fail-under=50
)

echo.
echo 📊 Coverage report generated in htmlcov\index.html
echo 💡 Tips:
echo    • Run 'scripts\run-tests.bat quick' for fast development testing
echo    • Start service first for full integration testing
echo    • View detailed coverage: open htmlcov\index.html

REM Post-test health check
if "!SERVICE_RUNNING!"=="true" (
    echo.
    echo 🔄 Post-test service check...
    curl -s "%BASE_URL%%HEALTH_ENDPOINT%" >nul 2>&1
    if !errorlevel! equ 0 (
        echo ✅ Service still responding after tests
    ) else (
        echo ⚠️  Service may have stopped during testing
    )
)
