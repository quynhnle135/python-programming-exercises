from validate_date import validate_date


def main():
    print(validate_date(2020, 12, 31))
    print(validate_date(2020, 2, 29))
    print(validate_date(2020, 2, 30))
    print(validate_date(2023, 5, 13))
    print(validate_date(2023, 2, 29))
    print(validate_date(2023, 2, 28))


if __name__ == "__main__":
    main()
