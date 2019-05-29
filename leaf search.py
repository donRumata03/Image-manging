from PIL import Image, ImageTk
import random

img = Image.open("h.png")


w = img.size[0]
h = img.size[1]
taken = [[0 for y in range(h)] for x in range(w)]


num_leafs = 0
leafs = []


for x in range(w):
    for y in range(h):
        if img.getpixel((x, y)) == (255, 255, 255):
            taken[x][y] = 1


for x in range(w):
    for y in range(h):
        if taken[x][y]:
            print(x, y)
            rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            print(rgb)
            num_leafs += 1
            leafs.append([])
            last_wave = [(x, y)]
            while len(last_wave) > 0:

                this_wave = []
                for point in last_wave:
                    # Upper
                    if point[1] != 0 and taken[point[0]][point[1] - 1]:
                        this_wave.append((point[0], point[1] - 1))
                        taken[point[0]][point[1] - 1] = 0
                        img.putpixel((point[0], point[1] - 1), rgb)
                    if point[0] != 0 and taken[point[0] - 1][point[1]]:
                        this_wave.append((point[0] - 1, point[1]))
                        taken[point[0] - 1][point[1]] = 0
                        img.putpixel((point[0] - 1, point[1]), rgb)
                    if point[0] != w - 1 and taken[point[0] + 1][point[1]]:
                        this_wave.append((point[0] + 1, point[1]))
                        taken[point[0] + 1][point[1]] = 0
                        img.putpixel((point[0] + 1, point[1]), rgb)
                    if point[1] != h - 1 and taken[point[0]][point[1] + 1]:
                        this_wave.append((point[0], point[1] + 1))
                        taken[point[0]][point[1] + 1] = 0
                        img.putpixel((point[0], point[1] + 1), rgb)
                    if point[1] != h - 1 and point[0] != w - 1 and taken[point[0] + 1][point[1] + 1]:
                        this_wave.append((point[0] + 1, point[1] + 1))
                        taken[point[0] + 1][point[1] + 1] = 0
                        img.putpixel((point[0] + 1, point[1] + 1), rgb)
                    if point[1] != h - 1 and point[0] != 0 and taken[point[0] - 1][point[1] + 1]:
                        this_wave.append((point[0] - 1, point[1] + 1))
                        taken[point[0] - 1][point[1] + 1] = 0
                        img.putpixel((point[0] - 1, point[1] + 1), rgb)
                    if point[1] != 0 and point[0] != w - 1 and taken[point[0] + 1][point[1] - 1]:
                        this_wave.append((point[0] + 1, point[1] - 1))
                        taken[point[0] + 1][point[1] - 1] = 0
                        img.putpixel((point[0] + 1, point[1] - 1), rgb)
                    if point[1] != 0 and point[0] != 0 and taken[point[0] - 1][point[1] - 1]:
                        this_wave.append((point[0] - 1, point[1] - 1))
                        taken[point[0] - 1][point[1] - 1] = 0
                        img.putpixel((point[0] - 1, point[1] - 1), rgb)
                last_wave = this_wave
                leafs[-1].extend(last_wave)

print(num_leafs)
print(leafs[0])

img.save("L_KONT.png")
img.show()
