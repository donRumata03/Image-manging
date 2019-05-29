from tkinter import *
from PIL import Image, ImageTk


l_tab = 250
u_tab = 200
b_tab = 100
r_tab = 100

image = None


def click(event):
    global x, y
    x = event.x
    y = event.y
    print("Click:", x, y)
    print("Converted:", (int(x * kxy), int(y * kxy)))


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
            # print(iteration)
            imgx = Image.new("RGB", (w, h), bg)
            for x in range(w):
                for y in range(h):
                    if not taken[x][y]:
                        imgx.putpixel((x, y), img.getpixel((x, y)))
            show_img(imgx)
            imgx.save("Samples/" + str(nomnom) + "/it=" + str(iteration) + ".jpg")
        iteration += 1
        last_wave = this_wave

    imgx = Image.new("RGB", (w, h), bg)
    for x in range(w):
        for y in range(h):
            if not taken[x][y]:
                imgx.putpixel((x, y), img.getpixel((x, y)))
    return imgx


def transpose():
    global image
    num = scale.get()
    print(image.size[0], image.size[1])
    print((scr_w - l_tab - r_tab), (scr_h - u_tab - b_tab))
    image = zaliv(image, (int(x * kxy), int(y * kxy)), k1=1, k2=1, num=num, nomnom=100, bg=(255, 255, 255))
    show_img(image)


def show_img(img):
    global img_lbl, kxy
    s0 = img.size[0]
    s1 = img.size[1]
    print("Size:", img.size[0], img.size[1])
    if scr_w - r_tab - l_tab > img.size[0] and scr_h - u_tab - b_tab > img.size[1]:
        img = img.resize((img.size[0], img.size[1]))
        kxy = 1
    elif scr_w - r_tab - l_tab > img.size[0]:
        img = img.resize(((img.size[0] * (scr_h - u_tab - b_tab)) // img.size[1], scr_h - b_tab - u_tab))
        kxy = s1 / (scr_h - u_tab - b_tab)
        print(kxy)
    elif scr_h - b_tab - u_tab > img.size[1]:
        img = img.resize((scr_w - l_tab - r_tab, (img.size[1] * (scr_w - r_tab - l_tab)) // img.size[0]))
        kxy = s0 / (scr_w - l_tab - r_tab)
    else:
        if scr_h / img.size[1] > scr_w / img.size[0]:
            img = img.resize((scr_w - l_tab - r_tab, (img.size[1] * (scr_w - r_tab - l_tab)) // img.size[0]))
            kxy = s0 / (scr_w - l_tab - r_tab)
            print((scr_w - l_tab - r_tab), img.size[0],  img.size[0] / (scr_w - l_tab - r_tab))
            print(4)
        else:
            img = img.resize(((img.size[0] * (scr_h - u_tab - b_tab)) // img.size[1], scr_h - b_tab - u_tab))
            kxy = s1 / (scr_h - u_tab - b_tab)
            print(5)
    img_for_inserting = ImageTk.PhotoImage(img)
    img_lbl = Label(window, image=img_for_inserting)
    img_lbl.image = img_for_inserting
    img_lbl.place(x=l_tab, y=u_tab)
    img_lbl.bind("<Button-1>", click)
    # print(img_lbl.height())
    window.update()
    print(kxy)


def opening():
    global image, kxy
    img = Image.open(texter.get('1.0', END)[:-1])
    image = img
    show_img(img)
    print(kxy)


window = Tk()
window.attributes("-fullscreen", True)
# window.geometry("1000x500")
window.configure(bg="#999950")

scr_h = window.winfo_screenheight()
scr_w = window.winfo_screenwidth()

btn_create = Button(window, height=5, width=15, bg="green", text="Open Image", command=opening)
btn_create.place(x=100, y=25)

scale = Scale(window, orient=HORIZONTAL, length=300, from_=0, to=10000, tickinterval=1000, resolution=1)
scale.place(x=500, y=25)

texter = Text(window, height=4, width=15, font='Arial 14', wrap=WORD)
texter.place(x=300, y=25)

btn_transpose = Button(window, height=5, width=15, bg="red", text="Transpose", command=transpose)
btn_transpose.place(x=900, y=25)


texter.insert(1.0, "Simple.jpg")
x, y = 0, 0
kxy = 1

window.mainloop()
