from title_case import get_title_case


def main():
    print(get_title_case("hello, world"))
    print(get_title_case("cat dog rat"))
    print(get_title_case("cat, dog, rat"))
    print(get_title_case("123abcd456xyz"))


if __name__ == "__main__":
    main()