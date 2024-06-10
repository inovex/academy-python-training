

houses = ("Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff")
#houses[1] = "Is the tuple really immutable?" # TypeError: 'tuple' object does not support item assignment

print(houses[2]) # "Slytherin"
print(houses[1:3]) # ('Ravenclaw', 'Slytherin')

my_tuple = (1, 2, 3, 4, 5)
len(my_tuple) # 5
max(my_tuple) # 5
max(houses) # 
min(my_tuple) # 1
print(my_tuple.index(4)) # 3

print(max(houses))
