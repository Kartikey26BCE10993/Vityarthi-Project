Personal Expense & Income Tracker

A robust, object-oriented Command Line Interface (CLI) application built in Python to track personal finances, manage daily spending limits, and provide automated spending analytics.

📌 Overview

Managing personal finances effectively requires tracking both income and expenditures. The Personal Expense & Income Tracker provides a lightweight, local, and reliable tool for users to record financial transactions, enforce daily spending budgets with real-time notifications, and analyze spending breakdowns by category.

The project is built adhering to Clean Architecture principles, utilizing Object-Oriented Programming (OOP) in Python and persistent storage using JSON data structures.

✨ Features

Transaction Management (CRUD):

Add Income and Expense transactions with custom categories and descriptions.

View all transactions formatted cleanly in a tabular console format.

Delete existing transactions using unique 8-character identifiers.

Budgeting & Limit Enforcement:

Set and inspect daily spending limits.

Automatic pre-transaction warnings when adding an expense exceeds today's daily limit.

Financial Analytics & Reporting:

Calculate total expenditures and income balance.

Dynamic percentage-based category breakdown analysis.

Persistent Local Data Storage:

Standard JSON persistence (data.json and settings.json) with relative file path anchoring to ensure portability.

🛠️ Technologies & Tools Used

Language: Python 3.x

Standard Libraries: json, os, uuid, datetime

Data Format: JSON

Version Control: Git / GitHub

🚀 Installation & Setup Instructions

Prerequisites

Ensure Python 3.8 or higher is installed on your machine. You can verify your Python version by running:

python --version


Setup Steps

Clone the Repository:

git clone https://github.com/Kartikeyavasthi17/Personal-Expense-tracker

Verify Project Structure:
Ensure the following files exist in the directory:

.
├── analytics.py
├── data.json
├── main.py
├── models.py
├── settings.json
├── storage.py
└── tracker.py


Run the Application:
Execute the application through the Python interpreter:

python main.py


🧪 Instructions for Testing

To verify the functional correctness of the system, follow these test cases:

Test Income & Expense Logging:

Launch main.py and select Option 1 to add an expense of $25.00 under category Food.

Select Option 2 to add income of $1000.00 under category Salary.

Select Option 3 to view all transactions and verify both records appear.

Test Daily Limit Warnings:

Select Option 5 and set a daily spending limit of $50.00.

Select Option 1 and attempt to log an expense of $60.00.

Confirm that the system raises a ! WARNING: DAILY EXPENSE LIMIT EXCEEDED ! prompt.

Test Data Persistence:

Exit the app (Option 7).

Re-launch python main.py and view transactions (Option 3). Verify that previously added records persist across sessions in data.json.

📸 Interactive CLI UI Preview

========================================
    PERSONAL EXPENSE & INCOME TRACKER   
========================================
1. Add Expense
2. Add Income
3. View All Transactions
4. Delete a Transaction
5. Set / View Daily Expense Limit
6. View Analytics & Financial Summary
7. Exit
----------------------------------------
Select an option (1-7): 
