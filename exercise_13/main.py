from sum_and_product import calculate_sum, calculate_product

def main():
    list_1 = [1, 1, 1, 1, 1]
    list_2 = [1, 2, 3, 4, 5]
    list_3 = [2, 4, 6, 8, 10]
    print(calculate_sum(list_1))
    print(calculate_sum(list_2))
    print(calculate_sum(list_3))
    print(calculate_product(list_1))
    print(calculate_product(list_2))
    print(calculate_product(list_3))


if __name__ == "__main__":
    main()