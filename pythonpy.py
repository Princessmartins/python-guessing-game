#the guessing game
import random

num=random.randint(0,10)
attempt=5
play_again = "Yes"
while play_again== "Yes":

    while attempt>=0:
        number= int(input("Enter any Number: "))

        if number==num:
            print("You are correct!")
            print("\n")
            run_again=input ("Enter Yes to play again: ")
            if run_again != "Yes":
                print("Play again!")
        else:
            print("You are wrong!")
            print("Try Again!")
            print("\n")
            print('Remaining attempts: {}'.format(attempt))
            print("\n")
            attempt-=1
            continue
            print("\n")
    print("You lost the Game,dumbass!")

    play_again = input("Game Over, Enter yes to play again: ")
    print("\n")
    if play_again == "Yes":
        attempt=5
    else:
        print("Closing Game...")

