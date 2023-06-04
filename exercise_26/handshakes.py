def count_handshakes(people: list):
    count = 0
    for person in range(len(people)):
        for another_person in range(person + 1, len(people)):
            count += 1
    return count