from random import randint

def roll_dice(number = 1, sides = 20, bonus = 0):
    # number and sides - xdy - 2d6, 3d8, 2d10
    # bonus is added to the result of rolling those x dice

    result = bonus

    for x in range(0, number):
        result += randint(1, sides)

    return result

# def generate_character():
#     # str, dex, con, int, wis, cha
#     # 3-18 - 3d6

#     character = {
#         'str': roll_dice(3, 6),
#         'dex': roll_dice(3, 6),
#         'con': roll_dice(3, 6),
#         'int': roll_dice(3, 6),
#         'wis': roll_dice(3, 6),
#         'cha': roll_dice(3, 6)
#     }

#     return character

# def generate_character():
#     # str, dex, con, int, wis, cha
#     # 3-18 - 3d6

#     stats = ['str', 'dex', 'con', 'int', 'wis', 'cha']
#     character = {}

#     for stat in stats:
#         character[stat] = roll_dice(3, 6)

#     return character

# def generate_character():
#     # str, dex, con, int, wis, cha
#     # 3-18 - 3d6

#     character = {}
#     character['str'] = roll_dice(3, 6)
#     character['dex'] = roll_dice(3, 6)
#     character['con'] = roll_dice(3, 6)
#     character['int'] = roll_dice(3, 6)
#     character['wis'] = roll_dice(3, 6)
#     character['cha'] = roll_dice(3, 6)

#     return character

def generate_character(stats = ['str', 'dex', 'con', 'int', 'wis', 'cha'], number = 3, sides = 6, max = 18):
    # str, dex, con, int, wis, cha
    # 3-18 - 3d6

    character = {}

    for stat in stats:
        result = roll_dice(number, sides)
        if result > max:
            character[stat] = max
        else:
            character[stat] = result

    return character


print(generate_character(number = 4))