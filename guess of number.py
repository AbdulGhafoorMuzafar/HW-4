import math
import random
x = 0
computer_number = random.randint(0,20)
while True :
    my_number = int(input("Enter your number :"))
    x+=1
    if (computer_number == my_number) :
        print ("You guess correct !!! " ,x)
        break
    if (computer_number < my_number ) :
        print("Your guess biger number !")
    if (computer_number > my_number ) :
        print("Your guess smaller number !")
