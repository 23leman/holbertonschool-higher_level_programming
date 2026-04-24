#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Göndərəcəyimiz məlumatları bir lüğətdə (dictionary) toplayırıq
    values = {'email': email}
    
    # Məlumatları URL formatına salırıq və baytlara çeviririk
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    
    # Sorğunu hazırlayırıq (data əlavə edildiyi üçün avtomatik POST olur)
    req = urllib.request.Request(url, data)
    
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
