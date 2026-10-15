"""MONTHLY BUDGET ANALYZER"""
monthly_income = 150000
house_rent =  30000
food = 22000
electricity = 8500
transport =	 10000
internet_mobile = 3500
other_expenses = 15000

total_expense = (
    house_rent
    + food
    + electricity
    + transport
    + internet_mobile
    + other_expenses
)

remaining_savings = monthly_income - total_expense
saving_percentage = remaining_savings / monthly_income * 100
expense_percentage = total_expense / monthly_income * 100
annual_savings = remaining_savings * 12

print("=" * 46)
print("      MONTHLY BUDGET ANALYZER")
print("=" * 46)
print(f"MONTHLY INCOME: {monthly_income:,.2f}")
print(f"TOTAL EXPENSEs:  {total_expense:,.2f}")
print(f"REMAINING SAVINGS: {remaining_savings:,.2f}")
print(f"SAVING PERCENTAGE: {saving_percentage:.2f}%")
print(f"EXPENSE PERCENTAGE: {expense_percentage:.2f}%")
print(f"ANNUAL SAVINGS:  {annual_savings:,.2f}")

