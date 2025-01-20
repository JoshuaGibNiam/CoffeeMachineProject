from datetime import datetime as dt



# Resources available in the coffee machine
resources = {
    "water": 2000,  # in ml
    "milk": 1500,   # in ml
    "coffee": 500, # in grams
    "money" : 0  #this is the profit made
}

# Needed resources and prices of coffee types
menu = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "money": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "money": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "money": 3.0},
}

def logtransaction(order, paid, change=0, cardnumber=0):
    """automatically log orders, used in processtransaction() function"""
    with open("log.txt", "a") as file:
        file.write(f"{order} ordered at {dt.now()} -- A${paid} fully paid -- Change: A${round(change, 2)} \n")
        if cardnumber == 0:
            file.write("Order above paid by cash.")
        else:
            file.write(f"Order above paid by card: **** **** **** {cardnumber[-4:]}.")

        file.write("\n")

def viewlog():
    """Allows admin to view transactions"""
    with open("log.txt", "r") as file:
        print(file.read())

def refill():
    """allows admin to refill resources """
    global resources #we need to modify the resources list
    for key in resources.keys():
        addedresource = 0
        if key == "money": #skip money
            continue
        while True:
            try:
                addedresource = int(input(f"How much {key} would you like to refill?: "))
                break
            except ValueError:
                print("Please enter a whole number.")
        resources.update({key: addedresource + resources[key]})

    print("Update Complete.")
    print(*list(f"{item} = {value} " for item, value in resources.items()), sep="\n")
    print("\n")

def printreciept(order, cardorcash, change=0, cardnumber=0):
    """Print reciepts (called in the transactionprocess function)"""

    reciept = (f"Order made at {dt.now()}: \n "           #time of order
    f"{order}----------------A${menu[order]['money']} \n" #order, order price
    f"Change: A${round(change, 2)} \n"                    #change
    f"Paid fully by {cardorcash} \n")                     #paid by card or cash

    print(reciept)
    if cardorcash == "card": #if user uses card, print card number
        print(f"**** **** **** {str(cardnumber[-4:])} \n")


def viewmenu():
    """allows the user to view menu"""
    print("\nToday's menu: ")
    print("-" * 20)
    for drink in menu:
        print(f"{drink}: A${menu[drink]["money"]}")
    print("\n")  # \n makes it more organised

def checkresources(order):
    truefalse = False
    """check the resources if enough for each order"""
    for resource, value in menu[order].items():
        if resource == "money": #skip the money part
            continue
        if value <= resources[resource]:
            truefalse = True
        else:
            return 0

    if truefalse:
        return 1


def processtransaction(order):
    """This is the money processing part. (Accepting money, refunding money etc...)
    """
    #ask for money
    while True:
        cardorcash = input("Would you like to pay using card or cash?: ").lower() #add error prevention
        if cardorcash in ["card", "cash"]:
            break
        else:
            print("Please enter 'card' or 'cash'.")
    #cash option
    if cardorcash == "cash":
        while True:
            try:
                andruaters = int(input("How many andruaters do you have? "))
                andrimes = int(input("How many andrimes do you have? "))
                andrickles = int(input("How many andricks do you have? "))
                andrennies = int(input("How many andrennies do you have? "))
                break
            except ValueError:
                print("Try again.")
        #convert to A$
        moneyin = andruaters * 0.25 + andrimes * 0.10 + andrickles * 0.05 + andrennies * 0.01

#verify sufficient funds y/n
#if enough money
        if moneyin == menu[order]["money"]:
            resources["money"] += moneyin
            print("Transaction successful. \n")
            printreciept(order, cardorcash) #print reciept
            logtransaction(order, menu[order]["money"])
            return 1
# if too much money
        if moneyin > menu[order]["money"]:
            resources["money"] += moneyin
            print("Transaction successful.")
            print(f"You have A${round(moneyin - menu[order]['money'], 2)} of change. \n") #return money, rounded to 2dp
            resources["money"] -= moneyin - menu[order]['money']
            printreciept(order, cardorcash, change=moneyin - menu[order]['money'])
            logtransaction(order, menu[order]["money"], change=moneyin - menu[order]['money'])
            return 1
        else:  #if insufficient
            print("You don't have enough money!")
        #refund
            print(f"Refunding A${moneyin}. \n")
            return 0

    #card option
    elif cardorcash == "card":
        cardno = input("Enter card number (without spacing): ")
        while True:
            if cardno.isdigit() and len(cardno) == 16: #check if the credit card number is valid
                print("Transaction successful.")
                resources["money"] += menu[order]["money"]
                printreciept(order, cardorcash, cardnumber=cardno) #print reciept
                logtransaction(order, menu[order]["money"], cardnumber=cardno)
                return 1
            else: #if card number is invalid
                print("Invalid card number.")
                cardno = input("Enter card number without spacing (Or press [ENTER] to start over): ")
                if cardno == "":
                    return 0




def makecoffee(order):
    """Make a coffee of the user's choice"""
    #deduct resource
    for resource in resources:
        #check if resource is money first
        if resource == "money":
            continue
        resources[resource] -= menu[order][resource]
    print(f"Here is your {order}! Bon Appetit!")

def remove(name):
    """Allows user to remove a certain item from the menu"""
    global menu
    if name in menu:
        del menu[name]
        print(f"You have successfully removed {name}")
    else:
        print(f"{name} does not exist!")

def add():
    """Allows admin to add item"""
    global menu

    #ask for details
    name = input("What will you name your item?: ")
    while True:
        try:
            water = int(input("How much water (ml) does it need?: "))
            milk = int(input("How much milk (ml) does it need?: ")) #optional: add try except
            coffee = int(input("How much coffee (g) does it need?: "))
            money = float(input("How much money does it cost (A$)?: "))
            break
        except ValueError:
            print("Invalid input. Please enter again.")

    # update menu
    menu.update({name: {"water" : water,  "milk" : milk, "coffee" : coffee, "money" : money}})
    print(f"You have successfully added {name}!")



######################################################
######################################################
# a loop while the coffee machine is on
#take the order
coffee_machine = "on"
while coffee_machine == "on":
    viewmenu()
    order = input("What would you like to order?: ").lower()
    ###off option moved to admin orders below, disallowing customers to turn off the machine
# view menu
    if order == "menu":
        viewmenu()
# report also moved to admin controls
#get a drink
    elif order in menu:
        sufficient = checkresources(order)
        if sufficient:
            print("Sure!")
            sufficientfunds = processtransaction(order)
            if sufficientfunds == 0:
                continue  # next order
            else:
                print("Making Coffee.")
                makecoffee(order)
        else:
            print("Not enough resources.")

    elif order == "admin": #extra: allows admin to refill resources and do other stuff
        pwd = input("Enter your password: ") #enter admin password to confirm
        if pwd != "111222":
            print("Wrong password! Access denied.")
            continue
        else:
            adminorder = input("What would you like to do?: ") #add, remove, refill
            if adminorder == "add":
                add()
            elif adminorder == "remove":
                removedobject = input("What would you like to remove?: ")
                remove(removedobject)
            elif adminorder == "off":
                coffee_machine = "off"
                print("Powering off.")
                break
            elif adminorder == 'report':
                print(*list(f"{item} = {value} " for item, value in resources.items()), sep="\n")

            elif adminorder == "refill":
                refill()
            elif adminorder == "view":
                viewlog()
            else:
                print("Invalid input.")

#order not existing (should be the last elif)
    elif order not in menu:
        print(f"Sorry, {order} does not exist!")

print("Machine status: off")








