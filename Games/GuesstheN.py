import random

# This module implements pseudo-random number generators for various distributions.

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess == 0 : print(f"Please enter a number between 1 and {x}: ")
        else:
            if guess < random_number:
                print("Sorry, Guess again. Too low")
            elif guess > random_number:
                print("Sorry, guess Too high.")

    print(f"Well Done!, You have guessed the number {random_number}. Congratulations!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (c)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low =  guess + 1 


    print(f"Yaaha! I guess it right {guess}")      

computer_guess(10)

computer_guess(5)   
