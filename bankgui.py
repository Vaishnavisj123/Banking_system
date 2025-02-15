import tkinter as tk
from tkinter import messagebox

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds. Available balance is {self.balance}.")
        elif amount > 0:
            self.balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"

class BankingSystem:
    def __init__(self, root):
        self.accounts = {}

        self.root = root
        self.root.title("Banking System")
        self.root.geometry("500x500")
        self.root.configure(bg="#add8e6")  # Light blue background

        # Header Label
        self.header_label = tk.Label(root, text="Banking System", font=("Arial", 18, "bold"), bg="#4682B4", fg="white", pady=10)
        self.header_label.pack(fill="x")

        # Styling for all labels and entry fields
        label_font = ("Arial", 12)
        entry_font = ("Arial", 12)
        button_font = ("Arial", 12, "bold")

        # Frame for account creation
        self.create_account_frame = tk.Frame(root, bg="#87CEEB", padx=10, pady=10)
        self.create_account_frame.pack(pady=10, fill="x")

        self.acc_num_label = tk.Label(self.create_account_frame, text="Account Number:", font=label_font, bg="#87CEEB")
        self.acc_num_label.grid(row=0, column=0, pady=5)
        self.acc_num_entry = tk.Entry(self.create_account_frame, font=entry_font)
        self.acc_num_entry.grid(row=0, column=1, pady=5)

        self.acc_holder_label = tk.Label(self.create_account_frame, text="Account Holder:", font=label_font, bg="#87CEEB")
        self.acc_holder_label.grid(row=1, column=0, pady=5)
        self.acc_holder_entry = tk.Entry(self.create_account_frame, font=entry_font)
        self.acc_holder_entry.grid(row=1, column=1, pady=5)

        self.initial_balance_label = tk.Label(self.create_account_frame, text="Initial Balance:", font=label_font, bg="#87CEEB")
        self.initial_balance_label.grid(row=2, column=0, pady=5)
        self.initial_balance_entry = tk.Entry(self.create_account_frame, font=entry_font)
        self.initial_balance_entry.grid(row=2, column=1, pady=5)

        self.create_acc_button = tk.Button(self.create_account_frame, text="Create Account", font=button_font, bg="#32CD32", fg="white", command=self.create_account)
        self.create_acc_button.grid(row=3, columnspan=2, pady=10, ipadx=10)

        # Frame for transactions
        self.transaction_frame = tk.Frame(root, bg="#AFEEEE", padx=10, pady=10)
        self.transaction_frame.pack(pady=10, fill="x")

        self.trans_acc_num_label = tk.Label(self.transaction_frame, text="Account Number:", font=label_font, bg="#AFEEEE")
        self.trans_acc_num_label.grid(row=0, column=0, pady=5)
        self.trans_acc_num_entry = tk.Entry(self.transaction_frame, font=entry_font)
        self.trans_acc_num_entry.grid(row=0, column=1, pady=5)

        self.amount_label = tk.Label(self.transaction_frame, text="Amount:", font=label_font, bg="#AFEEEE")
        self.amount_label.grid(row=1, column=0, pady=5)
        self.amount_entry = tk.Entry(self.transaction_frame, font=entry_font)
        self.amount_entry.grid(row=1, column=1, pady=5)

        self.deposit_button = tk.Button(self.transaction_frame, text="Deposit", font=button_font, bg="#FFD700", command=self.deposit)
        self.deposit_button.grid(row=2, column=0, pady=5, ipadx=10)

        self.withdraw_button = tk.Button(self.transaction_frame, text="Withdraw", font=button_font, bg="#FF4500", fg="white", command=self.withdraw)
        self.withdraw_button.grid(row=2, column=1, pady=5, ipadx=10)

        # Frame for account information
        self.info_frame = tk.Frame(root, bg="#D8BFD8", padx=10, pady=10)
        self.info_frame.pack(pady=10, fill="x")

        self.info_acc_num_label = tk.Label(self.info_frame, text="Account Number:", font=label_font, bg="#D8BFD8")
        self.info_acc_num_label.grid(row=0, column=0, pady=5)
        self.info_acc_num_entry = tk.Entry(self.info_frame, font=entry_font)
        self.info_acc_num_entry.grid(row=0, column=1, pady=5)

        self.info_button = tk.Button(self.info_frame, text="Display Info", font=button_font, bg="#1E90FF", fg="white", command=self.display_info)
        self.info_button.grid(row=1, columnspan=2, pady=10, ipadx=10)

    def create_account(self):
        acc_num = self.acc_num_entry.get()
        acc_holder = self.acc_holder_entry.get()
        try:
            initial_balance = float(self.initial_balance_entry.get())
            if acc_num and acc_holder:
                self.accounts[acc_num] = Account(acc_num, acc_holder, initial_balance)
                messagebox.showinfo("Success", "Account created successfully!")
            else:
                messagebox.showwarning("Error", "Account number and holder name cannot be empty!")
        except ValueError:
            messagebox.showwarning("Error", "Initial balance must be a valid number!")

    def deposit(self):
        acc_num = self.trans_acc_num_entry.get()
        try:
            amount = float(self.amount_entry.get())
            if acc_num in self.accounts:
                self.accounts[acc_num].deposit(amount)
                messagebox.showinfo("Success", f"Deposited {amount}. New balance is {self.accounts[acc_num].get_balance()}.")
            else:
                messagebox.showwarning("Error", "Account not found!")
        except ValueError:
            messagebox.showwarning("Error", "Enter a valid amount!")

    def withdraw(self):
        acc_num = self.trans_acc_num_entry.get()
        try:
            amount = float(self.amount_entry.get())
            if acc_num in self.accounts:
                self.accounts[acc_num].withdraw(amount)
                messagebox.showinfo("Success", f"Withdrew {amount}. New balance is {self.accounts[acc_num].get_balance()}.")
            else:
                messagebox.showwarning("Error", "Account not found!")
        except (ValueError, InsufficientFundsError) as e:
            messagebox.showwarning("Error", str(e))

    def display_info(self):
        acc_num = self.info_acc_num_entry.get()
        if acc_num in self.accounts:
            account_info = self.accounts[acc_num].display_account_info()
            messagebox.showinfo("Account Info", account_info)
        else:
            messagebox.showwarning("Error", "Account not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingSystem(root)
    root.mainloop()
