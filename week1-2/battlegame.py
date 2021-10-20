"""
Battle Game
"""

# Game Character
wizard = 'Wizard'
elf = 'Elf'
human = 'Human'

# Character Health Points
wizard_hp = 70
elf_hp = 100
human_hp = 150

# Your health and attack
my_hp = 0
my_damage = 0

# Character Damage
wizard_damage = 150
elf_damage = 100
human_damage = 20

# Dragon variable
dragon = 'Dragon'
dragon_hp = 300
dragon_damage = 50

# Character Selection
print("1)", wizard)
print("2)", elf)
print("3)", human)


while True:
    character = input("Choose your character:")
    print("You chose", character)
    if character == "1":
        character = 'Wizard'
        print(wizard)
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2":
        character = 'Elf'
        print(elf)
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3":
        character = 'Human'
        print(human)
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown Character")

print(character, my_hp, my_damage)

# Dragon Battle
while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    if dragon_hp <= 0:
        print("The Dragon has lost the battle.")
        break
    my_hp = my_hp - dragon_damage
    print(character, my_hp, my_damage)
    if my_hp <= 0:
        print("The", character, "has lost the battle")
        break
