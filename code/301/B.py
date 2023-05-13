N = int(input())
A = list(map(int, input().split()))

result = []
for i in range(N-1):
    result.append(A[i])
    diff = abs(A[i] - A[i+1])
    if diff > 1:
        if A[i] < A[i+1]:
            result.extend(range(A[i]+1, A[i+1]))
        else:
            result.extend(range(A[i]-1, A[i+1], -1))

result.append(A[-1]) 

print(*result)
