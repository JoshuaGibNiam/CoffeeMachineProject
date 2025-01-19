# Resources available in the coffee machine
resources = {
    "water": 500,  # in ml
    "milk": 300,   # in ml
    "coffee": 100, # in grams
    "money" : 0
}

# Needed resources and prices of coffee types
menu = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "money": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "money": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "money": 3.0},
}

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

# a loop while the coffee machine is on
#take the order
coffee_machine = "on"
while coffee_machine == "on":
    order = input("What would you like to order?(espresso: A$1.50 / latte: A$2.50 /"
"cappuccino: A$3.00): ").lower()

# take off
    if order == "off":
        coffee_machine = "off"
        break
# report
    elif order == 'report':
        print(*list(f"{item} = {value} " for item, value in resources.items()), sep="\n")

#get a drink
    elif order in menu:
        if order == "espresso":
            sufficient = checkresources("espresso")
        elif order == "latte":
            sufficient = checkresources("latte")
        elif order == "cappuccino":
            sufficient = checkresources("cappuccino")

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








