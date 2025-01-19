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
    global resources
    truefalse = False
    """check the resources if enough for each order"""
    for resource, value in menu[order].items():
        if value >= resources[resource]:
            truefalse = True
        else:
            return False

    if truefalse:
        return True



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
        else:
            print("Not enough resources.")





