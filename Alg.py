def p1(n):
    return 16 + 5 * (n - 1)


def p2(n):
    return 17 + 4 * (n - 1)


ms1 = [p1(i) for i in range(1, 500)]
ms2 = [p2(i) for i in range(1, 500)]

ms1.extend(ms2)

ms3 = sorted(ms1)[0:100]


print(len(ms3), ms3, sum(ms3))
