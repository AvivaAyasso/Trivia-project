#------------------------
def new_game():
    def new_game():

        guesses = []
        correct_guesses = 0
        question_num = 1

        for key in questions:
            print("-------------------------")
            print(key)
            for i in options[question_num - 1]:
                print(i)
            guess = input("Enter (A, B, C, or D): ")
            guess = guess.upper()
            guesses.append(guess)

            correct_guesses += check_answer(questions.get(key), guess)


#------------------------
def check_answer():
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")


#------------------------
def display_score():
    pass
#------------------------
def play_again():
    def play_again():

        response = input("Do you want to play again? (yes or no): ")
        response = response.upper()

        if response == "YES":
            return True
        else:
            return False

