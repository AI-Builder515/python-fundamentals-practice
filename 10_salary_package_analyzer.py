"""SALARY PACKAGE ANALYZER"""
basic_monthly_salary = 180000
house_allowance =	0.20
medical_allowance =	0.10
annual_bonus =	2 
monthly_tax	= 0.12 
monthly_provident_fund_deduction = 0.05

cal_house_allowance = basic_monthly_salary * house_allowance
cal_med_allowance = basic_monthly_salary * medical_allowance
gross_salary = basic_monthly_salary + cal_house_allowance + cal_med_allowance
cal_monthly_tax = gross_salary * monthly_tax
cal_provident_fund = basic_monthly_salary * monthly_provident_fund_deduction
net_monthly_salary = gross_salary - cal_monthly_tax - cal_provident_fund
annual_basic_salary = basic_monthly_salary * 12
cal_annual_bonus = basic_monthly_salary * annual_bonus
annual_net_salary = net_monthly_salary * 12
total_annual_compensation = gross_salary * 12 + cal_annual_bonus

print("=" * 50)
print("            SALARY PACKAGE ANALYZER")
print("=" * 50)
print(f"BASIC SALARY: {basic_monthly_salary:,.2f}")
print(f"HOUSE ALLOWANCE RATE: {house_allowance * 100:.0f} %")
print(f"MEDICAL ALLOWANCE RATE: {medical_allowance * 100:.0f} %")
print(f"ANNUAL BONUS: {annual_bonus}")
print(f"MONTHLY TAX: {monthly_tax * 100:.0f} %")
print(f"MONTHLY PROVIDENT FUND DEDUCTION: {monthly_provident_fund_deduction * 100:.0f} %")
print(f"HOUSE ALLOWANCE: {cal_house_allowance:,.2f}")
print(f"MEDICAL ALLOWANCE: {cal_med_allowance:,.2f}")
print(f"GROSS SALARY: {gross_salary:,.2f}")
print(f"MONTHLY TAX: {cal_monthly_tax:,.2f}")
print(f"PROVIDENT FUND: {cal_provident_fund:,.2f}")
print(f"NET SALARY: {net_monthly_salary:,.2f}")
print(f"ANNUAL BASIC SALARY: {annual_basic_salary:,.2f}")
print(f"ANNUAL BONUS: {cal_annual_bonus:,.2f}")
print(f"ANNUAL NET SALARY: {annual_net_salary:,.2f}")
print("-" * 50)
print(f"TOTAL ANNUAL COMPENSATION: {total_annual_compensation:,.2f}")
print(f"=" * 50)