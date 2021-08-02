# Following codes ensure that program accepts both uppercase and lowercase letters
def formatInput(textLine) :
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return textLine

# Price of single breakfast options are listed below
egg = 0.99
bacon = 0.49
sausage = 1.49
hash_brown = 1.19
toast = 0.79
coffee = 1.49
tea = 1.09

# Cost is defined to be zero
cost = 0

# Following codes determine the prices of breakfast options and cost
while (True):
    # Prompts user to then make their choice of food
    item_choice = input('Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea:\n')
    if item_choice == "q":
        break
    # If value entered is not valid; prompts user to enter a valid input
    # Item choices are formatted to ignore capitalization
    while formatInput(item_choice) not in ['small breakfast', 'regular breakfast', 'big breakfast', 'egg', 'bacon', 'sausage', 'hash brown', 'toast', 'coffee', 'tea']:
        item_choice = input('Error: Please enter a valid value:')
# Code will prompt user to select quantity of breakfast foods
    item_quantity = input('Enter quantity:')
    # To ensure that the number is numeric
    while not item_quantity.isnumeric():
        item_quantity = input('Please enter an integer value (ie. 2 as opposed to two.')
    # If and else statement are used to calculate what is ordered by the user
    if item_choice == "egg":
        cost = cost + (int(item_quantity) * 0.99)
    elif item_choice == "bacon":
        cost = cost + (int(item_quantity) * 0.49)
    elif item_choice == "sausage":
        cost = cost + (int(item_quantity) * 1.49)
    elif item_choice == "hash brown":
        cost = cost + (int(item_quantity) * 1.19)
    elif item_choice == "toast":
        cost = cost + (int(item_quantity) * 0.79)
    elif item_choice == "coffee":
        cost = cost + (int(item_quantity) * 1.49)
    elif item_choice == "tea":
        cost = cost + (int(item_quantity) * 1.09)
    elif item_choice == "small breakfast":
        cost = cost + ((0.99 + 1.19 + 1.58 + 0.98 + 1.49) * int(item_quantity))
    elif item_choice == "regular breakfast":
        cost = cost + ((0.99 + 0.99 + 1.19 + 0.79 + 0.79 + 1.96 + 2.98) * int(item_quantity))
    elif item_choice == "big breakfast":
        cost = cost + ((0.99 + 0.99 + 0.99 + 1.19 + 1.19 + 3.16 + 2.94 + 4.47) * int(item_quantity))


# The total cost will then be calculated with tax
tax = cost * 0.13
total_cost = cost + tax


# Final prices are formatted to two decimal points and printed
print('Cost: {:.2f}' .format(cost))
print('Tax: {:.2f}' .format(tax))
print('Total: {:.2f}'.format(total_cost))
