from ordinal_suffix import ordinal_suffix, ordinal_suffix_optimal


def main():
    for i in range(101):
        print(ordinal_suffix_optimal(i))
    print("----")
    print(ordinal_suffix_optimal(111))
    print(ordinal_suffix_optimal(112))
    print(ordinal_suffix_optimal(113))
    print(ordinal_suffix_optimal(10011))
    print(ordinal_suffix_optimal(10012))
    print(ordinal_suffix_optimal(10013))
    print(ordinal_suffix_optimal(1001))


if __name__ == "__main__":
    main()

