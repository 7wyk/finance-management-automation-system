import csv
import json
import os

def sum_expense_for_month(csv_file_path):
    total_expenses = 0.0
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  
        for row in reader:
            if len(row) < 6:  
                continue
            date, _, amount, _, transaction_type, status = row
            amount = amount.replace(',', '')
            if transaction_type.lower() == 'debit':
                total_expenses += float(amount)
    return total_expenses

def update_expenses_json(json_file_path, month, total_expenses):
    expenses_data = {}
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            expenses_data = json.load(json_file)

    expenses_data[month] = total_expenses        

    with open(json_file_path, 'w') as json_file:
        json.dump(expenses_data, json_file, indent=4)

month_input = input("Please enter the month (format: yyyy-mm): ")

csv_file_name = 'transaction.csv'
json_file_name = "monthly_expenses.json"

total_month_expenses = sum_expense_for_month(csv_file_name)

print(f"Total expenses for {month_input}: {total_month_expenses}")

update_expenses_json(json_file_name, month_input, total_month_expenses)
