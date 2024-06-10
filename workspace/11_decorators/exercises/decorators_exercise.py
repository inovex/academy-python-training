# # Decorators Exercises
# 
# 1. Write a decorator spell_check that takes a function as input and checks the 
#    correctness of the spell (see list of known spells below) before executing it
#       - return an error message if the incantation is not known
#       - define a function cast_spell that takes an input spell_name: str and prints the spell; 
#         make sure to use the spell_check decorator
#       - execute the function twice: once with a known, once with an unknown spell

known_spells = ["Expecto Patronum", "Avada Kedavra", "Expelliarmus", "Accio", "Lumos"]