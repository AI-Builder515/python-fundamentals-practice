"""SHOPPING BILL CALCULATOR"""

keyboard = 4500
mouse = 2800
headphones = 1750
key_quantity = 3
mouse_quantity = 2
headphones_quantity = 4

product_total_1 = keyboard * key_quantity
product_total_2 = mouse * mouse_quantity
product_total_3 = headphones * headphones_quantity
sub_total = product_total_1 + product_total_2 + product_total_3
discount = sub_total * 0.15
discount_amount = sub_total - discount
tax = discount_amount * 0.18
final_bill = discount_amount + tax

print("=================SHOPPING BILL====================")
print(f"KEYBOARD         Rs{keyboard:,.2f} x {key_quantity} = Rs {product_total_1:,.2f}")
print(f"MOUSE            Rs{mouse:,.2f} x {mouse_quantity}  = Rs {product_total_2:,.2f}")
print(f"HEADPHONES       Rs{headphones:,.2f} x {headphones_quantity} =  Rs {product_total_3:,.2f}")
print(f"SUBTOTAL         Rs{sub_total:,.2f}")
print(f"DISCOUNT         Rs{discount:,.2f}")
print(f"AFTER DISCOUNT   Rs{discount_amount}")
print(f"TAX              Rs{tax:,.2f}")

print("---------------------------------------------------")
print(f"FINAL BILL        Rs{final_bill:,.2f}")
print("===================================================")