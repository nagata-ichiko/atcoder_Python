import heapq
import sys

N,M = map(int, input().split())

a = [list(map(int, input().split())) for i in range(M)]
graph = [list() for i in range(N + 1)]

for a, b, c in a:
	graph[a].append((b, c))
	graph[b].append((a, c))

MAX = sys.maxsize
kakutei = [ False ] * (N + 1)
queue = []
calc =  [ MAX ] * (N + 1)
calc[1] =0
heapq.heappush(queue, (calc[1], 1))


while len(queue) > 0:
    x = heapq.heappop(queue)[1]
    
    if kakutei[x] == True:
        continue
    kakutei[x] = True
    for v in graph[x]:
        if calc[v[0]] > calc[x] + v[1]:
            calc[v[0]] = calc[x] + v[1]
            heapq.heappush(queue, (calc[v[0]], v[0]))

for i in range(1, N + 1):
    if kakutei[i]:
        print(calc[i])
    else:
        print("-1")