import os
from typing import List, Dict, Optional

import requests


def get_repos(org: str, token: str) -> List[str]:
    """Return a list of repository names for the organization."""
    url = f"https://api.github.com/orgs/{org}/repos"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return [repo["name"] for repo in response.json()]


def get_backlog_issues(org: str, repo: str, token: str) -> List[Dict]:
    """Return issues labeled 'backlog' for the given repository."""
    url = f"https://api.github.com/repos/{org}/{repo}/issues"
    params = {"state": "open", "labels": "backlog"}
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    issues = []
    for issue in response.json():
        # Exclude pull requests which also appear in the issues list
        if "pull_request" not in issue:
            issues.append({
                "number": issue["number"],
                "title": issue["title"],
                "labels": [l["name"] for l in issue.get("labels", [])],
            })
    return issues


def update_issue_status(org: str, repo: str, issue_number: int, token: str, assignee: str) -> None:
    """Assign the issue and move it to 'in progress'."""
    url = f"https://api.github.com/repos/{org}/{repo}/issues/{issue_number}"
    headers = {"Authorization": f"token {token}"}

    # Fetch existing labels to update them
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    labels = [l["name"] for l in data.get("labels", [])]
    if "backlog" in labels:
        labels.remove("backlog")
    if "in progress" not in labels:
        labels.append("in progress")

    payload = {"assignees": [assignee], "labels": labels}
    requests.patch(url, json=payload, headers=headers).raise_for_status()


def resolve_issue(org: str, repo: str, issue_number: int, token: str, close: bool, comment: Optional[str] = None) -> None:
    """Resolve the issue and optionally close it."""
    headers = {"Authorization": f"token {token}"}
    issue_url = f"https://api.github.com/repos/{org}/{repo}/issues/{issue_number}"

    if comment:
        comment_url = issue_url + "/comments"
        requests.post(comment_url, json={"body": comment}, headers=headers).raise_for_status()

    if close:
        requests.patch(issue_url, json={"state": "closed"}, headers=headers).raise_for_status()


def main() -> None:
    org = input("GitHub organization: ").strip()
    token = os.getenv("GITHUB_TOKEN") or input("GitHub API token: ").strip()

    repos = get_repos(org, token)
    if not repos:
        print("No repositories found.")
        return

    for idx, repo in enumerate(repos, 1):
        print(f"{idx}. {repo}")
    choice = int(input("Select repository: "))
    repo = repos[choice - 1]

    issues = get_backlog_issues(org, repo, token)
    if not issues:
        print("No backlog issues found.")
        return

    for idx, issue in enumerate(issues, 1):
        print(f"{idx}. #{issue['number']} {issue['title']}")
    issue_choice = int(input("Select issue to work on: "))
    issue_number = issues[issue_choice - 1]["number"]

    assignee = input("GitHub username to assign: ").strip()
    update_issue_status(org, repo, issue_number, token, assignee)
    print("Issue updated to in progress and assigned.")

    print("How would you like to resolve this issue?")
    print("1. Close issue")
    print("2. Leave open")
    action = input("Choose option: ").strip()
    close = action == "1"
    extra_instructions = input("Provide additional instructions for Codex (optional): ")
    if extra_instructions:
        print(f"Pretending to call Codex with instructions: {extra_instructions}")

    comment = None
    if close:
        comment = input("Enter closing comment: ")

    resolve_issue(org, repo, issue_number, token, close, comment)
    print("Issue resolution complete.")


if __name__ == "__main__":
    main()
