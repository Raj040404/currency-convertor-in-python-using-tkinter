Project Overview
This is a Python-based Currency Converter and Bank Deposit System built using the Tkinter library. The program performs currency conversions between a set of currencies and allows the converted amount to be deposited into a specified bank account. It also maintains a record of balances and transaction history.

Features:
Currency Conversion: Convert between USD, EUR, GBP, JPY, and INR using predefined exchange rates.
Bank Account Management: Deposit converted amounts into user-specified accounts and account types (e.g., savings or checking).
Transaction History: Keep track of all transactions with date, time, and the amount converted.
Account Balance: Retrieve and display the balance for each account and currency type.
Transaction Records: View a log of all transactions for a specific account or across all accounts.
Code Breakdown:
Currency Conversion Logic:

The currency_converter() function takes the input amount and converts it from the source currency to the target currency using predefined exchange rates.
python
Copy code
conversion_rates = {
    'USD': 1.0,  
    'EUR': 0.89,  
    'GBP': 0.78,  
    'JPY': 108.70,  
    'INR': 74.52
}
Adding Converted Amount to Bank Account:

Once the conversion is done, the program prompts the user for the bank account number and account type using askstring. It then adds the converted amount to the bank account using the add_to_bank_account() function. If the account already exists, it updates the balance; otherwise, it creates a new account entry.
Transaction History:

The transaction_history dictionary stores each transaction with details of the date, time, account type, and currency.
Balance and History Display:

The show_balance() function displays the current balance of a user’s bank account, while the show_history() and show_all_transactions() functions display detailed transaction histories.
Running the Application:
Requirements:

Python 3.x
tkinter (built-in with most Python installations)
How to Run:

Save the code into a Python file, e.g., currency_converter.py.
Run the script using:
bash
Copy code
python currency_converter.py
GUI Layout:

The application window contains input fields for the amount, dropdown menus for selecting the source and target currencies, and buttons to perform actions like conversion, showing balance, and viewing transaction history.
Key Components in the UI:
Currency Selection:

variable1 and variable2 represent the "From Currency" and "To Currency" options using a Tkinter OptionMenu.
Balance and History:

show_balance_button, show_history_button, and show_all_transactions_button trigger functions that show account balances and transaction history via tkinter.messagebox.
Clear All Button:

Resets all input fields in the GUI.
Future Enhancements:
Add dynamic currency rates from an external API like OpenExchangeRates.
Add more account management features, like withdrawal functionality.
Implement secure data storage for bank account information.
