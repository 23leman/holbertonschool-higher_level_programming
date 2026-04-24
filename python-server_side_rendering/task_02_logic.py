#!/usr/bin/python3
"""
Flask app rendering dynamic content using Jinja loops and conditions.
Reads data from a JSON file.
"""
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html')

@app.route('/items')
def items():
    """Reads items from json and renders items.html."""
    items_list = []
    try:
        # JSON faylını oxuyuruq
        with open('items.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Əgər 'items' açarı yoxdursa, boş siyahı [] qaytarırıq
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        # Fayl yoxdursa və ya xarabdırsa, səhifə çökməsin deyə siyahını boş saxlayırıq
        pass
    
    # Siyahını şablona göndəririk
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
