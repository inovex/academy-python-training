## Spell Casting System

1. Create a file named `magician.py` and define a class _Magician_ with the following attributes
  - name
  - spell_list
  - Choose the datatypes yourself! Think about the advantages and disadvantages of the different possibilities

2. Define a function `cast_spell` in the Magician class that takes `spell_name (str)` as an argument. If the spell is in the magician’s `spell_list`, the method should print the spell and the magician’s name. Otherwise, it should print that the magician cannot cast the spell.

3. Define a method `learn_spell` in the _Magician_ class that takes a `spell_name(str)` as an argument. If the spell is not already in the magician's spell list, the method should add it to the list and return True. If the spell is already in the magician's spell list, the method should return False.

4. Create a file name `main.py`. Import the `Magician` class and create a list of the following magicians.
  - Harry Potter, spells: lumos, accio
  - Ron Weasly, spells: lumos
  - Hermione Granger: lumos, accio, expalliarmus

5. Using a control flow structure of your choice, iterate over the list of magicians and the following list of spells. If the magicians can cast the spell, have them cast it. Otherwise, have them learn the spell:

```
spells = [‘expelliarmus’, ‘accio’, ‘lumos’, ‘petrificus totalus’, ‘wingardium leviosa’]
```

6. Print the list of spells Hermione Granger knows.

7. Print all spells Harry Potter knows that contain at least 4 vowels.

8. Execute `main.py`


