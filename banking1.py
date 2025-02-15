import streamlit as st

# Apply custom CSS for background and styling
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://source.unsplash.com/1600x900/?finance,money,banking");
    background-size: cover;
    background-position: center;
}

h1, h2, h3 {
    color: white !important;
    text-align: center;
}

div.stButton > button {
    width: 100%;
    font-size: 16px;
    font-weight: bold;
    border-radius: 10px;
}

div.stTextInput > label, div.stNumberInput > label {
    color: white !important;
    font-size: 18px;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title with icon
st.markdown("<h1>🏦 Banking System </h1>", unsafe_allow_html=True)

class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"✅ Deposited {amount}. New balance: {self.balance}."
        return "⚠ Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"❌ Insufficient funds! Available balance: {self.balance}.")
        elif amount > 0:
            self.balance -= amount
            return f"✅ Withdrew {amount}. New balance: {self.balance}."
        return "⚠ Withdrawal amount must be positive."

    def display_account_info(self):
        return f"""
        **📌 Account Number:** {self.account_number}  
        **👤 Account Holder:** {self.account_holder}  
        **💰 Balance:** {self.balance}
        """

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, initial_balance=0, interest_rate=0.01):
        super().__init__(account_number, account_holder, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"✅ Interest added: {interest}. New balance: {self.balance}."

class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, initial_balance=0):
        super().__init__(account_number, account_holder, initial_balance)

class Transaction:
    def __init__(self, transaction_id, from_account, to_account, amount):
        self.transaction_id = transaction_id
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount

    def execute(self):
        try:
            self.from_account.withdraw(self.amount)
            self.to_account.deposit(self.amount)
            return f"✅ Transaction {self.transaction_id} executed successfully."
        except InsufficientFundsError as e:
            return f"❌ Transaction {self.transaction_id} failed: {e}"

# Initialize session state for accounts
if "accounts" not in st.session_state:
    st.session_state.accounts = {}

# Sidebar navigation menu
menu = st.sidebar.radio("🔹 Select an Action:", [
    "🏦 Create Account", "💰 Deposit", "💸 Withdraw", "🔁 Transfer", "📈 Calculate Interest", "📜 Display Accounts"
])

if menu == "🏦 Create Account":
    st.subheader("🚀 Create a New Account")
    col1, col2 = st.columns(2)
    
    with col1:
        account_number = st.text_input("🔢 Account Number")
        account_holder = st.text_input("👤 Account Holder Name")

    with col2:
        account_type = st.selectbox("🏦 Account Type", ["Savings", "Checking"])
        initial_balance = st.number_input("💵 Initial Balance", min_value=0.0, format="%.2f")

    if account_type == "Savings":
        interest_rate = st.number_input("📈 Interest Rate", min_value=0.0, format="%.2f")
    else:
        interest_rate = None

    if st.button("✅ Create Account"):
        if account_number and account_holder:
            if account_type == "Savings":
                st.session_state.accounts[account_number] = SavingsAccount(account_number, account_holder, initial_balance, interest_rate)
            else:
                st.session_state.accounts[account_number] = CheckingAccount(account_number, account_holder, initial_balance)
            st.success("🎉 Account created successfully!")
        else:
            st.error("⚠ Please enter valid details.")

elif menu == "💰 Deposit":
    st.subheader("💰 Deposit Money")
    account_number = st.text_input("🔢 Account Number")
    amount = st.number_input("💵 Amount", min_value=0.0, format="%.2f")

    if st.button("✅ Deposit"):
        if account_number in st.session_state.accounts:
            result = st.session_state.accounts[account_number].deposit(amount)
            st.success(result)
        else:
            st.error("❌ Account not found!")

elif menu == "💸 Withdraw":
    st.subheader("💸 Withdraw Money")
    account_number = st.text_input("🔢 Account Number")
    amount = st.number_input("💵 Amount", min_value=0.0, format="%.2f")

    if st.button("✅ Withdraw"):
        if account_number in st.session_state.accounts:
            try:
                result = st.session_state.accounts[account_number].withdraw(amount)
                st.success(result)
            except InsufficientFundsError as e:
                st.error(e)
        else:
            st.error("❌ Account not found!")

elif menu == "🔁 Transfer":
    st.subheader("🔁 Transfer Money")
    from_account_number = st.text_input("🔻 From Account Number")
    to_account_number = st.text_input("🔺 To Account Number")
    amount = st.number_input("💵 Amount", min_value=0.0, format="%.2f")

    if st.button("✅ Transfer"):
        if from_account_number in st.session_state.accounts and to_account_number in st.session_state.accounts:
            transaction = Transaction("T001", st.session_state.accounts[from_account_number], st.session_state.accounts[to_account_number], amount)
            result = transaction.execute()
            st.success(result)
        else:
            st.error("❌ One or both accounts not found!")

elif menu == "📈 Calculate Interest":
    st.subheader("📈 Calculate Interest (Savings Account)")
    account_number = st.text_input("🔢 Account Number")

    if st.button("✅ Calculate Interest"):
        if account_number in st.session_state.accounts:
            if isinstance(st.session_state.accounts[account_number], SavingsAccount):
                result = st.session_state.accounts[account_number].calculate_interest()
                st.success(result)
            else:
                st.error("⚠ Interest calculation is only available for savings accounts!")
        else:
            st.error("❌ Account not found!")

elif menu == "📜 Display Accounts":
    st.subheader("📜 List of All Accounts")
    if st.session_state.accounts:
        for acc in st.session_state.accounts.values():
            st.markdown(acc.display_account_info())
            st.divider()
    else:
        st.warning("⚠ No accounts created yet.")
