import json

FILE = "expenses.json"

# Load data
def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

# Save data
def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f)

# Add expense
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses = load_expenses()
    expenses.append({"name": name, "amount": amount})
    save_expenses(expenses)

    print("Expense added!")

# View expenses
def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    total = 0
    for exp in expenses:
        print(f"{exp['name']} - ₹{exp['amount']}")
        total += exp['amount']

    print(f"Total: ₹{total}")

# Main loop
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice")