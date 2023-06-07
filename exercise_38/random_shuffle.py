import random


def random_shuffle(values):
    for i in range(len(values)):
        swap_index = random.randint(0, len(values) - 1)
        values[i], values[swap_index] = values[swap_index], values[i]

    return values