#Program Name: Tip Calculator
bill_amount = float (input("\n Enter the Bill Amount: $"))
print("="*38)
print (f"\n Bill: ${bill_amount}")
tip_amount = float (0.15 * bill_amount)

print (f"\n Tip (15%): ${tip_amount:.2f}")
total = bill_amount + tip_amount
print("\n Total: $",format(total,"0.2f"))