from flask import Flask, render_template

app = Flask(__name__)

# Our current customer
customer_name = "donsky"
# Customer list of orders
customer_orders = ["shoes", "bags", "cap"]

@app.route('/')
def index():
    return 'Hello world'

@app.route('/orders')
def orders():
    return render_template('orders.html', customer_name=customer_name, customer_orders=customer_orders)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
