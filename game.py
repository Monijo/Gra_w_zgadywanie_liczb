from random import randint

def game_of_guessing_numbers():
    drawn_number = randint(1,100)
    guessing_number = 0
    while not(drawn_number == guessing_number):
        try:
            guessing_number = int(input("Guess the number: "))
        except ValueError:
            print("It's not a number!")



game_of_guessing_numbers()