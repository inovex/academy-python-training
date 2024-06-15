from inventory import Inventory
from wizarding_item import WizardingItem, OutOfStockError


def main():
    # initialize the inventory
    inventory = Inventory()

    # Add items to the inventory
    inventory.add_item(WizardingItem("Weasleys' Wildfire Whiz-bangs", 10, 200))
    inventory.add_item(WizardingItem("Loonar Loop Luminators", 15, 22))
    inventory.add_item(WizardingItem("Skiving Snackbox", 8, 100))

    # sell items
    try:
        cost = inventory.find_item("Weasleys' Wildfire Whiz-bangs").sell(33)
        cost += inventory.find_item("Loonar Loop Luminators").sell(7)
        print(
            f"The cost of selling 33 of Weasleys' Wildfire Whiz-bangs and 7 Loonar Loop Luminators is {cost} Galleons.")
    except OutOfStockError as e:
        print(e)

    # Generate item report
    print(inventory.item_report())

    # Filter items by price
    cheap_items = inventory.filter_items(0, 10)
    print([(item.name, item.price) for item in cheap_items])

if __name__ == "__main__":
    main()
