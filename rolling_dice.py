import random
def dice(action):
    if action == "roll":
        print(random.randint(1,6))
actions = True          
while actions:
    actions = input("you want to roll the dice?")
    dice(actions.lower)
    if actions.lower == "no":
        break



    