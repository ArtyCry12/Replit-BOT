from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data to represent expenses
expenses = [
    {'id': 1, 'item': 'Coffee', 'amount': 3.5},
    {'id': 2, 'item': 'Lunch', 'amount': 15.0},
    {'id': 3, 'item': 'Book', 'amount': 20.0}
]

@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    item = request.form.get('item')
    amount = request.form.get('amount')
    new_expense = {'id': len(expenses) + 1, 'item': item, 'amount': float(amount)}
    expenses.append(new_expense)
    return render_template('index.html', expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)