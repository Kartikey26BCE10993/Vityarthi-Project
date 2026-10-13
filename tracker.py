from datetime import datetime
from models import Transaction
from storage import StorageHandler

class ExpenseTracker:
    """Core engine handling operations, financial calculations, and limit warnings."""

    def __init__(self):
        self.storage = StorageHandler()
        self.transactions = self.storage.load_transactions()
        self.settings = self.storage.load_settings()

    def set_daily_limit(self, limit):
        """Sets user daily spending limit."""
        self.settings.daily_limit = float(limit)
        self.storage.save_settings(self.settings)
        print(f"Success: Daily expense limit set to ${self.settings.daily_limit:.2f}")

    def get_today_expense_total(self):
        """Calculates total expenses logged for today's date."""
        today_str = datetime.now().strftime("%Y-%m-%d")
        return sum(
            t.amount for t in self.transactions 
            if t.trans_type == "Expense" and t.date == today_str
        )

    def add_income(self, amount, category, description):
        """Logs income transaction."""
        income = Transaction(amount, category, description, trans_type="Income")
        self.transactions.append(income)
        self.storage.save_transactions(self.transactions)
        print(f"Success: Income of ${amount:.2f} logged under '{income.category}'.")

    def add_expense(self, amount, category, description):
        """Logs expense transaction with daily limit validation."""
        amount = float(amount)
        today_total = self.get_today_expense_total()
        limit = self.settings.daily_limit

        # Validate against Daily Limit
        if limit > 0:
            projected_total = today_total + amount
            if projected_total > limit:
                print(f"\n! WARNING: DAILY EXPENSE LIMIT EXCEEDED !")
                print(f"Daily Limit: ${limit:.2f} | Today's Current Spending: ${today_total:.2f}")
                print(f"Adding ${amount:.2f} puts your daily spending at ${projected_total:.2f}.")
                proceed = input("Do you still wish to record this expense? (y/n): ").strip().lower()
                if proceed != 'y':
                    print("Transaction cancelled.")
                    return

        expense = Transaction(amount, category, description, trans_type="Expense")
        self.transactions.append(expense)
        self.storage.save_transactions(self.transactions)
        print(f"Success: Expense of ${amount:.2f} logged under '{expense.category}'.")

    def view_all_transactions(self):
        """Displays formatted table of all recorded transactions."""
        if not self.transactions:
            print("No records found.")
            return

        print(f"\n{'-'*75}")
        print(f"{'ID':<10} | {'Type':<8} | {'Date':<12} | {'Category':<15} | {'Amount':<10}")
        print(f"{'-'*75}")
        for t in self.transactions:
            sign = "+" if t.trans_type == "Income" else "-"
            print(f"{t.id:<10} | {t.trans_type:<8} | {t.date:<12} | {t.category:<15} | {sign}${t.amount:<9.2f}")
        print(f"{'-'*75}\n")

    def delete_transaction(self, trans_id):
        """Deletes transaction by ID."""
        initial_len = len(self.transactions)
        self.transactions = [t for t in self.transactions if t.id != trans_id]
        
        if len(self.transactions) < initial_len:
            self.storage.save_transactions(self.transactions)
            print(f"Success: Record {trans_id} removed.")
        else:
            print(f"Error: Record ID '{trans_id}' not found.")