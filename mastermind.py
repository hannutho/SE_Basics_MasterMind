from random import randrange

legit_numbers = [1,2,3,4,5,6]

def create_combination():
    random_combination = [str(randrange(1,7)) for x in range(4)]
    return "".join(random_combination)

def validate_code(input_guess):
    code = [int(x) for x in input_guess]
    if(len(code) != 4):
        input_guess = validate_code(input("Code is invalid! Try again:"))
    elif(not all(x in legit_numbers for x in code)):
        input_guess = validate_code(input("Code is invalid! Try again:"))
    return input_guess

def describe_hints(code, guess):
    

def play_mastermind():

    print("Welcome to master mind! Your guess the code of the codemaker. To achieve this you have 12 trys. After each try the codemaker will give you hints.")

    trys = 12
    code = create_combination()

    while trys > 0:
        trys-=1
        guess = validate_code(input("Make a guess:"))
        if(guess == code):
            print("You won the game!!!!!!")
            return
        else:
            right_number, right_position = describe_hints(code,guess)
            print("Your guess is wrong! Try again! (Try left: {})".format(trys))
            print("Hints:")
            print("{} are the right number!".format(right_number))
            print("{} numbers are at the right position!".format(right_position))
        
    print("You ran out of trys. The codemaker beat you. The right code was '{}'. Good luck next time!".format(code))



play_mastermind()