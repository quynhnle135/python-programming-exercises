def number_of_bottles():
    for bottle in range(99, 1, -1):
        print(f"{bottle} bottles of beer on the wall,\n"
              f"{bottle} bottles of beer,\n"
              "Take one down,\n"
              "Pass it around,\n"
              f"{bottle - 1} bottles of beer on the wall,\n")
    # when reaching to the last bottle
    print("1 bottle of beer on the wall\n"
          "1 bottle of beer,\n"
          "Take one down,\n"
          "No more bottles of beer on the wall!")
