#------------------------


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
            print("your score is :", round(correct_guesses* (100/10)))
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


questions1 = {"Who created Python?: ": "A",
              "What year was Python created?: ": "B",
              "Python is tributed to which comedy group?: ": "C",
              "What is the correct file extention for python files?": "B",
              "Which operators is used to multiply?": "B",
              "Which collection is ordered, changeable, and allows duplicate numbers?": "A",
              "Which statment is used to stop a loop? ": "A",
              "What is 'init' mean? ": "D",
              "What year Betty was barn": "B",
              "What year Aviva was barn": "C"

}


options1 = [
    ["A. Guido van Rossum", "B. Aviva Ayasso", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2022"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. '.pyt'", "B. '.py'", "C. '.pt'", "D. '.pyth'"],
    ["A. #", "B. *", "C. +", "D. x"],
    ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
    ["A. break", "B. exit", "C. stop", "D. return"],
    ["A. Meaningless name", "B. All answers are correct", "C. Object", "D. constructor"],
    ["A. 1989", "B. 1999", "C. 2000", "D. 2002"],
    ["A. 1989", "B. 2000", "C. 1991", "D. 2005"]

    ]


new_game()

while play_again():
    new_game()


print("Byeeeeee!")

