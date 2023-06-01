from mode import find_mode


def main():
    print(find_mode([]))
    print(find_mode([1, 2, 3, 4, 4]))
    print(find_mode([1, 1, 2, 3, 4]))
    print(find_mode([0, 0, 0, 0, 0]))
    print(find_mode([1, 2, 3, 4, 5, 6]))
    print(find_mode([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))


if __name__ == "__main__":
    main()
