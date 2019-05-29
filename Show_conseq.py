from PIL import Image
fname = "A.txt"
img = Image.new("RGB", (729, 658), (0, 0, 0))
ms = open(fname).read().split("\n")

for i in range(len(ms)):
    ms[i] = tuple(list(map(int, ms[i].split())))

for i in range(len(ms)):
    img.putpixel((ms[i][0], ms[i][1]), (255, 255, 255))
    if (i + 1) % 100:
        img.save("Samples/2/iter= " + str(i + 1) + ".jpg")

print(ms)

