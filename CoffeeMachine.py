# Resources available in the coffee machine
resources = {
    "water": 500,  # in ml
    "milk": 300,   # in ml
    "coffee": 100, # in grams
}

# Needed resources and prices of coffee types
menu = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0},
}

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
        pass

#get a drink
    elif order in menu:
        pass


