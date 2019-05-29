from matplotlib import pyplot as plt

ms = [(28, 426), (29, 424), (28, 425), (28, 427), (29, 423)]
'''
28 426
29 424
28 425
28 427
29 423
A: -30.9291 B: 1303.39
'''

percent = 0
num = 0


def find_MMS(ms):
    n = len(ms)
    msx = []
    msy = []

    for x in ms:
        msx.append(x[0])
        msy.append(x[1])

    s_xy = 0
    s_x = 0
    s_y = 0
    s_x2 = 0
    for i in ms:
        s_xy += i[0] * i[1]
        s_x += i[0]
        s_y += i[1]
        s_x2 += i[0] * i[0]
    print((n * s_xy, s_x * s_y))
    a = (n * s_xy - s_x * s_y) / (n * s_x2 - s_x ** 2)
    b = (s_y - a * s_x) / n
    plt.xlim(0, 100)
    plt.ylim(350, 500)
    plt.scatter(msx, msy)
    msx = []
    msy = []

    for x in range(0, 100):
        msx.append(x)
        msy.append(a * x + b)

    plt.plot(msx, msy)
    # plt.show()
    return a, b


if False and __name__ == "__main__":
    for i in range(10):
        m = ms[i * 10: (i + 1) * 10]
        find_MMS(m)
print(find_MMS(ms))
msx = []
msy = []
a = -30.9291
b = 1303.39
for x in range(0, 100):
    msx.append(x)
    msy.append(a * x + b)

plt.plot(msx, msy)

plt.show()
