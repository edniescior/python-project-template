import nox

nox.options.sessions = ["check_code_formatting", "lint"]

@nox.session(python=['{{ cookiecutter.python_version }}'])
def format_code(session):
    """
    Format the codebase.
    """
    session.run("uv", "sync", "--only-group", "format", "--active", external=True)
    session.run("uv", "run", "--active", "ruff", "format", external=True)


@nox.session(python=['{{ cookiecutter.python_version }}'])
def check_code_formatting(session):
    """
    Check code formatting without making any changes.
    """
    session.run("uv", "sync", "--only-group", "format", "--active", external=True)
    session.run("uv", "run", "--active", "ruff", "format", "--check", external=True)


@nox.session(python=['{{ cookiecutter.python_version }}'])
def lint(session):
    """
    Perform linting checks.
    """
    session.run("uv", "sync", "--only-group", "lint", "--active", external=True)
    session.run("uv", "run", "--active", "ruff", "check", external=True)


@nox.session(python=['{{ cookiecutter.python_version }}'])
def fix(session):
    """
    Perform linting checks and automatically fix any fixable linting errors.
    """
    session.run("uv", "sync", "--only-group", "lint", "--active", external=True)
    session.run("uv", "run", "--active", "ruff", "check", "--fix", external=True)