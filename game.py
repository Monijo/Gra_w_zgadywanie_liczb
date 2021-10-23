from random import randint

def game_of_guessing_numbers():
    drawn_number = randint(1,100)
    guessing_number = 0
    while not(drawn_number == guessing_number):
    guessing_number = input("Guess the number: ")
        if not(isinstance(guessing_number, int)):
            print("It's not a number!")

