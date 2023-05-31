from find_and_replace import find_and_replace, find_and_replace_advanced


def main():
    print(find_and_replace("the fox.", "fox", "dog"))
    print(find_and_replace("one two three", "two", "ten"))

    print(find_and_replace_advanced("the fox.", "fox", "dog"))
    print(find_and_replace_advanced("one two three", "two", "ten"))


if __name__ == "__main__":
    main()