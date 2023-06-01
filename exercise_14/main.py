from average import find_average


def main():
    print(f"Average for [1, 2, 3, 4, 5, 6]: {str(find_average([1, 2, 3, 4, 5, 6]))}")
    print(f"Average for [1, 1, 1, 1]: {str(find_average([1, 1, 1, 1]))}")
    print(f"Average for [2, 4, 6, 8, 10]: {str(find_average([2, 4, 6, 8, 10]))}")


if __name__ == "__main__":
    main()