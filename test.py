def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*25)
    print("Your score is: "+str(score)+"%")


def play_again():

    response = input("Would you like to try again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False



questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "My name is ?: ": "B",
 "My birthday is?: ": "A",
 "My partner name is?: ": "D",

}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. Guido van Rossum", "B. aviva ayasso", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 25.8.1991", "B. 24.5.1998", "C. 6.4.1992", "D. 27.3.1990"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. Betty"],
           ]


new_game()

while play_again():
    new_game()

print("------------------")
print("Continue to the next round")


#................................................................................

def new_game1():

    guesses1 = []
    correct_guesses1 = 0
    question_num1 = 1

    for key in questions1:
        print("-------------------------")
        print(key)
        for i in options1[question_num1-1]:
            print(i)
        guess1 = input("Enter (A, B, C, or D): ")
        guess1 = guess1.upper()
        guesses1.append(guess1)

        correct_guesses1 += check_answer1(questions1.get(key), guess1)
        question_num1 += 1

    display_score1(correct_guesses1, guesses1)


def check_answer1(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score1(correct_guesses1, guesses1):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions1:
        print(questions1.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses1:
        print(i, end=" ")
    print()

    score1 = int((correct_guesses1/len(questions1))*25)
    print("Your score is: "+str(score1)+"%")



def play_again1():

    response = input("Would you like to try again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

questions1 = {
 "My name is ?: ": "B",
 "My birthday is?: ": "A",
 "My partner name is?: ": "D",

}

options1 = [
    ["A. Guido van Rossum", "B. aviva ayasso", "C. Bill Gates", "D. Mark Zuckerburg"],
        ["A. 25.8.1991", "B. 24.5.1998", "C. 6.4.1992", "D. 27.3.1990"],
        ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. Betty"],
         ]


new_game1()

while play_again1():
    new_game1()
else:
    print("------------------")
    print("Continue to the next round")


#................................................................................



def new_game2():

    guesses2 = []
    correct_guesses2 = 0
    question_num2 = 1

    for key in questions2:
        print("-------------------------")
        print(key)
        for i in options2[question_num2-1]:
            print(i)
        guess2 = input("Enter (A, B, C, or D): ")
        guess2 = guess2.upper()
        guesses2.append(guess2)

        correct_guesses2 += check_answer2(questions2.get(key), guess2)
        question_num2 += 1

    display_score2(correct_guesses2, guesses2)


def check_answer2(answer2, guess2):

    if answer2 == guess2:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score2(correct_guesses2, guesses2):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions2:
        print(questions2.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses2:
        print(i, end=" ")
    print()

    score2 = int((correct_guesses2/len(questions2))*25)
    print("Your score is: "+str(score2)+"%")


def play_again2():

    response2 = input("Would you like to try again? (yes or no): ")
    response2 = response2.upper()

    if response2 == "YES":
        return True
    else:
        return False
questions2 = {
 "What year are was last year ?: ": "B",
 "What year are we in?: ": "D",
 "What is the color of the banana?: ": "C",

}

options2 = [
    ["A. 1991", "B. 2021", "C. 2019", "D. 2013"],
        ["A. 2021", "B. 1998", "C. 1992", "D. 2022"],
        ["A. Red", "B. Blue", "C. yellow", "D. Green"],
         ]

new_game2()

while play_again2():
   new_game2()

print("------------------")
print("Continue to the bonus round")


#................................................................................




def new_game3():

    guesses3 = []
    correct_guesses3 = 0
    question_num3 = 1

    for key in questions3:
        print("-------------------------")
        print(key)
        for i in options3[question_num3-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses3.append(guess)

        correct_guesses3 += check_answer3(questions3.get(key), guess)
        question_num3 += 1

    display_score(correct_guesses3, guesses3)


def check_answer3(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score3(correct_guesses3, guesses3):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions3:
        print(questions3.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses3:
        print(i, end=" ")
    print()

    score3 = int((correct_guesses3/len(questions3))*100)
    print("Your score is: "+str(score3)+"%")


def play_again3():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False



questions3 = {
 "what the color of the sum?: ": "A"
}

options3 = ["A. Red", "B. Blue", "C. yellow", "D. Green"],


new_game3()

while play_again3():
    new_game()




print("Byeeeeee!")
