import tkinter as tk
import tkinter.messagebox
from tkinter.simpledialog import askstring, askfloat
from datetime import datetime

# GUI
root = tk.Tk()
root.title("Efficient Currency Conversion and Automated Bank Deposit")

# Function to perform currency conversion
def currency_converter():
    try:
        amount = float(Amount1_field.get())
        from_currency = variable1.get()
        to_currency = variable2.get()

        # Define conversion rates for some example currencies
        conversion_rates = {
            'USD': 1.0,  # US Dollar
            'EUR': 0.89,  # Euro
            'GBP': 0.78,  # British Pound
            'JPY': 108.70,  # Japanese Yen
            'INR': 74.52,  # Indian Rupee
        }

        if from_currency == to_currency:
            converted_amount = amount
        else:
            converted_amount = amount * (conversion_rates[to_currency] / conversion_rates[from_currency])

        Amount2_field.delete(0, tk.END)
        Amount2_field.insert(0, round(converted_amount, 2))

        # After conversion, ask for the bank account number
        bank_account_no = askstring("Bank Account Number", "Enter your bank account number:")
        
        if bank_account_no is not None:
            selected_currency_type = variable2.get()
            account_type = askstring("Account Type", f"Enter the account type for {selected_currency_type}:")
            add_to_bank_account(bank_account_no, selected_currency_type, converted_amount, account_type)
    except ValueError:
        tkinter.messagebox.showinfo("Error", "Please enter a valid amount.")

# Dictionary to store bank account balances
bank_accounts = {}

# Dictionary to store transaction history with date and time
transaction_history = {}

# Function to add converted amount to a bank account with date and time
def add_to_bank_account(account_no, currency_type, converted_amount, account_type):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if account_no in bank_accounts:
        if account_type in bank_accounts[account_no]:
            if currency_type in bank_accounts[account_no][account_type]:
                bank_accounts[account_no][account_type][currency_type] += converted_amount
            else:
                bank_accounts[account_no][account_type][currency_type] = converted_amount
        else:
            bank_accounts[account_no][account_type] = {currency_type: converted_amount}
    else:
        bank_accounts[account_no] = {account_type: {currency_type: converted_amount}}

    # Add transaction to history with date and time
    if account_no in transaction_history:
        transaction_history[account_no].append((current_datetime, account_type, currency_type, converted_amount))
    else:
        transaction_history[account_no] = [(current_datetime, account_type, currency_type, converted_amount)]

# Function to show the available balance in a bank account
def show_balance():
    bank_account_no = askstring("Bank Account Number", "Enter your bank account number:")
    
    if bank_account_no is not None:
        if bank_account_no in bank_accounts:
            balance_message = f"Available Balance for Account {bank_account_no}:\n"
            for account_type, account_data in bank_accounts[bank_account_no].items():
                balance_message += f"Account Type: {account_type}\n"
                for currency_type, balance in account_data.items():
                    balance_message += f"{currency_type}: {balance:.2f}\n"
            tkinter.messagebox.showinfo("Bank Account Balance", balance_message)
        else:
            tkinter.messagebox.showinfo("Bank Account Balance", "Account not found or no balance available.")

# Function to show transaction history for a bank account
def show_history():
    bank_account_no = askstring("Bank Account Number", "Enter your bank account number:")
    
    if bank_account_no is not None:
        if bank_account_no in transaction_history:
            history_message = f"Transaction History for Account {bank_account_no}:\n"
            for transaction_data in transaction_history[bank_account_no]:
                history_message += f"Date and Time: {transaction_data[0]}\n"
                history_message += f"Account Type: {transaction_data[1]}, Currency Type: {transaction_data[2]}, Amount: {transaction_data[3]:.2f}\n"
            tkinter.messagebox.showinfo("Transaction History", history_message)
        else:
            tkinter.messagebox.showinfo("Transaction History", "No transactions found for the account.")

# Function to show all transactions for a bank account with date and time
def show_all_transactions():
    history_message = "All Transactions with Date and Time:\n"
    for account_no, transactions in transaction_history.items():
        for transaction_data in transactions:
            history_message += f"Account No: {account_no}, Date and Time: {transaction_data[0]}\n"
            history_message += f"Account Type: {transaction_data[1]}, Currency Type: {transaction_data[2]}, Amount: {transaction_data[3]:.2f}\n"
    tkinter.messagebox.showinfo("Transaction History", history_message)

# Clear all input fields
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)

CurrenyCode_list = ["USD", "EUR", "GBP", "JPY", "INR"]

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="Amount:", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

label2 = tk.Label(root, font=('lato black', 15, 'bold'), text="From Currency:", bg="#e6e5e5", fg="black")
label2.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

label3 = tk.Label(root, font=('lato black', 15, 'bold'), text="To Currency:", bg="#e6e5e5", fg="black")
label3.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

label4 = tk.Label(root, font=('lato black', 15, 'bold'), text="Converted Amount:", bg="#e6e5e5", fg="black")
label4.grid(row=8, column=0, padx=10, pady=10, sticky=tk.W)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=1, padx=10, pady=10, ipadx=28, sticky=tk.W)

variable1 = tk.StringVar(root)
variable1.set("USD")  # Default currency
FromCurrency_option = tk.OptionMenu(root, variable1, *CurrenyCode_list)
FromCurrency_option.grid(row=3, column=1, padx=10, pady=10, ipadx=45, sticky=tk.W)

variable2 = tk.StringVar(root)
variable2.set("USD")  # Default currency
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrenyCode_list)
ToCurrency_option.grid(row=4, column=1, padx=10, pady=10, ipadx=45, sticky=tk.W)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=1, padx=10, pady=10, ipadx=31, sticky=tk.W)

convert_button = tk.Button(root, font=('arial', 15, 'bold'), text="Convert", padx=2, pady=2, bg="lightblue", fg="white", command=currency_converter)
convert_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

show_balance_button = tk.Button(root, font=('arial', 15, 'bold'), text="Show Balance", padx=2, pady=2, bg="lightblue", fg="white", command=show_balance)
show_balance_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

show_history_button = tk.Button(root, font=('arial', 15, 'bold'), text="Show History", padx=2, pady=2, bg="lightblue", fg="white", command=show_history)
show_history_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

show_all_transactions_button = tk.Button(root, font=('arial', 15, 'bold'), text="Show All Transactions", padx=2, pady=2, bg="lightblue", fg="white", command=show_all_transactions)
show_all_transactions_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

clear_button = tk.Button(root, font=('arial', 15, 'bold'), text="Clear All", padx=2, pady=2, bg="lightblue", fg="white", command=clear_all)
clear_button.grid(row=13, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
