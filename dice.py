import random

while True :
    dice = random.randint(1,6)
    print(dice)
    if dice == 6 :
        dice = random.randint(1,6)
        print("second time dice roll : ",dice)
        break
    else :
        break