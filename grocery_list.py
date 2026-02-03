# Variables
user_choice = 'c'
grand_total = 0.0
item_total = 0.0
total_items = 0

#List
grocery_history = []

# Dictonary with pairs
grocery_item = {'name':'','number':'','price':''}

# A 'while-loop' repeats until user choice is inputed
while user_choice == 'c' :
    # Prompt the user to enter the item name.
    print("Item name:")
    # Accept the item name from the user.
    grocery_item['name'] = input()

    # Prompt the user to enter the quantity.
    print("Quantity purchased:")
    # Accept the quantity from the user.
    grocery_item['number'] = input()

    # Prompt the user to enter the price of per item.
    print("Price per item:")
    # Accept the price from the user.
    grocery_item['price'] = input()
    # Append item to grocery_history list
    grocery_history.append(grocery_item.copy())

    # Prompt the user for input
    print("Would you like to enter another item?")
    print("Type 'c' for continue or 'q' to quit:")
    user_choice = input()
   
    total_items+=1

# A 'for-loop' to display the items. 
# used index of i
for i in range(0,total_items):
    item_total = int(grocery_history[i]['number'])*float(grocery_history[i]['price'])#stores grocery_history as an integer for the quantity and as a float for the price in range of i for the item_total
    print(grocery_history[i]['number'] + " " + grocery_history[i]['name']+"@ $" + grocery_history[i]['price'] +" ea "+"$"+str(item_total))
    grand_total += item_total #grand_total is added with the item_total
   
print("Grand total: $%.2f" % (grand_total)) #outputs the grandtotal with 2 decimal places