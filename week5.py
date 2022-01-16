"""Theme: functions
Project: Creating a shopping program """

from IPython.display import clear_output

cart = [] #global scope

def addItem(item):
    clear_output()
    cart.append(item)
    print("{} has been added".format(item))

def removeItem(item):
    clear_output()
    try:
        cart.remove(item)
        print("{} has been removed".format(item))
    except:
        print("Sorry we could not remove that item")

def showCart():
    clear_output()
    print("Here is your cart:")
    cartsize = len(cart)
    if cartsize != 0:
        for item in cart:
            print("- {}".format(item))
    else:
        print("Your cart is empty")

def clearCart():
    clear_output()
    cart.clear()
    print("Your cart is empty")

def main():
    done = False
    while not done:
        ans = input("quit/add/remove/show/clear".lower())
        clear_output()

        if ans == "quit":
            print("Thank you for using our program")
            showCart()
            done = True

        elif ans == "add":
            theItem=input("What would you like to add?".title())
            addItem(theItem)

        elif ans == "remove":
            item= input("What would you like to remove?".title())
            removeItem(item)

        elif ans == "show":
            showCart()

        elif ans == "clear":
            clearCart()

        else:
            print("Sorry, {} was not an option".format(ans))

main()


