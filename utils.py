#------------------------
from questions import *

def new_game():


    correct_guesses = 0
    question_num = 1

    print("Welcome to the game, have fan!!!")
    for key in questions1.keys():
        print("-------------------------")
        print(key)
        for i in options1[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()

        correct_guesses += check_answer(questions1.get(key), guess)
        if question_num == 10 and check_answer(questions1.get(key), guess) == 1:
            correct_guesses += 1
        if question_num % 3 == 0:
            print("your score is :", round(correct_guesses * (100/10)))
        question_num += 1

    display_score(correct_guesses)


#------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


#------------------------
def display_score(correct_guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")


    score = int((correct_guesses * (100/10)))
    print("Your Total score is: " + str(score))
#------------------------


def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False



new_game()



