"""
    AutoGitHub v0.1
    Developed by Antonio Lo Fiego - github.com/antoniolofiego
"""

import sys
import json
from github import Github


def _create_github():
    """
        Creates a repository on GitHub through the PyGithub library, which uses the GitHub REST API v3.
        It is not meant to be used on its own, but in conjunction with the AutoGitHub utility.
    """
    with open('credentials.json', 'r')  as f:
        access_token = json.load(f)[sys.argv[1]]
  
    g = Github(access_token)
    g.get_user().create_repo(sys.argv[2])

if __name__ == '__main__':
    _create_github()