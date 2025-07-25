import random
#This is to randomize fruit outputs to make the game more challenging.
fruits = ["🍎", "🍊", "🥑", "🍓", "🥝", "🥥", "🍋", "🍏"] 
#List of all fruit options that users can choose from
def welcometofruitgame():
    #This is a welcome function
    print("\nWelcome to the fruit game! Your goal is to combine as many fruits as possible to get to the green apple!")
    print(f"Fruit options are: {fruits}")

welcometofruitgame()
#Calling the function
loop = True
while loop:
    random_fruit = random.choice(fruits)
    fruit1 = input("What two fruits do you want to combine?")

    if fruit1 == "🍎🍎":
        print("🍊")
    elif fruit1 == "🍊🍊":
        print("🥑" + random_fruit + random_fruit)
    elif fruit1 == "🥑🥑":
        print(random_fruit + "🍓")
    elif fruit1 == "🍓🍓":
        print("🍍🍍" +random_fruit)
    elif fruit1 == "🍍🍍":
        print("🥝")
    elif fruit1 == "🥝🥝":
        print("🥥" + (random_fruit * 3))
    elif fruit1 == "🥥🥥":
        print("🍋" + random_fruit)
    elif fruit1 == "🍋🍋":
        print("🍏")
        print("Congrats! You won the game!")
        loop = False
    else:
        print("❌ Invalid combination. Try again") #This is to avoid user error from inputting other fruit combinations.
    #Fruit equivalencies:
        # "🍎🍎" = 🍊
        # "🍊🍊" = 🥑 + random_fruit + random_fruit
        # "🥑🥑" = random_fruit + 🍓
        # "🍓🍓" = 🍍+ random_fruit+random_fruit+random_fruit+random_fruit+random_fruit
        # "🍍🍍" = 🥝
        # "🥝🥝" = 🥥 + (random_fruit * 3)
        # "🥥🥥" = 🍋 + random_fruit
        # "🍋🍋" = 🍏 so Game Over!