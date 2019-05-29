n, m = map(int, input().split())
n = 8 - n + 1
m = 8 - m + 1


print(n, m)

ms = [[0 for i in range(m)] for j in range(n)]
mt = [[0 for i in range(m)] for j in range(n)]

for y in range(n):
    for x in range(m):
        if x == 0:
            mt[y][x] = 1
            continue
        if y == 0:
            mt[y][x] = mt

print(ms)