from wizarding_item import WizardingItem

def log_inventory(func):
   # TODO: implement this decorator
   # it should log a message containing the function's name before
   # and after the function is called
   pass

class Inventory:

    def __init__(self):
        self.items = []

    def add_item(self, item: WizardingItem):
        self.items.append(item)

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def filter_items(self, min_price, max_price):
        # TODO: filter the items
        pass

    def item_report(self):
        print("Weasley's Wildfire Whiz-bangs")
        print("-------------------------")
        for item in self.items:
            item_str = f"""
                Name: Weasley's Wildfire Whiz-bangs
                Price: {item.price}
                Stock: {item.stock}
            """
            yield item_str
