"""EMPLOYEE SALARY CALCULATOR"""
BASIC_SALARY = 85000
HOUSE_ALLOWANCE = 15000
TRANSPORT_ALLOWANCE = 8000

performance_bonus = 0.12 
tax = 0.08
cal_performance_bonus = BASIC_SALARY * performance_bonus
amount = BASIC_SALARY + HOUSE_ALLOWANCE + TRANSPORT_ALLOWANCE + cal_performance_bonus
cal_tax = amount * tax 
final_salary = amount - cal_tax

print("================EMPLOYEE SALARY REPORT======================")
print(f"BASIC_SALARY        Rs{BASIC_SALARY}")
print(f"HOUSE_ALLOWANCE     Rs{HOUSE_ALLOWANCE}")
print(f"TRANSPORT_ALLOWANCE Rs{TRANSPORT_ALLOWANCE}")
print(f"PERFORMANCE BONUS   Rs{cal_performance_bonus}")
print(f"GROSS SALARY        Rs{amount:,.2f}")
print(f"TAX DEDUCTION       Rs{cal_tax}")

print("--------------------------------------")
print(f"FINAL SALARY        Rs{final_salary}")
print("======================================")