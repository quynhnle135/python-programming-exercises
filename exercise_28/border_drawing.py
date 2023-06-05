# my solution
def draw_border(width, height):
    if width == 1 or height == 1:
        return

    for row in range(height):
        for column in range(width):
            if (row == 0 and column == 0) or (row == 0 and column == width - 1) or (row == height - 1 and column == 0) or (row == height - 1 and column == width - 1):
                print("+", end="")
            elif row == 0 or row == height - 1:
                print("-", end="")
            elif column == 0 or column == width - 1:
                print("|", end="")
            else:
                print(" ", end="")
        print()


# suggested solution
def drawBorder(width, height):
    if width < 2 or height < 2:
        return
    print("+" + ("-" * (width - 2)) + "+")
    for i in range(1, height - 1):
        print("|" + " " * (width - 2) + "|")
    print("+" + ("-" * (width - 2)) + "+")

