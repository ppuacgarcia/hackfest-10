def restrict(rectangles: list[list[int]]):
    for i in range(len(rectangles)):
        for j in range(len(rectangles)-1):
            if j < len(rectangles)-1:
                x0r1 = rectangles[i][0]
                y0r1 = rectangles[i][1]
                x1r1 = rectangles[i][2]
                y1r1 = rectangles[i][3]
                x0r2 = rectangles[j+1][0]
                y0r2 = rectangles[j+1][1]
                x1r2 = rectangles[j+1][2]
                y1r2 = rectangles[j+1][3]
                if x0r2 > x0r1 > x1r2 or y0r2 > y0r1 > y1r2 or x0r2 > x1r1 > x1r2 or y0r2 > y1r1 > y1r2:
                    if x0r2 > x0r1 > x1r2:
                        dif_x = x0r2-x0r1
                        rectangles[i][0] = rectangles[i][0]+dif_x
                    if x0r2 < x1r1 < x1r2:
                        dif_x = x1r2 - x1r1
                        rectangles[i][2] = rectangles[i][2] - dif_x
                    if y0r2 > y0r1 > y1r2:
                        dif_y = y0r2-y0r1
                        rectangles[i][1] = rectangles[i][1] - dif_y
    return rectangles


def calculate_total_rectangles(rectangles: list[list[int]]):
    total_rectangles = 0
    for index in range(len(rectangles)):
        x0 = rectangles[index][0]
        y0 = rectangles[index][1]
        x1 = rectangles[index][2]
        y1 = rectangles[index][3]
        dif_x = x1 - x0
        dif_y = y1 - y0
        print(dif_y*dif_x)
        total_rectangles = total_rectangles + dif_y*dif_x
    return total_rectangles


rectangles = [[3, 3, 8, 4],
              [6, 3, 8, 9],
              [11, 6, 14, 12]]
restricted_rectangles = restrict(rectangles.copy())
print(restricted_rectangles)
print(calculate_total_rectangles(restricted_rectangles))
