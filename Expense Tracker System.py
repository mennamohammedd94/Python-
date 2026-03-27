class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def total_expenses(self):
        return sum(e.amount for e in self.expenses)

    def show_expenses(self):
        for e in self.expenses:
            print(e.category, e.amount)


# Example usage
tracker = ExpenseTracker()
tracker.add_expense(Expense("Food", 100))
tracker.add_expense(Expense("Transport", 50))

tracker.show_expenses()
print("Total:", tracker.total_expenses())