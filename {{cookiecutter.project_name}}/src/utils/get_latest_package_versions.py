"""
PyPI Package Version Checker

This script retrieves the latest versions of Python packages from PyPI.
It can accept package names as command-line arguments or read them from a requirements.txt file.

Usage:
    python script_name.py package1 package2 ...
    python script_name.py -r requirements.txt

The script outputs the package names along with their latest versions from PyPI.
If a package is not found or an error occurs, it displays an appropriate error message.
"""

import argparse
import re
import sys
from typing import List

import requests


def get_latest_version(package_name: str) -> str:
    """Get the latest version of a package from PyPI."""
    url = f'https://pypi.org/pypi/{package_name}/json'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data['info']['version']
    except requests.HTTPError:
        return f"Error: Package '{package_name}' not found on PyPI"
    except requests.RequestException as e:
        return f'Error retrieving {package_name}: {str(e)}'


def parse_requirements_file(file_path: str) -> List[str]:
    """Parse package names from a requirements.txt file."""
    packages = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                this_line = line.strip()
                if not this_line or this_line.startswith('#'):
                    continue

                # Remove inline comments and environment markers
                this_line = re.split(r'\s*#|\s*;', this_line)[0].strip()

                # Extract package name (supports most requirement formats)
                match = re.match(r'^([a-zA-Z0-9\-_\.]+)', this_line)
                if match:
                    package = match.group(1).lower()
                    packages.append(package)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found", file=sys.stderr)
        sys.exit(1)
    return packages


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Get latest package versions from PyPI',
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        'packages', nargs='*', help='List of package names (space-separated)'
    )
    parser.add_argument(
        '-r', '--requirements', metavar='FILE', help='Path to requirements.txt file'
    )

    args = parser.parse_args()
    all_packages = args.packages.copy()

    if args.requirements:
        all_packages.extend(parse_requirements_file(args.requirements))

    if not all_packages:
        parser.print_help()
        return

    for package in all_packages:
        version = get_latest_version(package)
        print(
            f'{package}=={version}'
            if isinstance(version, str) and version[0].isdigit()
            else f'{package}: {version}'
        )


if __name__ == '__main__':
    main()
