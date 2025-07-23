#Print the welcome message

def welcome_message ():
    print ("="*38)
    print("\nWelcome to the Grade Calculator\n")
    print ("="*38)

def get_user_scores():
    test_score_1 = float (input("What is your score for Test #1?"))
    test_score_2 = float (input ("What is your score for Test #2?"))
    test_score_3 = float(input ("What is your score for test #3?"))
    
    return test_score_1, test_score_2, test_score_3

def calculate_average (test_score_1, test_score_2, test_score_3):
    total = test_score_1 + test_score_2 + test_score_3 
    average = total/3
    print(f"Your total is {average}")
    return average

def get_letter_grade (average):
    if average >= 90:
        return "A"
    elif average>= 80:
        return "B"
    elif average>= 70:
        return "C"
    elif average>= 60:
        return "D"
    else:
        return "F"

    
       


def display_result (test_score_1, test_score_2, test_score_3, average, grade):
    print("\nYour Results")
    print (f"Test 1: {test_score_1}")
    print (f"Test 2: {test_score_2}")
    print (f"Test 3: {test_score_3}")
    print (f"Average: {average}")
    print (f"Grade: {grade}")

#calling the welcome message function
welcome_message ()

def main():
    #variables that store user score
    test_score_1, test_score_2, test_score_3 = get_user_scores ()

    #variable that stores the avg score of user
    average = calculate_average (test_score_1, test_score_2, test_score_3)
    grade= get_letter_grade (average)
    #calling function that shows the user the results
    display_result(test_score_1, test_score_2,test_score_3, average,grade )

main()




