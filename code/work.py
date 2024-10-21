import sys
import heapq

def solve():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx +=1
    results = []
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        idx +=2
        A = list(map(int, data[idx:idx+N]))
        idx +=N
        B = list(map(int, data[idx:idx+N]))
        idx +=N
        items = sorted(zip(A, B), key=lambda x: x[0])
        heap = []
        sumB =0
        min_val = float('inf')
        for a, b in items:
            heapq.heappush(heap, -b)
            sumB +=b
            if len(heap) > K:
                removed = -heapq.heappop(heap)
                sumB -=removed
            if len(heap) == K:
                val = a * sumB
                if val < min_val:
                    min_val = val
        results.append(str(min_val))
    print('\n'.join(results))

if __name__ == "__main__":
    solve()