import random

x = random.randint(1,100);

count = 0
flag = 1
inp = int(input("Guess the number: "))

while(flag == 1):
    if(inp>x):
        print("Guess lower")
        count = count + 1
        flag = 1
        inp = int(input("Guess the number: "))

    elif(inp<x):
        print("Guess higher")
        count = count + 1
        flag = 1
        inp = int(input("Guess the number: "))

    else:
        print(f"Guessed in {count}")
        flag = 0
