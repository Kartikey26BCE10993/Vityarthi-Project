# analytics.py
class ExpenseAnalytics:
    @staticmethod
    def show_summary(expenses):
        if not expenses:
            print("Not enough data to generate analytics.")
            return

        total = sum(exp.amount for exp in expenses)
        print(f"\n--- Analytics Summary ---")
        print(f"Total Spent: ${total:.2f}")

        category_totals = {}
        for exp in expenses:
            category_totals[exp.category] = category_totals.get(exp.category, 0) + exp.amount

        print("\n--- Spending by Category ---")
        for category, amount in category_totals.items():
            percentage = (amount / total) * 100
            print(f"{category}: ${amount:.2f} ({percentage:.1f}%)")
        print("----------------------------\n")