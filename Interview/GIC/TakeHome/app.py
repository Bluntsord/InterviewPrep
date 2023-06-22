from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

accounts = {}
transactions = {}

@app.route('/deposit', methods=['POST'])
def deposit():
    amount = float(request.json['amount'])
    if 'balance' not in accounts:
        accounts['balance'] = amount
    else:
        accounts['balance'] += amount

    transaction_id = len(transactions)
    transactions[transaction_id] = {
        'date': datetime.utcnow(),
        'amount': amount,
        'balance': accounts['balance'],
    }

    return jsonify({'balance': accounts['balance'], 'transaction_id': transaction_id})

@app.route('/withdraw', methods=['POST'])
def withdraw():
    amount = float(request.json['amount'])

    if 'balance' not in accounts or accounts['balance'] < amount:
        return jsonify({'error': 'Insufficient balance'}), 400

    accounts['balance'] -= amount
    transaction_id = len(transactions)
    transactions[transaction_id] = {
        'date': datetime.utcnow(),
        'amount': -amount,
        'balance': accounts['balance'],
    }

    return jsonify({'balance': accounts['balance'], 'transaction_id': transaction_id})

@app.route('/statement', methods=['GET'])
def statement():
    return jsonify([{k: v for k, v in t.items() if k != 'balance'} for t in transactions.values()])

@app.route('/quit', methods=['POST'])
def quit():
    return jsonify({'message': 'Thank you for banking with AwesomeGIC Bank. Have a nice day!'})

if __name__ == '__main__':
    app.run(debug=True)
