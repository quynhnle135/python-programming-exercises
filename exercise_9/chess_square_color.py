def get_chess_square_color(row, column):
    if row > 8 or row <= 0 or column <= 0 or column > 8:
        return ""

    if row % 2 == 0 and column % 2 == 0:
        return "white"
    elif row % 2 == 0 and column % 2 == 1:
        return "black"
    elif row % 2 == 1 and column % 2 == 0:
        return "black"
    else:
        return "white"
