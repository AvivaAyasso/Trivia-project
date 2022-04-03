from utils import *


questions = {
    "What is the correct file extention for python files?": "B",
    "Which operators is used to multiply?": "B",
    "Which collection is ordered, changeable, and allows duplicate numbers?": "A",
}

options = [
    ["A. '.pyt'", "B. '.py'", "C. '.pt'", "D. '.pyth'"],
    ["A. #", "B. *", "C. +", "D. x"],
    ["A. List", "B. Dictionary", "C. Tuple", "D. Set"]
]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")