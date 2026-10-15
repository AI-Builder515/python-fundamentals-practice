"""CURRENCY EXCHANGE CALCULATOR"""

usd_amount = 750
exchange_rate = 279.50
transaction_fee = 0.02

converted_amount = usd_amount * exchange_rate
fees = converted_amount * 2 / 100
final_amount = converted_amount - fees

print("=" * 50)
print("         CURRENCY EXCHANGE CALCULATOR")
print("=" * 50)
print(f"USD:  {usd_amount:,.2f}")
print(f"EXCHANGE RATE: {exchange_rate:,.2f}")
print(f"TRANSACTION FEES: {fees:.2f} ")

print("-" * 50)
print(f"FINAL AMOUNT: {final_amount:,.2f}")
print("=" * 50)