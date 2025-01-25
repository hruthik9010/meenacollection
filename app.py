from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Product data
products = [
    {"name": "Silk Saree", "price": "₹2500", "image": "/static/images/silk-saree.jpg"},
    {"name": "Cotton Saree", "price": "₹1500", "image": "/static/images/cotton-saree.jpg"},
    {"name": "Designer Lehenga", "price": "₹5000", "image": "/static/images/lehenga.jpg"},
 ]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/products')
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True)