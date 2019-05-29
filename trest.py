from PIL import Image


def diff(p1, p2):
    d1 = (p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2 + abs(p1[2] - p2[2]) ** 2
    # kr = p1[0] / p2[0]
    dr = 1
    return d1


def zaliv(img, point, k1 = 1, k2 = 1, num = 4000, nomnom = 1, bg = (0, 0, 0), fg = (0, 0, 0)):
    iteration = 0
    # img = Image.open("Simple.jpg")
    col0 = img.getpixel(point)
    global taken
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

    mix = img.size[0]
    miy = img.size[1]
    ma_x = 0
    ma_y = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if taken[i][j]:
                mix = min(i, mix)
                miy = min(j, miy)
                ma_x = max(i, ma_x)
                ma_y = max(j, ma_y)
    print(mix, miy, ma_x, ma_y)
    imgx = Image.new("RGB", (w, h), bg)
    for x in range(w):
        for y in range(h):
            if taken[x][y]:
                imgx.putpixel((x, y), (0, 0, 0))

    imgx = imgx.crop((mix, miy, ma_x, ma_y))
    return imgx


img = Image.open("2xiFMQxVwmU.jpg")

taken = [[]]
bg = (255, 255, 255)
fg = (50, 255, 50)
img2 = zaliv(img, (0, 0), nomnom=0, num=2500, bg=bg)

img2.save("r1.png")
