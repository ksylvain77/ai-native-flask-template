# {{PROJECT_NAME}} Testing Framework

## Overview

This project uses **pytest** with **coverage.py** for industry-standard testing, replacing the previous custom testing framework. The approach maintains the proven 4-phase testing methodology while providing reliable, well-documented testing tools.

## Key Benefits

### 🛠️ **Industry Standard Tools**

- **pytest**: Modern Python testing framework with excellent fixture and marker support
- **pytest-cov**: Industry-standard coverage reporting plugin
- **coverage.py**: Python coverage measurement tool

### 📊 **Reliable Coverage Strategy**

- **Target**: 70% coverage (configurable in `.coveragerc`)
- **Focus**: Business logic modules (`modules/`)
- **Exclusions**: Test files, scripts, virtual environment, cache files
- **Reports**: Terminal output + HTML reports in `htmlcov/`

### 🧪 **4-Phase Testing Methodology**

Maintains the proven testing approach:

1. **Unit Tests** (`@pytest.mark.unit`) - Backend function testing
2. **Integration Tests** (`@pytest.mark.integration`) - API endpoint testing
3. **Contract Tests** (`@pytest.mark.integration`) - Data contract validation
4. **System Tests** (`@pytest.mark.system`) - End-to-end functionality

## 🚀 Quick Start

### Development Testing (Fast)

```bash
# Quick unit tests (no coverage, fast feedback)
./scripts/run-tests.sh quick
```

### Full Testing

```bash
# Complete test suite with coverage
./scripts/run-tests.sh
```

### Specific Test Types

```bash
# Unit tests only
.venv/bin/python -m pytest -m unit

# Integration tests only
.venv/bin/python -m pytest -m integration

# System tests only
.venv/bin/python -m pytest -m system

# With detailed coverage
.venv/bin/python -m pytest --cov-report=html
```

## 📁 Configuration Files

### `pytest.ini`

- Test discovery settings
- Coverage configuration
- Test markers and output options
- Warning filters

### `.coveragerc`

- Coverage measurement configuration
- File exclusions and inclusions
- Report formatting options
- Minimum coverage thresholds

## 🎯 Test Implementation Guide

### Backend Function Tests (Phase 1)

```python
@pytest.mark.unit
def test_your_function():
    """Test core business logic"""
    from modules.your_module import your_function

    result = your_function()

    assert isinstance(result, dict)
    assert 'required_field' in result
```

### API Endpoint Tests (Phase 2)

```python
@pytest.mark.integration
def test_api_endpoint(service_check):
    """Test API endpoints"""
    response = requests.get(f"{BASE_URL}/api/your/endpoint")

    assert response.status_code == 200
    data = response.json()
    assert 'expected_field' in data
```

### Data Contract Tests (Phase 2.5)

```python
@pytest.mark.integration
def test_response_contract(service_check):
    """Validate API response structure"""
    response = requests.get(f"{BASE_URL}/api/data")
    data = response.json()

    # Validate required fields
    required_fields = ['field1', 'field2', 'timestamp']
    for field in required_fields:
        assert field in data

    # Validate data types
    assert isinstance(data['field1'], str)
    assert isinstance(data['timestamp'], str)
```

### System Integration Tests (Phase 3)

```python
@pytest.mark.system
def test_end_to_end_workflow(service_check):
    """Test complete workflows"""
    # Multi-step workflow testing
    response1 = requests.get(f"{BASE_URL}/api/step1")
    assert response1.status_code == 200

    response2 = requests.get(f"{BASE_URL}/api/step2")
    assert response2.status_code == 200
```

## 🔧 Test Helpers

The `TestHelpers` class provides utilities:

- `import_module_function()` - Safe module imports with skip on missing
- `check_service_running()` - Service availability checking
- Custom fixtures for service dependencies

## 📊 Coverage Reports

### Terminal Output

- Real-time coverage during test runs
- Missing line indicators
- Summary statistics

### HTML Reports

- Detailed coverage by file in `htmlcov/index.html`
- Line-by-line coverage visualization
- Branch coverage details

## 🎨 Test Organization

### Markers

- `@pytest.mark.unit` - Fast, isolated function tests
- `@pytest.mark.integration` - API and integration tests
- `@pytest.mark.system` - End-to-end system tests
- `@pytest.mark.slow` - Tests that take longer to run

### Fixtures

- `service_check` - Ensures service is running for integration tests
- Custom fixtures for test data and setup

## 💡 Best Practices

### For AI Development

1. **Start with unit tests** - Test functions as you create them
2. **Use descriptive test names** - Clear intent for AI understanding
3. **Template-based approach** - Copy and modify template tests
4. **Fail fast** - Use `--maxfail=3` to stop on repeated failures

### For Coverage

1. **Focus on business logic** - Not utility/formatting functions
2. **Aim for 70%+ coverage** - Configurable threshold
3. **Use exclusions wisely** - Skip non-business-logic files
4. **Review HTML reports** - Identify missing test areas

## 🔄 Migration from Custom Framework

If migrating from the custom test suite:

1. **Keep test structure** - Maintain 4-phase organization
2. **Convert dictionary tests** - Transform to pytest functions
3. **Add markers** - Use `@pytest.mark.*` for test categorization
4. **Update scripts** - Use pytest commands instead of custom runner
5. **Configure coverage** - Set appropriate thresholds and exclusions

## 🚨 Troubleshooting

### Common Issues

**Import Errors**: Ensure virtual environment is activated and dependencies installed

```bash
.venv/bin/python -m pip install -r requirements.txt
```

**Service Not Running**: Integration tests will be skipped if service unavailable

```bash
./manage.sh start
```

**Coverage Too Low**: Review HTML report and add tests for uncovered areas

```bash
open htmlcov/index.html
```

### Debug Options

```bash
# Verbose output with local variables
.venv/bin/python -m pytest -v --showlocals

# Stop on first failure
.venv/bin/python -m pytest -x

# Run specific test
.venv/bin/python -m pytest tests/test_template.py::test_specific_function
```

---

This testing framework provides reliable, industry-standard testing while maintaining the AI-native development patterns that make this template effective.
