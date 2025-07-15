from inventory import Inventory
from wizarding_item import WizardingItem, OutOfStockError

# initialize the inventory
inventory = Inventory()

# Add items to the inventory
inventory.add_item(WizardingItem("Weasleys' Wildfire Whiz-bangs", 10, 200))
inventory.add_item(WizardingItem("Loonar Loop Luminators", 15, 22))
inventory.add_item(WizardingItem("Skiving Snackbox", 8, 100))

print("\n\n")

### TODO ###
# Sell items
# Use the find_item method twice to sell 33 pieces of Weasleys’ Wildfire Whiz-bangs
# and 7 pieces of Loonar Loop Luminators.
# Store the total amount of the items in a variable cost and print the price.
# To catch OutOfStockErrors, wrap a try … except clause around your function calls.


# Generate and print item report
for item in inventory.item_report():
    print(item)

# TODO: Filter items that cost 10 Galleons max. Use a list comprehension to create a list of tuples [(item.name, item.price),...]. Print the list
