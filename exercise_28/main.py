from border_drawing import draw_border, drawBorder


def main():
    draw_border(16, 4)
    print("USING SUGGESTED SOLUTION")
    drawBorder(16, 4)
    print("NEXT DRAWING")
    draw_border(10, 5)
    print("USING SUGGESTED SOLUTION")
    drawBorder(10, 5)


if __name__ == "__main__":
    main()