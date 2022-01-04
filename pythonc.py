#from random import randint
#repeat = True
#while repeat:
 #   print("You rolled",randint(1,6))
  #  print("Do you want to roll again?")
   # repeat = ("y" or "yes") in input().lower()
actions = True;
          
while actions:
    actionss = int(input("wanna roll the dice?"))
    print(actionss)
    print(type(actionss))

    if actionss == 0:
        break
    