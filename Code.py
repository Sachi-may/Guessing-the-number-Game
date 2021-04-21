import random

def guess_fun(a,b,the_number):
    num_guess =1
    user_guess = int(input(f"ENTER your guess between {a} and {b}\n"))
    while user_guess!=the_number:
        if user_guess<the_number:
            print("Enter bigger number")
            user_guess = int(input())
            num_guess+=1
        else:
            print("Enter smaller number")
            user_guess = int(input())
            num_guess+=1

    print(f"Your guess is correct,you took {num_guess} times to guess")
    return num_guess


if __name__ == '__main__':
    print("This is a number guessing game between two people")
    a=int(input("ENTER the lower limit\n"))
    b=int(input("ENTER the upper limit\n"))
    the_number1=random.randint(a,b)
    print("Players one Turn,play")
    g1=guess_fun(a,b,the_number1)
    print("Player two turn,play")
    the_number2=random.randint(a,b)
    g2=guess_fun(a,b,the_number2)

    if g1<g2:
        print(f"Player 1 took {g1} guesses and player 2 took {g2} guesses\n PLAYER ONE WON")
    elif g1>g2:
        print(f"Player 1 took {g1} guesses and player 2 took {g2} guesses\n PLAYER TWO WON")
    else:
        print(f"Player 1 took {g1} guesses and player 2 took {g2} guesses\n MATCH TIED")

    print(f"Player one number was {the_number1} and player two's number was {the_number2}")





