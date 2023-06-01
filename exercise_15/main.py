from median import find_median


def main():
    print(find_median([]))
    print(find_median([1, 2, 3]))
    print(find_median([1, 2, 3, 4]))
    print(find_median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]))
    print(find_median([3, 7, 10, 4, 1, 9, 6, 2, 8]))


if __name__ == "__main__":
    main()