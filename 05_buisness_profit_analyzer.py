"""BUISNESS PROFIT ANALYZE"""
total_sales_revenue	= 250000
cost_of_goods_sold =   140000
employee_salaries =   35000
office_rent	=         15000
marketing_expenses =  8000
other_expenses =      7000

gross_profit = total_sales_revenue - cost_of_goods_sold
total_operating_expenses = employee_salaries + office_rent + marketing_expenses + other_expenses
net_profit = gross_profit - total_operating_expenses
gross_profit_margin = gross_profit / total_sales_revenue * 100
net_profit_margin = net_profit / total_sales_revenue * 100
annual_net_profit = net_profit * 12

print("=" * 50)
print("             BUISNESS PROFIT REPORT")
print("=" * 50)
print(f"TOTAL SALES REVENUE: {total_sales_revenue:,.2f}")
print(f"COST OF GOODS:       {cost_of_goods_sold:,.2f}")
print(f"GROSS PROFIT:        {gross_profit:,.2f}")
print(f"TOTAL OPERATING EXPENSE: {total_operating_expenses:,.2f}")
print(f"NET PROFIT: {net_profit:,.2f}")
print(f"GROSS P MARGIN: {gross_profit_margin:.2f} %")
print(f"NET P MARGIN: {net_profit_margin:.2f} %")
print("-" * 50)
print(f"ANNUAL PROFIT {annual_net_profit:,.2f}")
print(f"=" * 50)