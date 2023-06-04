from multiplication_table import generate_multiplication_table, multiplication_table


def main():
    # generate_multiplication_table()
    print("-----")
    table = multiplication_table()
    for row in table:
        print(row)


if __name__ == "__main__":
    main()