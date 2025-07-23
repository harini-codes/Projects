age = int(input("What is your age ?"))
if age >= 16:
    print (f"You are {age} years old.")
    print ("You are old enough to drive!")

else: print (f"You are not old enough to drive yet.")
print ("=" *40)

#Create a variable for temperature
temperature = int (input ("\nWhat is the temperature outside?"))
if temperature >= 75: 
    print (f"\nIt's {temperature} degrees outside.")
    print ("It's hot! Wear shorts and a t-shirt")
else: print (f"It's {temperature} degrees outside.")
print("It's cool! Wear a jacket.")
print ("=" *40)

#Create a variable for student grade
student_grade = int (input("\nWhat is your grade?"))
if student_grade >= 90:
    print (f"Your grade is {student_grade}.")
    print ("Excellent! You got an A.\n")
elif student_grade >= 80:
    print (f"Your grade is {student_grade}.")
    print ("Great job! You got a B.\n")
else:
    print (f"Your grade is {student_grade}.")
    print ("Keep studying! You can do better.\n")

print ("=" *40)

score = int (input ("\nWhat is your score?"))
#Not equal to operator (!=) - checks if two things are different
if score != 100:
    print (f"Your score is {score}.")
    print ("Almost perfect, but not quite 100!") 
elif score >=100:
    print (f"Your score is {score}.")
    print ("Great job! You scored 100.")

#Variable for day of the weeek
day = (input ("\nWhat day is it?"))
if day == "Saturday" or day == "Sunday":
    print (f"Today is {day}.")
    print ("It's the weekend! Time to relax.")
else:
    print (f"Today is {day}.")
    print ("It's a weekday. Time for school or work.")

print ("=" *40)

#Get user's age
user_age = int (input ("\nHow old are you?"))
if user_age < 13 :
    print ("You're a kid! Enjoy being young.")
elif user_age > 13 and user_age <= 19: 
    print ("You're a teenager! These are exciting years.")
else:
    print ("You're an adult! You have lots of responsibilities.")

print ("=" *40)


