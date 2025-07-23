print ("\nExample 1: Basic For Loop")
print("-"*25)

for i in range (1,11):
    print (f"This is loop number {i}")
print ("\nLoop is finished!\n")

print ("Example 2: Counting 1 to 10")
print ("-"*24)

for number in range (1,11):
    print(f"Count: {number}")
print ("\nCounting complete!")
print ("-"*24)

print ("Example 3: Looping Through a List")
print ("-"*24)

#Create a list of favorite foods
favorite_foods = ["\nlasagna", "sushi","pancakes", "brownies"]
for food in favorite_foods:
    print (food)

Fruits = ["\nmango", "strawberry", "pineapple"]
for fruit in Fruits: 
    print (fruit)

print ("-"*24)
for number in range (1,6):
    print (number)

print ("\nExample 4: Skip Counting")
print ("-"*24)
for num in range (0,21,2):
    print (f"Even number: {num}")

print ("\nAll even numbers from 0 to 20!")

print ("\nExample 5: Multiplication Table for 5")
print ("-"*24)
for i in range (1,19):
    product = 5* i
    print (f"5 * {i} = {product}")

print ("\nMultiplication table complete!\n")

print ("\nExample 6: Looping Through Letters")
print ("-"*24)
word = "PYTHON"
for letter in word:
    print (f"Letter: {letter}")
print (f"\nThe word '{word}' has {len(word)} letters!\n")


for row in range (3): #Outer loop - runs 3 times
    print (f" Row {row + 1}: ", end ="") 

    for star in range (5):
        print ("*", end ="")
    print()

times = int (input ("\nHow many times should I say hello?"))

for i in range (times):
    print (f"Hello #{i+1}")

print ("\nAll done saying hello!")
print ()
