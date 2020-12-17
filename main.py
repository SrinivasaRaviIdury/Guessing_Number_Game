import art
import random
print(art.logo)

print("Welcome to the number guessing game")
print("I'm thinking a number between 1 and 100 ")
number = random.randint(1,100)
level = input("choose your difficulty level type 'easy' or 'difficult': ").lower()
if level == "easy":
    attempts = 10
else:
    attempts = 5
def compare():
    if number > user_num:
        print(f"Your number {user_num}, Is too low than number")
        return 0
    elif number < user_num:
        print(f"Your number {user_num}, Is too high than number")
        return 0
    else:
        return 1

while attempts:
    user_num=int(input("Guess a number: "))
    res=compare()
    if res:
        print(f"You Guessed The Number: {number}! Congrats")
        break
    attempts -= 1
    if attempts == 0:
        print("Your chances are over You Lost!")
 
print('Good Bye!')
