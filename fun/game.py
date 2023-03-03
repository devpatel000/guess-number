import random

num = random.randint(1,99)
guess = None

for i in range(5):
    print("chance", i+1)
    guess = int(input("guess the number: "))
    
    if guess == num:
        print("you won...!")
        break
    if guess < num:
        print("number is less")
    if guess > num:
        print("number is greater")

    