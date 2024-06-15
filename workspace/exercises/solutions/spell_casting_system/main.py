from magician import Magician


def main():
    # create list of magicians
    magicians = [
        Magician("Harry Potter", ["lumos", "accio"]),
        Magician("Ron Weasley", ["lumos"]),
        Magician("Hermione Granger", ["lumos", "accio", "expelliarmus"])
    ]

    spells = ["expelliarmus", "accio", "lumos",
              "petrificus totalus", "wingardium leviosa"]

    # let magicians cast known and learn new spells
    for magician in magicians:
        for spell in spells:
            if spell in magician.spell_list:
                magician.cast_spell(spell)
            else:
                magician.learn_spell(spell)

    # print Hermione Granger's spell list
    print("Hermione Granger knows the following spells: ",
          magicians[-1].spell_list)


if __name__ == "__main__":
    main()
