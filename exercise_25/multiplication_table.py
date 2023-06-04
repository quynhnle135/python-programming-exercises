def generate_multiplication_table():
    for row in range(1, 11):
        for column in range(1, 11):
            print(str(row * column), end=" ")
        print()


def multiplication_table() -> list:
    result = []
    for row in range(1, 11):
        row_list = []
        for column in range(1, 11):
            value = column * row
            row_list.append(value)
        result.append(row_list)

    return result



