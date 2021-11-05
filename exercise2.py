import random
number = random.randint(1,50)
guess=0
while guess != number :
    guess=int(input("enter a number:"))
    if guess > number:
        print("please decrease your number")
    elif guess < number :
        print("please increase your number")
    else :
        print("your number is correct congrats !!")
