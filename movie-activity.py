# Movie Age ristrictions activity
# User enters their age and the program tells them if they can watch the movie

def main():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You can watch the 18+ movie")
    elif age >= 16:
        print("You can watch the 16+ movie")
    elif age >= 12:
        print ("You can watch the 12+ movie")
    elif age >= 15:
        print ("You can watch the 15+ movie")
    elif age >= 117:
        print ("Your age has to be under 117")
        main()
    else:
        print("Try Again")
        main()   