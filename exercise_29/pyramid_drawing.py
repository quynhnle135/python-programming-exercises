# my solution
def draw_pyramid(height):
    if height == 0:
        return
    space = height - 1
    count = 1
    for r in range(height):
        print((" " * space) + ("*" * count) + (" " * space))
        space -= 1
        count += 2


# suggested solution
def drawPyramid(height):
    for rowNumber in range(height):
        leftSideSpace = " " * (height - (rowNumber + 1))
        pyramidRow = "*" * (rowNumber * 2 + 1)
        print(leftSideSpace + pyramidRow)


