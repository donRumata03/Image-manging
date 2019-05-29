from PIL import Image

f = open("C:\\Users\\Vova\\source\\repos\\Find_similar_objects\\Find_similar_objects\\saved.ppm")

ms = f.read().split("\n")
h = int(ms[1].split()[1])
w = int(ms[1].split()[0])
img = Image.new("RGB", tuple(map(int, ms[1].split())), (0, 0, 0))
# matriks = img.load()
for i in range(len(ms[3:])):
    x = i % w
    y = i // w
    Tuple = (ms[3:])[i].split()
    if ms[3:][i] == '' or x >= w or y >= h:
        break
    r = int(Tuple[0])
    g = int(Tuple[1])
    b = int(Tuple[2])
    img.putpixel((x, y), (r, g, b))
img.save("C:\\Users\\Vova\\source\\repos\\Find_similar_objects\\Find_similar_objects\\picture.png")
img.show()

