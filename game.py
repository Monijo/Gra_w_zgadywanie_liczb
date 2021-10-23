from random import randint

def game_of_guessing_numbers():
    '''Get number from user.
    Compare with drawn number.
    '''
    drawn_number = randint(1,100)
    guessing_number = 0
    while not(drawn_number == guessing_number):
        try:
            guessing_number = int(input("Guess the number: "))
            if guessing_number < drawn_number:
                print("To small!")
            elif guessing_number > drawn_number:
                print("To big!")
        except ValueError:
            print("It's not a number!")
    print("You win!")


if __name__ =="__main__":
    game_of_guessing_numbers()