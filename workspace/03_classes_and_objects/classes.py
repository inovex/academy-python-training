class Spell:
    class_name = "Spell"
    def __init__(self, name: str, incantation: str, effect: str, spell_type: str):
        self.name = name
        self.incantation = incantation
        self.effect = effect
        self._type = spell_type
        self.__private = True
    
    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def accio(cls):
        return cls("accio", "Accio", "Makes objects fly", "Charm")

accio = Spell("accio", "Accio", "Makes objects fly", "Charm")
print(accio.incantation) # Accio
print(accio.class_name) # Spell
print(Spell.class_name) # Spell
# print(Spell.incantation) # AttributeError: type object 'Spell' has no attribute 'incantation'

print(accio._type) # Charm
# print(accio.__private) # AttributeError: 'Spell' object has no attribute '__private'
print(accio) # <__main__.Spell object at 0x7f277971ba00>

accio.cast() # Accio!
accio = Spell.accio()
print(accio.incantation) # Accio!

class Spell:
    class_name = "Spell"
    def __init__(self, name: str, incantation: str, effect: str):
        self.name = name
        self.incantation = incantation
        self.effect = effect

class Charm(Spell):
    def defining_feature(self):
        return ("Alteration of the object's inherent qualities, "
                "that is, its behaviour and capabilities")

class Jinx(Spell):
    def defining_feature(self):
        return ("Minor dark magic. A spell whose effects are irritating but amusing, "
                "almost playful and of minor inconvenience to the target")

accio = Charm("summoning_charm", "Accio", "Makes objects fly")
levi = Jinx("dangling_jinx", "Levicorpus", "Causes the victim to be hoisted into the air by their ankle")

for spell in [accio, levi]:
    print(spell.defining_feature())