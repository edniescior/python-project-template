# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Project Structure
```bash
├── src/
│   └── {{ cookiecutter.project_slug }}/  # Main package
├── tests/                  
│   ├── conftest.py        
│   ├── test_data/         
│   ├── unit/              
│   └── integration/       
├── docker/                
├── cicd/                  
├── pyproject.toml        # Project configuration
└── noxfile.py            # Development automation tasks
```

## Development Setup

1. Install uv
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Install nox
```bash
uv tool install nox
```

2. Create virtual environment and install dependencies
```bash
uv venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Install main dependencies
uv pip install .

# Install development dependencies
uv pip install --group dev
```

## Dependencies

Main dependencies:
- 
- 
- 

Development tools:
- 
- pytest
- ruff (formatting and linting)

## Code Quality

This project uses Ruff for both formatting and linting. Configuration is defined in pyproject.toml.

Formatting rules:
- Single quotes for strings
- Formatted docstring code blocks
- Other standard Ruff formatting defaults

Linting rules include:
- PEP 8 style checks (E, W)
- Bugbear (B) for additional checks
- Security checks (S)
- Import sorting (I)
- And more (see pyproject.toml for full list)

Run quality checks:
```bash
nox -s check_code_formatting  # Check code formatting
nox -s lint                  # Run linting checks
```

Fix issues:
```bash
nox -s format_code           # Format code
nox -s fix                   # Fix linting issues
```

## Testing
```bash
# Install test dependencies
uv pip install --group dev

# Run tests
pytest tests/unit            
pytest tests/integration     
pytest --cov=src            # With coverage
```

## Local Development


## Project Conventions
- Python version: {{ cookiecutter.python_version }}
- All code must pass Ruff checks
- Tests required for new features
- Keep dependencies updated and grouped appropriately in pyproject.toml

## Pre-commit Checks
Before committing changes:
```bash
nox                         # Runs formatting and linting checks
```

## Building and Distribution
This project uses Hatch for building:
```bash
# Build package
hatch build

# Create distribution
hatch build -t wheel
```

## Contact
{{ cookiecutter.author_name }} - {{ cookiecutter.author_email }}
