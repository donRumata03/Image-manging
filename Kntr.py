from PIL import Image, ImageTk

img = Image.open("r1.png")


w = img.size[0]
h = img.size[1]
img2 = Image.new("RGB", (w, h), (0, 0, 0))


def t(p):
    if img.getpixel(p) == (255, 255, 255):
        return True
    return False


def p(p):
    img2.putpixel((p[0], p[1]), (255, 255, 255))


for x in range(w):
    for y in range(h):
        if t((x, y)):
            if x == 0:
                p((x, y))
            elif t((x, y)) != t((x - 1, y)):
                p((x, y))
            if y == 0:
                p((x, y))
            elif t((x, y)) != t((x, y - 1)):
                p((x, y))
            if x == w-1:
                p((x, y))
            elif t((x, y)) != t((x + 1, y)):
                p((x, y))
            if y == h-1:
                p((x, y))
            elif t((x, y)) != t((x, y + 1)):
                p((x, y))

img2.save("h.png")