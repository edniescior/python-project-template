# Python Project Setup

## Prerequisites

### Install `uv`
Install `uv` with this command:
```
brew install uv
```

### Install `cookiecutter`
Install `cookiecutter` with the following command:
```
uv tool install cookiecutter
```

### Install `nox`
Install `nox` with the following command:
```
uv tool install nox
```

## Usage

### Use the template to create your project
Inside the folder you want to setup your project, run the following command:
```
cookiecutter gitpath

cookiecutter file:///Users/edwardn/Workspace/repos/python-project-template

```
`cookiecutter` will now prompt you for a couple of configurations like the project name, the python version, and so on.

## Directory Structure
The directory structure you will end up with will look like this:
```
.
└── <your_project_name>/
    ├── .github/
    │   └── workflows/
    │       └── ci.yaml
    ├── .gitignore
    ├── README.md
    ├── src/
    │   └── <your_app_name>/
    │       ├── __init__.py
    │       └── main.py
    ├── tests/
    │   └── test_e2e.py
    ├── noxfile.py
    └── pyproject.toml
```

## Test the setup
In order to start running the linting checks, just like it will be done inside the CI environment, you can use `nox`. There are some nox sessions defined inside the `noxfile.py`.

You can run the following sessions in order to check your code.

### Check code formatting without making any changes (this will mimic the CI code formatting checks)
```
nox --session check_code_formatting
```

### Format code (in order to pass code formatting checks inside the CI)
```
nox --session format_code
```

### Run linting checks (includes Bandit security checks)
```
nox --session lint
```

### Run linting checks and automatically fix any fixable linting errors
```
nox --session fix
```