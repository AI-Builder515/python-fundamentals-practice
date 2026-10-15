"""EMPLOYEE OVERTIME AND PAYROLL ANALYZER"""
basic_salary = 95000
house_allowance	= 18000
transport_allowance	= 7000
bonus =	0.15 
tax =	0.10 
loan_deduction = 5000

bonus_amount = basic_salary * bonus
gross_salary = basic_salary + house_allowance + transport_allowance + bonus_amount
tax_amount = gross_salary * tax
net_salary = gross_salary - tax_amount - loan_deduction

print("=" * 50)
print("       EMPLOYEE OVERTIME AND PAYROLL ANALYZER")
print("=" * 50)
print(f"BASIC SALARY: {basic_salary:,.2f}")
print(f"HOUSE ALLOWANCE: {house_allowance:,.2f}")
print(f"TRANSPORT ALLOWANCE: {transport_allowance:,.2f}")
print(f"BONUS: {bonus} % ")
print(f"TAX: {tax} %")
print(f"LOAN DEDUCTION: {loan_deduction:,.2f}")
print(f"SALARY WITH BONUS: {bonus_amount:,.2f}")
print(f"GROSS SALARY: {gross_salary:,.2f}")
print(f"TAX AMOUNT: {tax_amount:,.2f} ")
print("-" * 50)
print(f"NET SALARY: {net_salary:,.2f}")
print("=" * 50)


