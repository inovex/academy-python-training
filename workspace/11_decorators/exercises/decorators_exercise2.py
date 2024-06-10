# # Decorators - Exercise 2

# - Create a class Magician with two attributes: name and magical_energy
# - Create a decorator subtract_magical_energy that takes an argument energy_subtracted: int
# - Create a function cast_spell that takes two arguments: magician and spell_name and applies the subtract_magical_energy decorator on it
#       - set energy_subtracted=20
#       - the function should print the name of the magician casting the spell and the name of the spell that is casted
# - If the magician does not have enough energy to cast the spell, the function should return an error message
# - Create an instance of Magician who has a magical_energy of 30, 
# - Call the cast_spell function twice and check if the magical energy is subtracted correctly from your Magician instance's magical_energy field