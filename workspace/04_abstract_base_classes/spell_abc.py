from abc import ABC, abstractmethod

class Spell(ABC):
    def __init__(self, name: str, incantation: str, effect: str):
        self.name = name
        self.incantation = incantation
        self.effect = effect

    @abstractmethod
    def defining_feature(self):
        pass

class Charm(Spell):
    pass 

class Jinx(Spell):
    def defining_feature(self) -> str:
        return ("Minor dark magic. A spell whose effects are irritating but amusing.")

# Let's say defining_feature is not implemented in the Charm class
# Then, the statement below will throw an error
# accio = Charm("summoning_charm", "Accio", "Makes objects fly")

class Charm(Spell): 
    def defining_feature(self) -> str:
        return ("Alteration of the object's inherent qualities, "
                "that is, its behaviour and capabilities")

accio = Charm("summoning_charm", "Accio", "Makes objects fly")
