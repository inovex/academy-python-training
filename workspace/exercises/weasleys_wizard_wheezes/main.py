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
try:
    cost = inventory.find_item("Weasleys' Wildfire Whiz-bangs").sell(33)
    cost += inventory.find_item("Loonar Loop Luminators").sell(7)
    print(f"the total cost of the order is {cost}")
    
except OutOfStockError as e:
    print(e)
    
print("\n\n")
    
# Generate and print item report
for item in inventory.item_report():
    print(item)

# Filter items by price
cheap_items = [ (i.name, i.price) for i in inventory.filter_items(0, 10) ]
print(cheap_items)