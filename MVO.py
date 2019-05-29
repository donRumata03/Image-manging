from matplotlib import pyplot as plt
import math


def rotate(A,B,C):
    return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])


def predicate(p):
    delta_x = p[0] - points[shkvoren][0]
    delta_y = p[1] - points[shkvoren][1]
    if delta_x == 0 and delta_y > 0:
        return 9863541
    elif delta_x == 0 and delta_y < 0:
        return -9863541
    return delta_y/delta_x


def dele(point):
    for i in range(len(points)):
        if point == points[i]:
            num = points.pop(i)
            return num


def exclude(points, obolochkis, x):
    obolochka = []
    for i in range(len(x)):
        num = dele(x[i])
        if num is None:
            num = points[shkvoren]
        obolochka.append(num)
    obolochkis.append(obolochka)


def check(points):
    for i in range(len(points) - 2):
            if predicate(points[i + 2]) == predicate(points[i + 1]) and math.sqrt((points[i][0])**2 + (points[i+1][0])) > math.sqrt((points[i+2][1])**2 + (points[i][1])):
                points[i + 2], points[i + 1] = points[i + 1], points[i + 2]


def find_MVO(po, shkvoren):
    x = po.pop(shkvoren)
    po.sort(key=predicate)
    check(po)
    # print(po)
    S = [points[shkvoren], po[0]]
    for i in range(1, len(po)):
        while rotate(S[-2], S[-1], po[i]) < 0:
            # print(S, rotate(S[-2], S[-1], po[i]))
            del S[-1]  # pop(S)

        S.append(po[i])  # push(S,P[i])
        # print(S)
        # print("kjlkjlkj")
    return S


def find_shkvoren(points):
    mx = points[0][0]
    mxi = 0
    for i in range(len(points)):
        if points[i][0] < mx:
            mx = points[i][0]
            mxi = i
    return mxi


def points_print(points):
    msx = [i[0] for i in points]
    msy = [i[1] for i in points]
    plt.plot(msx, msy)


def main():
    global shkvoren, points, obolochkis
    while len(points) >= 2:
        print(points)
        shkvoren = find_shkvoren(points)
        print(shkvoren)
        x = find_MVO(points[:], shkvoren)
        print(x)
        result = x
        result.append(points[shkvoren])
        points_print(result)
        exclude(points, obolochkis, x)



points = [(1, 3), (3, 0), (0, 5), (2, 4), (3, 5), (4, 3), (5, 5), (4, 1), (5, 7), (6, 2), (6, 4), (8, 1), (8, 4), (8, 6), (3.0, 5.6), (6.2, 3.9), (5.5656, 2.37347), (7.5678, 1.3453568), (1.5, 7.5)]


msx = [i[0] for i in points]
msy = [i[1] for i in points]

plt.figure(figsize=(6, 6))
plt.xlim(0, 9)
plt.ylim(0, 8)
plt.scatter(msx, msy)
'''
shkvoren = find_shkvoren(points)
print(shkvoren)
x = find_MVO(points[:], shkvoren)
result1 = x
result1.append(points[shkvoren])
exclude(points, obolochkis, x)


shkvoren = find_shkvoren(points)

x1 = find_MVO(points[:], shkvoren)
result2 = x1
result2.append(points[shkvoren])
plt.show()
'''

shkvoren = 0
obolochkis = []
main()
plt.show()
