#!/usr/bin/python3
"""
Flask application to display product data from JSON or CSV files
based on query parameters.
"""
from flask import Flask, render_template, request
import json
import csv

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
    
    error_message = None
    products_data = []

    # Source yoxlanışı
    if source == 'json':
        products_data = read_json_data()
    elif source == 'csv':
        products_data = read_csv_data()
    else:
        error_message = "Wrong source"
        return render_template('product_display.html', error=error_message)

    # ID yoxlanışı və filtreləmə
    if product_id:
        # Həm JSON-dan gələn integer, həm də CSV-dən gələn string tipli ID-ləri 
        # düzgün müqayisə etmək üçün hər ikisini string-ə çeviririk.
        filtered_data = [p for p in products_data if str(p.get('id')) == str(product_id)]
        
        if not filtered_data:
            error_message = "Product not found"
            return render_template('product_display.html', error=error_message)
        
        products_data = filtered_data

    return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
