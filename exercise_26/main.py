from handshakes import count_handshakes


def main():
    print(count_handshakes(['Alice', 'Bob']))
    print(count_handshakes(['Alice', 'Bob', 'Carol']))
    print(count_handshakes(['Alice', 'Bob', 'Carol', 'David']))


if __name__ == "__main__":
    main()