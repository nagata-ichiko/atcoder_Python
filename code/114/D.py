import heapq
import math

N,M = map(int, input().split())
a = list(map(int, input().split()))

for i in range(len(a)):
    a[i] *= -1
    
heapq.heapify(a)

for i in range(M):
    x = heapq.heappop(a)
    # print(x)
    x = int(math.ceil(x / 2.0))
    heapq.heappush(a, x)
    # print(x)

ans =  -sum(a)

print(ans)
# print(a)