from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Expense tracking data
expenses = []

@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    title = request.form['title']
    amount = request.form['amount']
    expenses.append({'title': title, 'amount': amount})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)