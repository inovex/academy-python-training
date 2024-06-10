Fred and George Weasley finally opened their joke shop _Weasley's Wizard Wheezes_. The shop works much better than they expected and the two brothers are gradually losing track of the shop inventory. To this end, they have implemented a basic inventory system but now need your help to optimize and complete it.

1. The `sell()` method does not take into account whether the quantity of an item to be sold is in stock. Create an exception class OutOfStockError and edit the `sell()` method so that it is raised when there are not enough items in stock.

2. The two brothers would like to log whenever an item is removed from or added to the inventory. Create a decorator `log_inventory` that takes a function as input and logs a message containing the function’s name before and after the function is called (the function’s name can be accessed by invoking function.__name__). Use the `log_inventory` decorator on the `add_item` and the `remove_item` methods of the _Inventory_ class.

3. Sometimes, customers are asking for articles in a specific price range. Create a new method `filter_items` in the _Inventory_ class that takes two arguments `min_price` and `max_price`.

4. In the `main.py`, Fred and George have already started creating an inventory.
  a. Use the `find_item` method twice to sell 33 pieces of Weasleys’ Wildfire
_Whiz-bangs_ and 7 pieces of Loonar Loop Luminators. Store the total amount of the items in a variable cost and print the price. To catch OutOfStockErrors, wrap a try ... except clause around your function calls.
  b. Filter items that cost 10 Galleons max. Use a list comprehension to create a list of tuples `[(item.name, item.price),...]`. Print the list