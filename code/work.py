import numpy as np
N = int(input())
a = [list(map(int, input().split())) for l in range(N)]
b = a.copy()

result = [None] * N

for i in range(N):
    buf = [None] * N
    for j in range(N):
        x1,y1 = a[i]
        x2,y2 = b[j]
        buf[j] = np.sqrt((x1-x2)**2 + (y1-y2)**2)
    result[i] = buf.index(max(buf))+1


for i in result:
    print(i)

