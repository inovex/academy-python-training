from wizarding_item import WizardingItem

def log_inventory(func):
    def inner(*args, **kwargs):
        print(f"<{func.__name__}>")
        res = func(*args, **kwargs)
        print(f"<{func.__name__}/>")
        return res
    return inner

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

    def filter_items(self, min_price, max_price):
        for item in self.items:
            if item.price >= min_price and item.price <= max_price:
                yield item

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
