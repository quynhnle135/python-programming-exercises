from read_write_file import read_from_file, write_to_file, append_to_file


def main():
    write_to_file('draft.txt', 'hello mimi\n')
    append_to_file('draft.txt', 'so long by vinh khuat is so good\n')
    append_to_file('draft.txt', 'i gotta go to work at 6:30pm\n')
    read_from_file('draft.txt')


if __name__ == "__main__":
    main()