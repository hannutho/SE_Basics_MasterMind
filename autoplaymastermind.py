from random import randrange
from os import system

legit_numbers = [1,2,3,4,5,6]

def create_combination():
    random_combination = [str(randrange(1,7)) for x in range(4)]
    return "".join(random_combination)

def describe_hints(code, guess):
    right_number = 0
    right_position = 0
    temp_code = [x for x in code]
    
    for idx,x in enumerate(guess):
        if x == code[idx]:
            right_position+=1
        elif x in temp_code:
            right_number+=1

    return right_number, right_position


def autoplay_mastermind():

    trys = 12
    code = create_combination()
    tried_codes = []

    while trys > 0:
        trys-=1

        guess = validate_code(input("Make a guess:"),tried_codes)
        tried_codes.append(guess)

        if(guess == code):
            print("You won the game! The code was '{}'. Congratulations!".format(code))
            return
        else:
            system("clear")
            right_number, right_position = describe_hints(code,guess)
            print("Your guess '{}' is wrong! Try again! (Trys left: {})".format(guess,trys))
            print("Hints:")
            print("     {} of your numbers are inside the code!".format(right_number))
            print("     {} of your numbers are at the right position!".format(right_position))

    system("clear")
    print("You ran out of trys. The codemaker beat you. The right code was '{}'. Good luck next time!".format(code))


play_mastermind()
