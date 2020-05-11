def main(image_2d, sr, sc, new_color):
    initial_color = image_2d[sr][sc]
    image_1 = flood_fill(image_2d, sr, sc, initial_color, new_color, -1, 0)
    image_2 = flood_fill(image_1, sr, sc, initial_color, new_color, 1, 0)
    image_3 = flood_fill(image_2, sr, sc, initial_color, new_color, 0, -1)
    image_4 = flood_fill(image_3, sr, sc, initial_color, new_color, 0, 1)
    image_5 = flood_fill(image_4, sr, sc, initial_color, new_color, 1, 1)
    image_6 = flood_fill(image_5, sr, sc, initial_color, new_color, -1, -1)
    image_7 = flood_fill(image_6, sr, sc, initial_color, new_color, -1, 1)
    image_8 = flood_fill(image_7, sr, sc, initial_color, new_color, 1, -1)
    return image_8


def flood_fill(image_2d, sr, sc, initial_color, new_color, r, c):
    if sr > (len(image_2d) - 1) or sc > (len(image_2d[0]) - 1) or sr < 0 or sc < 0:
        return image_2d
    if image_2d[sr][sc] == initial_color:
        image_2d[sr][sc] = new_color

    return flood_fill(image_2d, sr + r, sc + c, initial_color, new_color, r, c)


image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

sr = 1
sc = 1
newColor = 2

main(image, sr, sc, newColor)
