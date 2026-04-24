#!/usr/bin/python3
"""
Consuming and processing data from an API using Python.
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints their titles."""
    url = 'https://jsonplaceholder.typicode.com/posts'
    r = requests.get(url)
    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetches all posts and saves them into a CSV file."""
    url = 'https://jsonplaceholder.typicode.com/posts'
    r = requests.get(url)

    if r.status_code == 200:
        posts = r.json()
        # Məlumatı lüğət siyahısı şəklində strukturlaşdırırıq
        data = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']}
            for p in posts
        ]

        # CSV faylına yazırıq
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
