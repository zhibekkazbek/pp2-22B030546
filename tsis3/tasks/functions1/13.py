import random

def guess_number():
    print("Hello! What is your name?")
    name = input()
    print("Well, {}. I am thinking of a number between 1 and 20.".format(name))
    number = random.randint(1, 20)
    guess = 0
    attempts = 0
    while guess != number:
        print("Take a guess.")
        guess = int(input())
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        attempts += 1
    print("Good job, {}! You guessed my number in {} guesses!".format(name, attempts))
    
guess_number()