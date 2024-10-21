import sys
import sys
from collections import deque

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    edges = data[2:]
    
    adj = [[] for _ in range(N + 1)]
    for i in range(M):
        a = int(edges[2 * i])
        b = int(edges[2 * i + 1])
        adj[a].append(b)
    
    from collections import deque
    
    distance = [-1] * (N + 1)
    distance[1] = 0
    q = deque()
    q.append(1)
    
    min_cycle = -1
    
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v == 1 and distance[u] + 1 >= 2:
                if min_cycle == -1 or distance[u] +1 < min_cycle:
                    min_cycle = distance[u] +1
            if distance[v] == -1:
                distance[v] = distance[u] +1
                q.append(v)
    
    print(min_cycle)

if __name__ == "__main__":
    main()