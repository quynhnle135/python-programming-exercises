import random

def roll_dice(dice):
    if dice == 0:
        return 0
    result = random.randint(1, dice * 6)
    return result