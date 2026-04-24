#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter.
Displays the id and name if the response is a valid JSON.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    payload = {'q': q}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        json_data = r.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
