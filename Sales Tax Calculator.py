#Program Name: Sales Tax Calculator
item_price = float (input("\n Enter Item Price: $"))
print("="*38)
sales_tax = float (0.0825 * item_price)

print(f"\nSales Tax (8.25%):${sales_tax}")
total_cost = item_price + sales_tax
print("\nTotal Cost: $",format (total_cost, "0.2f"))