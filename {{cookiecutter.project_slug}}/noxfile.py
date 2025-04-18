import nox

# Default sessions to run when no session is specified
nox.options.sessions = ["check_code_formatting", "lint", "test"]

# Use Python version from cookiecutter
PYTHON_VERSION = "{{ cookiecutter.python_version }}"

# Common paths for checking
PATHS = ["src", "tests", "noxfile.py"]


@nox.session(python=[PYTHON_VERSION])
def format_code(session):
    """Format the codebase using ruff."""
    session.run("uv", "sync", "--only-group", "format", "--active", external=True)
    session.run("uv", "run", "--active", "ruff", "format", *PATHS, external=True)


@nox.session(python=[PYTHON_VERSION])
def check_code_formatting(session):
    """Check code formatting without making any changes."""
    session.run("uv", "sync", "--only-group", "format", "--active", external=True)
    session.run(
        "uv", "run", "--active", "ruff", "format", "--check", *PATHS, external=True
    )


@nox.session(python=[PYTHON_VERSION])
def lint(session):
    """Perform linting checks."""
    session.run("uv", "sync", "--only-group", "lint", "--active", external=True)
    session.run("uv", "run", "--active", "ruff", "check", *PATHS, external=True)


@nox.session(python=[PYTHON_VERSION])
def fix(session):
    """Fix linting errors automatically where possible."""
    session.run("uv", "sync", "--only-group", "lint", "--active", external=True)
    session.run("uv", "run", "--active", "ruff", "check", "--fix", *PATHS, external=True)


@nox.session(python=[PYTHON_VERSION])
def test(session):
    """Run the test suite."""
    session.run("uv", "sync", "--only-group", "dev", "--active", external=True)
    session.install("-e", ".")
    session.run("uv", "run", "--active", "pytest", "tests", *session.posargs, external=True)


@nox.session(python=[PYTHON_VERSION])
def coverage(session):
    """Run the test suite with coverage reporting."""
    session.run("uv", "sync", "--only-group", "dev", "--active", external=True)
    session.run(
        "uv",
        "run",
        "--active",
        "pytest",
        "tests",
        "--cov=src",
        "--cov-report=term-missing",
        "--cov-report=html",
        *session.posargs,
        external=True,
    )


@nox.session(python=[PYTHON_VERSION])
def clean(session):
    """Remove build artifacts and cache directories."""
    clean_dirs = [
        "build",
        "dist",
        ".coverage",
        "coverage_html",
        ".pytest_cache",
        ".ruff_cache",
        ".nox",
    ]
    for directory in clean_dirs:
        session.run("rm", "-rf", directory, external=True)
