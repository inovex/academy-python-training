from functools import wraps

class Magician:
  def __init__(self, name, magical_energy):
    self.name = name
    self.magical_energy = magical_energy

def subtract_magical_energy(energy_subtracted: int):
  def decorator(function):
    @wraps(function)
    def wrapper(magician, spell_name):
      if magician.magical_energy - energy_subtracted < 0:
        print(f"{magician.name} does not have enough magical energy to cast a {spell_name} spell")
      else:
        magician.magical_energy -= energy_subtracted
        return function(magician, spell_name)
    return wrapper
  return decorator

@subtract_magical_energy(energy_subtracted=20)
def cast_spell(magician, spell_name):
    print(f"{magician.name} casted the {spell_name} spell")

harry_potter = Magician("Harry Potter", 30)
cast_spell(harry_potter, "Expecto Patronus")
cast_spell(harry_potter, "Expelliarmus")
