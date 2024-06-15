from wizarding_item import WizardingItem


def log_inventory(function):
    def wrapper(*args, **kwargs):
        print(f"{function.__name__} called")
        result = function(*args, **kwargs)
        print(f"{function.__name__} completed")
        return result
    return wrapper


class Inventory:

    def __init__(self):
        self.items = []

    @log_inventory
    def add_item(self, item: WizardingItem):
        self.items.append(item)

    @log_inventory
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def item_report(self):
        report = "Weasley's Wizard Wheezes Item Report\n" + "-" * 20 + "\n"
        items = (
            f"Name: {item.name}\nPrice: {item.price} Galleons\nStock: {item.stock}\n\n" for item in self.items)
        for item in items:
            report += item
        return report

    def filter_items(self, min_price, max_price):
        return [item for item in self.items if min_price <= item.price <= max_price]
