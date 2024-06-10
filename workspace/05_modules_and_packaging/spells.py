class Spell:
    def __init__(self, name: str, incantation: str, effect: str):
        self.name = name
        self.incantation = incantation
        self.effect = effect
    
    def cast(self):
        print(f"{self.incantation}!")