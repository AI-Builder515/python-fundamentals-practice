"""E-COMMERCE FINANCIAL ENGINE"""
number_of_orders =	320
average_order_value	= 2500
product_cost_rate =	0.55
discount_rate = 0.08
delivery_fee_collected_per_order = 150
delivery_expense_per_order =  100
payment_gateway_fee_rate = 0.02
marketing_expenses = 45000
fixed_operating_expenses = 60000
tax_rate = 	0.10

gross_sales = number_of_orders * average_order_value
total_discount = gross_sales * discount_rate
sales_after_discount = gross_sales - total_discount
delivery_income = number_of_orders * delivery_fee_collected_per_order
total_revenue = sales_after_discount + delivery_income
cost_of_goods_sold = gross_sales * product_cost_rate
total_delivery_expenses = number_of_orders * delivery_expense_per_order
payment_gateway_fee  =  sales_after_discount * payment_gateway_fee_rate
total_expense = cost_of_goods_sold + total_delivery_expenses + payment_gateway_fee + fixed_operating_expenses + marketing_expenses
profit_before_tax = total_revenue - total_expense
tax = profit_before_tax * tax_rate
net_profit = profit_before_tax - tax
net_profit_margin = (net_profit / total_revenue) * 100 

print("=" * 50)
print("           ECOMMERCE FINANCIAL ENGINE")
print("=" * 50)
print(f"NUMBER OF ORDERS: {number_of_orders:,}")
print(f"AVERAGE ORDER VALUE: {average_order_value:,.2f}")
print(f"PRODUCT COST RATE: {product_cost_rate * 100:.0f} %")
print(f"DISCOUNT RATE: {discount_rate * 100:.0} %")
print(f"DELIVERY FEE PER ORDER: {delivery_fee_collected_per_order:,.2f}")
print(f"DELIVERY EXPENSE PER ORDER: {delivery_expense_per_order:,.2f}")
print(f"PAYMENT GATEWAY FEE RATE: {payment_gateway_fee_rate * 100:.0f} %")
print(f"MARKETING EXPENSE: {marketing_expenses:,.2f}")
print(f"FIXED OPERATING EXPENSE: {fixed_operating_expenses:,.2f}")
print(f"TAX RATE: {tax_rate * 100:,.0f} % ")
print(f"GROSS SALES: {gross_sales:,.2f}")
print(f"TOTAL DISCOUNT: {total_discount:,.2f}")
print(f"SALES AFTER DISCOUNT: {sales_after_discount:,.2f}")
print(f"DELIVERY INCOME: {delivery_income:,.2f}")
print(f"COGS: {cost_of_goods_sold:,.2f}")
print(f"DELIVERY EXPENSE: {total_delivery_expenses:,.2f}")
print(f"PAYMENT GATEWAY FEES: {payment_gateway_fee:,.2f}")
print(f"TOTAL EXPENSE: {total_expense:,.2f}")
print(f"PROFIT BEFORE TAX: {profit_before_tax:,.2f}")
print(f"TAX AMOUNT: {tax :,.2f}")
print(f"NET PROFIT: {net_profit:,.2f}")
print("-" * 50)
print(f"NET PROFIT MARGIN: {net_profit_margin:.2f}%")
print("=" * 50)