**FOR BANKING1.PY FILE AND BANKGUI.PY 

🏦 Banking System – Streamlit App**

A visually appealing and interactive Banking System built using Python, Streamlit, and OOP concepts.
This project allows users to create accounts, deposit money, withdraw funds, transfer money, calculate interest, and view all accounts—all inside a modern UI with a finance-themed background.

🌟 Features

🔹 Create Account

Create Savings or Checking accounts

Add initial balance

Set interest rate for savings

Uses OOP class inheritance

💰 Deposit

Deposit money safely into any existing account

Validation for invalid amounts

💸 Withdraw

Withdraw money with exception handling

Custom InsufficientFundsError implemented

🔁 Transfer Money

Transfer funds between any two accounts

Transaction class handles debit & credit securely

📈 Calculate Interest

Available for Savings Account only

Interest is added to the balance and updated instantly

📜 Display All Accounts

Shows account number, account holder name, and balance

Clean, modern UI presentation

🛠️ Technologies Used

Technology	Purpose
Python	Core logic and OOP structure
Streamlit	Web interface
HTML/CSS	Background image, styling
OOP Concepts	Inheritance, custom exceptions, composition

🎨 UI Highlights

✔ Finance-themed background
✔ Centered white headings
✔ Stylish buttons with animations
✔ Modern layout with columns
✔ Professional look suitable for academic submissions

🚀 How to Run this Project 

Follow the steps below even if this is your first time running a Python project.

Step 1: Install Python

Download from: https://www.python.org/downloads/

Step 2: Install Required Libraries

Open CMD or Terminal and run:

pip install streamlit

Step 3: Save the Code

Create a file named banking_app.py and paste the full project code inside.

Step 4: Run the Application

Run this command in the terminal:

streamlit run banking_app.py


✔ A browser window will automatically open
✔ You can now use the Banking System interactively

📦 Project Structure

Banking-System/
│── banking_app.py       # Main Streamlit application
│── README.md            # Project documentation

📄 Object-Oriented Concepts Used

Concept	Where Used
Classes	Account, SavingsAccount, CheckingAccount, Transaction
Inheritance	SavingsAccount & CheckingAccount inherit from Account
Custom Exception	InsufficientFundsError
Method Overriding	SavingsAccount modifies behavior (interest feature)
Encapsulation	Account data stored inside objects

📊 Account Types

1️⃣ Savings Account

Supports deposits & withdrawals

Interest can be calculated

Inherits from the base Account class

2️⃣ Checking Account

Basic deposit & withdraw features

No interest calculation

Simpler than savings
