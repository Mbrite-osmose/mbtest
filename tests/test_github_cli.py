import builtins
from unittest import mock

import pytest

from src import github_cli


def test_get_repos():
    with mock.patch('requests.get') as m:
        m.return_value.json.return_value = [
            {'name': 'repo1'},
            {'name': 'repo2'},
        ]
        m.return_value.raise_for_status.return_value = None
        repos = github_cli.get_repos('org', 'token')
        assert repos == ['repo1', 'repo2']
        m.assert_called_once()


def test_get_backlog_issues_filters_pull_requests():
    with mock.patch('requests.get') as m:
        m.return_value.json.return_value = [
            {'number': 1, 'title': 'a', 'labels': [], 'pull_request': {}},
            {'number': 2, 'title': 'b', 'labels': [{'name': 'backlog'}]},
        ]
        m.return_value.raise_for_status.return_value = None
        issues = github_cli.get_backlog_issues('org', 'repo', 'token')
        assert issues == [{'number': 2, 'title': 'b', 'labels': ['backlog']}]

