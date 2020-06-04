from random import randrange
from os import system
from itertools import product

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


def choose_optimized_guess(current_guess_space,code,tried_codes):
    new_space_sizes = []

    allCodes = ["".join([str(y) for y in x]) for x in product(range(1,7), repeat=4)]

    last_guess = tried_codes[-1]
    for guess in allCodes:
        print(guess)
        


def autoplay_mastermind():

    tried_codes = []

    trys = 1

    code = create_combination()
    print("Code: " + code)

    allCodes = ["".join([str(y) for y in x]) for x in product(range(1,7), repeat=4)]

    while trys > 0:
        trys -= 1

        #Pick optimized new code
        guess = allCodes[randrange(len(allCodes))]
        tried_codes.append(guess)
        choose_optimized_guess(allCodes,code,tried_codes)


        #If win return
        if(guess == code):
            print("Game won in {} trys!".format(12-trys))
            print("Tried codes: {}".format(tried_codes))
            return

        #Remove all codes that dont give same hints in reference to current guess as current guess does in reference to the code
        tmp = []
        for x in allCodes:
            if describe_hints(x,guess) == describe_hints(code,guess):
                if(x != guess):
                    tmp.append(x)
        allCodes = tmp

autoplay_mastermind()
