class Magician:

    def __init__(self, name: str, spell_list: list = []):
        self.name = name
        self.spell_list = spell_list

    def cast_spell(self, spell_name: str):
        if spell_name in self.spell_list:
            print(f"{self.name} casted {spell_name}")
        else:
            print(f"{self.name} does not know how to cast {spell_name}")

    def learn_spell(self, spell_name: str):
        if spell_name in self.spell_list:
            return False
        else:
            self.spell_list.append(spell_name)
            return True
