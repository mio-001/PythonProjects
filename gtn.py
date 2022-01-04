import random

secretNumber = random.randint(1,100)


while True:
    yourAnswer = int(input("Enter a number between 0 and 100:"))
    if secretNumber == yourAnswer:
        print("your answer is correct!")
        break
    elif secretNumber > yourAnswer:
        print("your answer is smalller than the secret number")
        print("when divided by 2 the number is:"+str(secretNumber/2))
    elif secretNumber < yourAnswer:
        print("your answer is bigger than the secret number")
        print("when multipled by 3 the number is:"+str(secretNumber*3))