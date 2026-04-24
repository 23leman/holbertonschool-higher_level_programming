#!/usr/bin/python3
"""
Flask application to display product data from JSON, CSV, or SQLite
based on query parameters.
"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_data():
    """Reads data from products.json"""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def read_csv_data():
    """Reads data from products.csv"""
    data = []
    try:
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data

@app.route('/products')
def display_products():
    """Displays products based on source and id query parameters."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    products_data = []

    # Source parametrinin yoxlanması və müvafiq datanın çəkilməsi
    if source == 'json':
        products_data = read_json_data()
    elif source == 'csv':
        products_data = read_csv_data()
    elif source == 'sql':
        try:
            # SQLite bazasına qoşuluruq
            conn = sqlite3.connect('products.db')
            # Nəticələrin lüğət (dictionary) kimi qayıtması üçün Row factory istifadə edirik
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, category, price FROM Products")
            # Nəticələri siyahı içərisində lüğətlərə çeviririk
            products_data = [dict(row) for row in cursor.fetchall()]
            conn.close()
        except sqlite3.Error as e:
            return render_template('product_display.html', error="Database error")
    else:
        # Naməlum source xətası
        return render_template('product_display.html', error="Wrong source")

    # ID yoxlanışı və məlumatın süzgəcdən keçirilməsi (filter)
    if product_id:
        filtered_data = [p for p in products_data if str(p.get('id')) == str(product_id)]
        
        if not filtered_data:
            return render_template('product_display.html', error="Product not found")
        
        products_data = filtered_data

    return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
