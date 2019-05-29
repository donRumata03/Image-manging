from PIL import Image

name = "2xiFMQxVwmU.jpg"
res_path = "C:\\Users\\Vova\\source\\repos\\Find_similar_objects\\Find_similar_objects\\saved.ppm"
img = Image.open(name)
img2 = Image.new("RGB", img.size, (0, 0, 0))
h = img.size[1]
w = img.size[0]
st = "P3" + "\n" + str(w) + " " + str(h) + "\n255\n"
for y in range(h):
    for x in range(w):
        st += " ".join(list(map(str, img.getpixel((x, y))))[:3])
        img2.putpixel((x, y), img.getpixel((x, y)))
        st += "\n"

img2.save("test.png")
print(st)
f = open(res_path, "w")
f.write(st)
f.close()
