from leap_year import isLeapYear

def main():
    print(isLeapYear(1999)) # False
    print(isLeapYear(2001)) # false
    print(isLeapYear(2002)) # False
    print(isLeapYear(2100)) # False
    print(isLeapYear(2004)) # True
    print(isLeapYear(2400)) # True
    print(isLeapYear(2000)) # True


if __name__ == "__main__":
    main()