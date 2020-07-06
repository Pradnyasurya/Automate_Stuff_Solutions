import random

print("I'm thinking of a number between 1 to 20")
x = random.randint(1,20)

for i in range(1,10):

    print("Take a guess...")

    y = int(input())

   
    if y < x:
        print("Your guess is too low!")
    elif y > x: 
        print("Your guess is too high!")
    else:
        break

if y == x:
    print("Good Job! You guessed my number in", i ,"attempts!")

else: 
    print("Nope.. My guess was",x)
        