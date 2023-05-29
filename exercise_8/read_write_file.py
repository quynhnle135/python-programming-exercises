def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)


def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text)


def read_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)


