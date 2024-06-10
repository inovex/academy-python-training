basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket) # {'orange', 'banana', 'pear', 'apple'}
# basket.add([1, 2, 3]) # TypeError: unhashable type: 'list'

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
'orange' in basket # True
'kiwi' in basket # False  

charm = set("Accio")
curse = set("Avada Kedavra")
print(charm) # {'c', 'A', 'o', 'i'}
print(curse) # {'d', 'K', 'v', 'r', 'e', ' ', 'a', 'A'}
print(charm - curse) # {'c', 'i', 'o'}
print(charm & curse) # {'A'}

for item in basket:
    print(item)