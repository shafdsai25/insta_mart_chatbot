from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

with open('data/products.json', 'r') as f:
    products = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = handle_message(user_message)
    return jsonify({'response': response})

def handle_message(message):
    message = message.lower()
    if 'product' in message:
        return list_products()
    elif 'order' in message:
        return check_order_status()
    elif 'store' in message:
        return store_info()
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def list_products():
    product_list = ', '.join([product['name'] for product in products])
    return f"Here are some products we have: {product_list}"

def check_order_status():
    return "Please provide your order ID to check the status."

def store_info():
    return "Our store is located at 123 Insta Mart Street. We are open from 9 AM to 9 PM."

if __name__ == '__main__':
    app.run(debug=True)
