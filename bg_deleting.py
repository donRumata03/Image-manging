from PIL import Image


def diff(p1, p2):
    d1 = (p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2 + abs(p1[2] - p2[2]) ** 2
    # kr = p1[0] / p2[0]
    dr = 1
    return d1


def zaliv(img, point, k1 = 1, k2 = 1, num = 4000, nomnom = 1, bg = (0, 0, 0)):
    iteration = 0
    # img = Image.open("Simple.jpg")
    col0 = img.getpixel(point)

    h = img.size[1]
    w = img.size[0]
    last_wave = [point]
    taken = [[0 for y in range(h)] for x in range(w)]
    while len(last_wave) > 0:

        this_wave = []
        # print(last_wave)
        for point in last_wave:
            col1 = img.getpixel(point)
            # Upper
            if point[1] != 0 and not taken[point[0]][point[1] - 1] and (k1 * diff(col1, img.getpixel((point[0], point[1] - 1))) + k2 * diff(col0, img.getpixel((point[0], point[1] - 1)))) < num:
                this_wave.append((point[0], point[1] - 1))
                taken[point[0]][point[1] - 1] = 1
            if point[0] != 0 and not taken[point[0] - 1][point[1]] and (k1 * diff(col1, img.getpixel((point[0] - 1, point[1]))) + k2 * diff(col0, img.getpixel((point[0] - 1, point[1])))) < num:
                this_wave.append((point[0] - 1, point[1]))
                taken[point[0] - 1][point[1]] = 1
            if point[0] != w - 1 and not taken[point[0] + 1][point[1]] and (k1 * diff(col1, img.getpixel((point[0] + 1, point[1]))) + k2 * diff(col0, img.getpixel((point[0] + 1, point[1])))) < num:
                this_wave.append((point[0] + 1, point[1]))
                taken[point[0] + 1][point[1]] = 1
            if point[1] != h - 1 and not taken[point[0]][point[1] + 1] and (k1 * diff(col1, img.getpixel((point[0], point[1] + 1))) + k2 * diff(col0, img.getpixel((point[0], point[1] + 1)))) < num:
                this_wave.append((point[0], point[1] + 1))
                taken[point[0]][point[1] + 1] = 1
        if iteration % 100 == 0:
            print(iteration)
            imgx = Image.new("RGB", (w, h), bg)
            for x in range(w):
                for y in range(h):
                    if not taken[x][y]:
                        imgx.putpixel((x, y), img.getpixel((x, y)))
            imgx.save("Samples/" + str(nomnom) + "/it=" + str(iteration) + ".jpg")
        iteration += 1
        last_wave = this_wave

    imgx = Image.new("RGB", (w, h), bg)
    for x in range(w):
        for y in range(h):
            if not taken[x][y]:
                imgx.putpixel((x, y), img.getpixel((x, y)))
    return imgx


img = Image.open("it=200.jpg")
bg = (50, 255, 50)
img2 = zaliv(img, (338, 294), nomnom=0, num=50000, bg=bg)

img2.save("r1.jpg")
