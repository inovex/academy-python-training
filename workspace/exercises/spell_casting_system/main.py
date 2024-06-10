from magician import Magician

harry_potter = Magician("Harry Potter", spell_list=["lumos", "accio"])
ron_weasley = Magician("Ron Weasly", spell_list=["lumos"])
hermione_granger = Magician("Hermione Granger", spell_list=["lumos", "accio", "expelliarmus"])

all_spells = ["expelliarmus", "accio", "lumos", "petrificus totalus", "wingardium leviosa"]
magicians = [harry_potter, ron_weasley, hermione_granger]

# Using a control flow structure of your choice, iterate over the list of magicians and the following list of spells.
# # If the magicians can cast the spell, have them cast it. Otherwise, have them learn the spell
for magician in magicians:
    for spell in all_spells:
        if spell in magician.spell_list:
            magician.cast_spell(spell)
        else:
            magician.learn_spell(spell)

print("\n\n")

# Print the list of spells Hermione Granger knows.
for spell in hermione_granger.spell_list:
    hermione_granger.cast_spell(spell)


def vowel_count(s: str) -> int:
    return sum([s.lower().count(x) for x in "aeiou"])

print("\n\n")

# Print all spells Harry Potter knows that contain at least 4 vowels.
for spell in [ s for s in harry_potter.spell_list if vowel_count(s) >= 4 ]:
    print(spell)