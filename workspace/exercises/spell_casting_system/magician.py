
class Magician:
    
    def __init__(self, name: str, spell_list: list[str]):
        self.name = name
        self.spell_list = spell_list
        
    def cast_spell(self, spell_name: str):
       if spell_name in self.spell_list:
           print(f"{self.name} spells {spell_name}")
       else:
           print(f"{self.name} cannot cast the {spell_name}")
           
    def learn_spell(self, spell_name: str):
        if not spell_name in self.spell_list:
            self.spell_list.append(spell_name)
            return True
        else:
            return False
        
    