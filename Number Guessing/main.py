from art import logo
import random

def guessing_game():

    print(logo)
    rand = random.randint(0, 100)

    game_level = input("Choose the difficulty level 'easy' or 'hard': ")

    chances = 0

    if game_level == "easy":
        chances = 10
    elif game_level == "hard":
        chances = 5
    else:
        print("You selected the wrong option")


    while chances != 0:
        print(f"You have {chances} attempt left")
        print("\n"*2)
        user_guess = int(input("Enter No. to guess: "))

        if user_guess < rand:
            print("Too low")
        elif user_guess > rand:
            print("Too high")
        elif user_guess == rand:
            print(f"You got it, The number is {rand}")
            break
        else:
            print("Sorry you are out of life")
        
        chances -= 1
        if chances == 0:
            print("Sorry you are out of lives")
        
    want_continue = input("Do you want to continue ? say 'yes' or 'no' ")
    if want_continue == 'yes':
        print("\n"*20)

        guessing_game()
    else:
        print("thanks for playing")

guessing_game()