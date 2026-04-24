#!/usr/bin/python3
"""
Uses the GitHub API to display a GitHub ID based on credentials.
Takes username and personal access token as arguments.
Uses Basic Authentication.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    token = sys.argv[2]

    r = requests.get(url, auth=(user, token))

    try:
        print(r.json().get('id'))
    except ValueError:
        print("None")
