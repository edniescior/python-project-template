import subprocess

# Initialize a Git repository with 'main' as the default branch
subprocess.run(["git", "init", "--initial-branch=main"])
