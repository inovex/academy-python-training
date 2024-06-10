spells = {"charm": "Accio", "curse": "Avada Kedavra", "jinx": "Levicorpus"}
print(spells)

len(spells) # 3
spells.items() # returns dict_items([('charm', 'Accio'), ('curse', 'Avada Kedavra'), ('jinx', 'Levicorpus')])
spells.values() # returns dict_values(['Accio', 'Avada Kedavra', 'Levicorpus'])

for key, value in spells.items():
    print(key, value)