""" ELECTRICITY BILL ANALYZER"""
units_consumed = 450
cost_per_unit = 65
fixed_meter_charges = 850
fuel_adjustment_charges = 1250
government_tax = 0.17
previous_unpaid_balance	= 2400

electricity_cost = units_consumed * cost_per_unit
bill_before_tax = electricity_cost + fixed_meter_charges + fuel_adjustment_charges
tax = bill_before_tax * government_tax
gov_tax = bill_before_tax + tax
current_bill = bill_before_tax + tax
final_bill = current_bill + previous_unpaid_balance

print("=" * 50)
print("      ELECTRICITY BILL ANALYZER")
print("=" * 50)
print(f"CONSUMED UNITS: {units_consumed:,.2f}")
print(f"COST PER UNIT:  {cost_per_unit:,.2f}")
print(f"FIXED METER CHARGES: {fixed_meter_charges:,.2f}")
print(f"FUEL ADJUSTMENT CHARGES: {fuel_adjustment_charges:,.2f}")
print(f"GOVERNMENT TAX: {government_tax} %")
print(f"PREVIOUS BALANCE: {previous_unpaid_balance:,.2f}")
print(f"ELECTRICITY COST: {electricity_cost:,.2f}")
print(f"BILL BEFORE TAX: {bill_before_tax:,.2f}")
print(f"GOVERNMENT TAX: {gov_tax:,.2f}")
print(f"CURRENT BILL: {current_bill:,.2f}")

print("-" * 50)
print(f"FINAL BILL: {final_bill:,.2f}")
print("=" * 50)
