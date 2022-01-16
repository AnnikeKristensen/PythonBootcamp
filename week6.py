"""Subject: Collection and files
Project: Creating a sample database"""

import csv
from IPython.display import clear_output

def registerUser():
    with open("users.csv",mode="a",newline="") as f:
        writer = csv.writer(f,delimiter = ",")
        print("To register, please enter your info:")
        email = input("Email: ")
        password = input("Password: ")
        password2 = input("Re-type password: ")
        clear_output()

        if password == password2:
            writer.writerow([email,password])
            print("You are now registered!")
        else:
            print("Something went wrong. Try again. ")

def loginUser():
    print("To login, please enter your info: ")
    email = input("Email: ")
    password = input("Password: ")
    clear_output()
    with open("users.csv",mode="r") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            if row == [email, password]:
                print("You are now logged in ")
                return True
    print("Something went wrong, try again.")
    return False

active = True
logged_in = False

while active:
    if logged_in:
        print("1. logout\n2. Quit")
        choice = input("What would you like to do?".lower())

        if choice == "logout":
            logged_in = False
            print("You are now logged out")

        if choice == "quit":
            active = False
            print("Thank you for using our software!")
    else:
        print("1. Login\n2. Register\n3.Quit")
        choice = input("What would you like to do?".lower())
        clear_output()

        if choice == "register" and logged_in == False:
            registerUser()

        elif choice == "login" and logged_in == False:
            logged_in = loginUser()

        elif choice == "quit":
            active = False
            print("Thank you for using our software!")

        elif choice == "logout" and logged_in == True:
            logged_in = False
            print("You are now logged out.")
        else:
            print("Sorry try again.")
