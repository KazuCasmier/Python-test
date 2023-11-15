import random

print('%0s %20s' % ('Start', 'Quit'))
print('__________________________')
game_start = input('')

# Placeholder variables for the character stats
inventory = []
strength = 0
dex = 0
con = 0
cha = 0
intel = 0
wis = 0
# Randomizes the stats
for i in range(0, 6):
    if i == 0:
        strength += random.randint(1, 10)
    if i == 1:
        dex += random.randint(1, 10)
    if i == 2:
        con += random.randint(1, 10)
    if i == 3:
        cha += random.randint(1, 10)
    if i == 4:
        intel += random.randint(1, 10)
    if i == 5:
        wis += random.randint(1, 10)

print(f"__Y_O_U_R__S_T_A_T_S__\nStrength: {strength}   Charisma: {cha}\nDexterity: {dex}   Intelligence: {intel}\nConstitution: {con}  Wisdom: {wis}\n")

# The idea here is to give the player some basic items according to their class
def cha_class(fighter, rogue, wizard, cleric):
    if fighter == inventory:
        inventory.append('Shortsword')
        inventory.append('Rope')
        inventory.append('Scale Armour')

# Asks the player what class to play
if game_start == 'start':
    while True:
        us_class = int(input("what class would you like to play?\n(Please enter the number next to the class)\n1. Fighter\n2. Rogue\n3. Wizard\n4. Cleric\n\n"))
        if us_class == 1:
            cha_class(inventory, 0 , 0 , 0)
            break
        if us_class == 2:
            cha_class(0, inventory, 0, 0)
            break
        if us_class == 3:
            cha_class(0, 0, inventory, 0)
            break
        if us_class == 4:
            cha_class(0, 0, 0, inventory)
            break
        else:
            print('Please enter a valid class!')

print(inventory)
