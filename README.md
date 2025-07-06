# Codex GitHub Interface

This simple command line tool demonstrates how Codex could interact with GitHub.
It allows a user to select a repository and backlog issue from a GitHub
organization, update the issue status to "in progress" and optionally resolve
it.

## Usage

```bash
python -m src.github_cli
```

The tool will prompt for the organization, a GitHub API token, a repository
from that organization, and a backlog issue to work on. It then asks how the
issue should be resolved and prints a message simulating a call to Codex.
