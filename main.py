from tracker import ExpenseTracker
from analytics import ExpenseAnalytics

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n========================================")
        print("    PERSONAL EXPENSE & INCOME TRACKER   ")
        print("========================================")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View All Transactions")
        print("4. Delete a Transaction")
        print("5. Set / View Daily Expense Limit")
        print("6. View Analytics & Financial Summary")
        print("7. Exit")
        print("----------------------------------------")
        
        choice = input("Select an option (1-7): ").strip()

        if choice == '1':
            try:
                amt = float(input("Enter expense amount: "))
                cat = input("Enter category (e.g., Food, Travel, Rent): ")
                desc = input("Enter description: ")
                tracker.add_expense(amt, cat, desc)
            except ValueError:
                print("Error: Invalid numerical amount.")

        elif choice == '2':
            try:
                amt = float(input("Enter income amount: "))
                cat = input("Enter category (e.g., Salary, Allowance, Freelance): ")
                desc = input("Enter description: ")
                tracker.add_income(amt, cat, desc)
            except ValueError:
                print("Error: Invalid numerical amount.")

        elif choice == '3':
            tracker.view_all_transactions()

        elif choice == '4':
            t_id = input("Enter Transaction ID to delete: ").strip()
            tracker.delete_transaction(t_id)

        elif choice == '5':
            print(f"Current Daily Limit: ${tracker.settings.daily_limit:.2f}")
            try:
                new_limit = float(input("Enter new daily limit (0 to disable): "))
                tracker.set_daily_limit(new_limit)
            except ValueError:
                print("Error: Please enter a valid numeric value.")

        elif choice == '6':
            ExpenseAnalytics.show_full_summary(tracker)

        elif choice == '7':
            print("Thank you for using Expense Tracker. Goodbye!")
            break
            
        else:
            print("Invalid selection. Please choose an option between 1 and 7.")

if __name__ == "__main__":
    main()