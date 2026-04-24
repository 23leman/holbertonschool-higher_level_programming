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

    # Basic Authentication istifadə edərək GET sorğusu göndəririk
    r = requests.get(url, auth=(user, token))

    try:
        # Cavabı JSON-a çeviririk və 'id' açarını götürürük
        # Əgər 'id' tapılmazsa (məs. səhv login), .get('id') avtomatik None qaytarır
        print(r.json().get('id'))
    except ValueError:
        print("None")
