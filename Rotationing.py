import math
from matplotlib import pyplot as plt
import random

dist = 1

ang = 60 * math.pi / 180  # in radians


def rotate(point, O, degree):
    x0 = point[0]
    y0 = point[1]
    xo = O[0]
    yo = O[1]
    # (x1 - xo) ** 2 + (y1 - yo) ** 2 = (x0 - xo) ** 2 + (y0 - yo) ** 2
    # angle(O, point, point1) = degree
    # degree = angle(O, A, (xa, yo)) + angle(O, (xa, yo), B)


def angle(O, A, B):
    xo = O[0]
    yo = O[1]
    xa = A[0]
    ya = A[1]
    xb = B[0]
    yb = B[1]

    ang1 = math.atan((ya - yo)/(abs(xa - xo)))
    ang2 = math.atan((yo - yb)/(abs(xb - xo)))
    print((ya - yo)/((xa - xo)), (yo - yb)/((xb - xo)))
    print((ya - yo), ((xa - xo)), (yo - yb), ((xb - xo)))
    return ang1 + ang2


for i in range(100):
    xo = random.random()
    yo = random.random()
    xa = random.random()
    ya = random.random()
    xb = random.random()
    yb = random.random()

    plt.plot([xa, xo, xb], [ya, yo, yb])
    plt.scatter([xa, xo, xb], [ya, yo, yb])
    plt.scatter([xa], [ya])
    plt.title(str(angle((xo, yo), (xa, ya), (xb, yb)) * 180 / math.pi))

    plt.show()

