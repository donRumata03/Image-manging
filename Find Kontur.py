from PIL import Image, ImageTk

img = Image.open("r1.png")


w = img.size[0]
h = img.size[1]
img2 = Image.new("RGB", (w, h), (0, 0, 0))


def t(p):
    if p == (255, 255, 255):
        return True
    return False


print(img.getpixel((w, h - 1)))

'''

for x in range(w):
    for y in range(h):
        print(x, y)
        if t(img.getpixel((x, y))) and (x == 0 or t(img.getpixel((x, y))) is not t(img.getpixel((x - 1, y)))) or (y == 0 or t(img.getpixel((x, y))) is not t(img.getpixel((x, y - 1)))) or (x == w - 2 and t(img.getpixel((x, y))) is not t(img.getpixel((x + 1, y)))) or (y == h - 2 or t(img.getpixel((x, y))) is not t(img.getpixel((x, y + 1)))):
            img2.putpixel((x, y), (255, 255, 255))


img2.save("Res1.png")
img2.show()
'''