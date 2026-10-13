# Project Statement & Scope Document

## 1. Problem Statement
Individuals often struggle with budget management and unplanned expenditures due to a lack of simple, frictionless tools to log daily transactions. Existing mobile apps frequently require cloud synchronization, subscription models, or unnecessary complexity. There is a need for a lightweight, secure, local CLI application that allows users to record daily income and expenses, enforces strict budget guardrails with real-time feedback, and provides clear financial breakdowns without external network dependencies.

---

## 2. Scope of the Project
The **Personal Expense & Income Tracker** addresses individual financial management requirements by providing:
- Local persistent storage of transaction records (income and expense entries) and system settings.
- Real-time limit checking to warn users before they commit expenses exceeding their daily budget limit.
- Structured tabular reporting of transaction logs.
- Category-wise financial aggregation and analytics calculated dynamically.

### Out of Scope
- Multi-user authentication and cloud server synchronization.
- Multi-currency conversions and live exchange rates.
- Graphical User Interfaces (GUI) or mobile app integrations.

---

## 3. Target Users
- **Students & Individuals:** Looking for a straightforward offline tool to monitor daily living expenses and allowances.
- **Budget-Conscious Users:** Individuals who need hard daily budget enforcement to curb overspending.
- **Privacy-Oriented Users:** Users who prefer keeping financial records locally on their machine without sharing data with third-party web services.

---

## 4. High-Level Features

1. **Transaction Entry & Categorization:**
   - Interactive CLI prompts to log amount, category, and description.
   - Auto-generated unique transaction IDs (`uuid`) and automated ISO timestamping (`YYYY-MM-DD`).

2. **Budget Safety Guardrails:**
   - User-defined daily expense thresholds stored persistently in `settings.json`.
   - Real-time calculation of daily cumulative spend with user confirmation prompts when budget thresholds are breached.

3. **Dynamic Financial Analytics:**
   - Total spending summary across all expense categories.
   - Percentage-based analysis ($\text{Category Percentage} = \frac{\text{Category Spend}}{\text{Total Spend}} \times 100$) for visual insight into spending habits.

4. **Persistent File I/O:**
   - Robust JSON loading/saving using robust error handling (`JSONDecodeError`, `IOError`) and relative path anchoring (`os.path`).