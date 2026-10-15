"""LOAN REPAYMENT ANALYZER"""
total_loan_amount = 1200000
annual_interest_rate =	0.12
loan_duration =	5 
monthly_processing = 500

total_interest = total_loan_amount * annual_interest_rate * loan_duration
total_repayment = total_loan_amount + total_interest
num_of_installments = loan_duration * 12
monthly_installments = total_repayment / num_of_installments
monthly_pay_incl_fee = monthly_installments + monthly_processing
total_amount_paid = monthly_pay_incl_fee * num_of_installments

print("=" * 50) 
print("             LOAN REPAYMENT ANALYZER")
print("=" * 50)

print(f"PRINCIPAL: {total_loan_amount:,.2f}")
print(f"ANNUAL INTERSET RATE: {annual_interest_rate:,.2f}")
print(f"DURATION OF LOAN: {loan_duration}")
print(f"MONTHLY PROCESSING CHARGES: {monthly_processing}")
print(f"TOTAL INTETEST: {total_interest:,.2f} ")
print(f"TOTAL REPAYMENT: {total_repayment:,.2f}")
print(f"NUMBER OF INSTALLMENTS: {num_of_installments:,.2f}")
print(f"MONTHLY INSTALLMENTS: {monthly_installments:,.2f}")
print(f"TOTAL AMOUNT PAID: {total_amount_paid:,.2f}")