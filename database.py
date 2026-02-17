import json
from datetime import datetime

class ReceiptDatabase:
    def __init__(self, filename='receipts.json'):
        self.filename = filename
        self.load_receipts()

    def load_receipts(self):
        try:
            with open(self.filename, 'r') as file:
                self.receipts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.receipts = []

    def save_receipts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.receipts, file, indent=4)

    def add_receipt(self, receipt):
        receipt['date'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        self.receipts.append(receipt)
        self.save_receipts()

    def get_receipts(self):
        return self.receipts

    def find_receipt(self, search_criteria):
        return [receipt for receipt in self.receipts if all(k in receipt and receipt[k] == v for k, v in search_criteria.items())]