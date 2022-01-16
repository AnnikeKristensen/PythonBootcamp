"""week subject: user input and conditionals
project: build a calculator"""

operation = input("Would you like to add/subtract/multiply/divide? ").lower()
print("You chose {}".format(operation))

if operation == "subtract" or operation == "divide":
    print("Please keep in mind that the order of your numbers matter")

num1 = input("What is the first number?")
num2 = input("What is the second number?")

try:
    num1, num2 = float(num1), float(num2)
    if operation == "add":
        result = num1 + num2
        print("{} + {} = {}".format(num1, num2, result))
    elif operation == "subtract":
        result = num1 - num2
        print("{} - {} = {}".format(num1, num2, result))
    elif operation == "multiply":
        result = num1 * num2
        print("{} * {} = {}".format(num1, num2, result))
    elif operation == "divide":
        result = num1 / num2
        print("{} / {} = {}".format(num1, num2, result))
    else:
        print("Sorry but '{}' is not an option".format(operation))
except:
    print("Error: improper number used. Please try again.")
