# Resources available in the coffee machine
resources = {
    "water": 2000,  # in ml
    "milk": 1500,   # in ml
    "coffee": 500, # in grams
    "money" : 0
}

# Needed resources and prices of coffee types
menu = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "money": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "money": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "money": 3.0},
}

def viewmenu():
    for drink in menu:
        print(f"{drink}: A${menu[drink]["money"]}")

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
    """This is the money processing part. (Accepting money, refunding money etc...)"""
    #ask for money
    andruaters = int(input("How many andruaters do you have? "))
    andrimes = int(input("How many andrimes do you have? "))       #add error prevention system
    andrickles = int(input("How many andricks do you have? "))
    andrennies = int(input("How many andrennies do you have? "))
    moneyin = andruaters * 0.25 + andrimes * 0.10 + andrickles * 0.05 + andrennies * 0.01

#verify sufficient funds y/n
#if enough money
    if moneyin == menu[order]["money"]:
        resources["money"] += moneyin
        print("Transaction successful.")
        return 1
# if too much money
    if moneyin > menu[order]["money"]:
        resources["money"] += moneyin
        print("Transaction successful.")
        print(f"You have A${round(moneyin - menu[order]['money'], 2)} of change.") #return money, rounded to 2dp
        resources["money"] -= moneyin - menu[order]['money']
        return 1
    else:  #if insufficient
        print("You don't have enough money!")
        #refund
        print(f"Refunding A${moneyin}.")
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
    global menu

    #ask for details
    name = input("What will you name your item?: ")
    water = int(input("How much water (ml) does it need?: "))
    milk = int(input("How much milk (ml) does it need?: ")) #optional: add try except
    coffee = int(input("How much coffee (g) does it need?: "))
    money = float(input("How much money does it cost (A$)?: "))

    # update menu
    menu.update({name: {"water" : water,  "milk" : milk, "coffee" : coffee, "money" : money}})
    print(f"You have successfully added {name}!")



######################################################
######################################################
# a loop while the coffee machine is on
#take the order
coffee_machine = "on"
while coffee_machine == "on":
    order = input("What would you like to order? (type 'menu' for to view the menu): ").lower()

# take off
    if order == "off":
        coffee_machine = "off"
        break
# view menu
    elif order == "menu":
        viewmenu()
# report
    elif order == 'report':
        print(*list(f"{item} = {value} " for item, value in resources.items()), sep="\n")

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
    #add & remove
    elif order == "add":
        add()
    elif order == "remove":
        removedobject = input("What would you like to remove?: ")
        remove(removedobject)





#order not existing (should be the last elif)
    elif order not in menu:
        print(f"Sorry, {order} does not exist!")









