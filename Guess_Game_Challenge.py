# Let's use while loops to create a guessing game.
# The Challenge:
# Write a program that picks a random integer from 1 to 100, and has players guess the number. 
# The rules are:
# If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# On a player's first turn, if their guess is
# within 10 of the number, return "WARM!"
# further than 10 away from the number, return "COLD!"
# On all subsequent turns, if a guess is
# closer to the number than the previous guess return "WARMER!"
# farther from the number than the previous guess, return "COLDER!"
# When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
# You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!

# First, pick a random integer from 1 to 100 using the random module and assign it to a variable
# Note: random.randint(a,b) returns a random integer in range [a, b], including both end points.
import random
rand_num=random.randint(1,100)
prev_guess=[]
while True:
    guess_num=int(input("Guess a Number between 1 to 100:"))
    
    if guess_num<1 or guess_num>100:
        print("OUT OF BOUNDS")
        continue
    if rand_num==guess_num:
        prev_guess.append(guess_num)
        print(f"You guessed correctly in {len(prev_guess)} guesses!")
        break
    if len(prev_guess)==0:
        if abs(rand_num-guess_num)<=10:
            print("WARM!")
        else:
            print("COLD!")
    else:
        if abs(rand_num-guess_num)<abs(rand_num-prev_guess[-1]):
            print("Warmer!")
        else:
            print("Colder!")
    prev_guess.append(guess_num)