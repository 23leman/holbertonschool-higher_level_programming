#!/usr/bin/python3
"""
Takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Göndərəcəyimiz məlumatı lüğət (dictionary) şəklində hazırlayırıq
    payload = {'email': email}
    
    # POST sorğusunu göndəririk və məlumatı data parametrinə ötürürük
    r = requests.post(url, data=payload)
    
    # Qayıdan cavabın mətnini (body) çap edirik
    print(r.text)
