columns=int (input ("Enter the number of columns:"))
rows = int (input ("Enter the number of rows:"))
symbol = (input("Enter a symbol to use (like *, #,@,$,%,^,&,etc.)"))

for row in range (rows):
    print (f"\n {symbol} ", end ="")
    for column in range (columns-1):
        print(f" {symbol} ", end = "")

print("\n🎉 Pattern complete!")
print(f"You made a {rows} x {columns} pattern using '{symbol}'! ")
print ("🌟 Amazing work! You're a pattern master!\n")