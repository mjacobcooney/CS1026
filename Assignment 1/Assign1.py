##
#This program takes user input and computes the price for a breakfast at the Good Morning America! restaurant.
#
# Price list for menu items.
EGG = .99
BACON = .49
SAUSAGE = 1.49
HASH_BROWN = 1.19
TOAST = .79
COFFEE = 1.09
TEA = .89
SMALL_BREAKFAST = EGG + HASH_BROWN + TOAST * 2 + BACON * 2 + SAUSAGE
REGULAR_BREAKFAST = EGG * 2 + HASH_BROWN + TOAST * 2 + BACON * 4 + SAUSAGE * 2
BIG_BREAKFAST = EGG * 3 + HASH_BROWN * 2 + TOAST * 4 + BACON * 6 + SAUSAGE * 3

#This dictionary store string : float pairs. This is used to get the floating point price of the menu item.
menuPrices =  {"egg": EGG,
            "bacon": BACON,
            "sausage": SAUSAGE,
            "hash brown": HASH_BROWN,
            "toast": TOAST,
            "coffee": COFFEE,
            "tea": TEA,
            "small breakfast": SMALL_BREAKFAST,
               "regular breakfast": REGULAR_BREAKFAST,
               "big breakfast": BIG_BREAKFAST}

#This array contains all the valid input string names for breakfast items.
validMenuItems = ["small breakfast","regular breakfast", "big breakfast", "egg", "bacon", "sausage", "hash brown", "toast", "coffee", "tea"]
madeSelection = False
quantity = 0
selection = ''

#given code to format inputs
def formatInput(textLine) :
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return textLine

#Orders is a dictionary which store string:int pair. The int corresponds to the quantity of items ordered.
orders = {}
while not madeSelection:
    selection = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea:\n")
    if selection is not "q":
        selection = formatInput(selection)
    if selection is 'q':
        madeSelection = True
        print("Thank you for dining with Good Morning America!\n")
    elif validMenuItems.__contains__(selection):
        #if the word is valid
        quantity = input("Enter quantity\n")
        while not quantity.isnumeric(): #ensure input for quantity is numeric
            quantity = input("Please select a numerical input\n")
        #add menu item and quantity to orders dict
        orders[selection] = quantity
    else:
        print("Please select a valid input")
total = 0.0
print(orders)
#loop through all the orders and add to total
if len(orders) > 0:
    for order in orders:
    #This function is Price * Quantity. Price is the value of menuPrices dict with key value order name. Quantity is the value of the orders dict for the order name.
    #Quantity needed to be cast to int because it was returning string value.
        total = total + (menuPrices[order] * int(orders[order]))

print("Cost:  ", round(total, 2)) #pre tax rounded
print("Tax:   ", round(total * 0.13, 2)) #tax amount rounded
print("Total: ", round(total * 1.13, 2)) # pre tax + tax amount rounded







