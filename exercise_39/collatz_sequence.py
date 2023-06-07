def generate_collatz_sequence(start):
    if start < 1:
        return []

    sequence = []
    num = start
    sequence.append(num)
    while num > 1:
        if num % 2 == 1:
            num = 3 * num + 1
        else:
            num = num // 2
        sequence.append(num)
    return sequence