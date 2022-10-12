from curses.ascii import isdigit
from operator import truediv


user_prompt = True

while user_prompt:
    age = input("Please enter your age: ")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please enter digits only, no decimals or aplha characters")
print ("Your age is: ", age)