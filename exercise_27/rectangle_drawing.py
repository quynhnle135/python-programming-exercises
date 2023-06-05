def draw_rectangle(width, height):
    if width == 1 or height == 1:
        return
    for w in range(height):
        for h in range(width):
            print("#", end=" ")
        print()
