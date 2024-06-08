N,M = map(int, input().split())
H = list(map(int, input().split()))

result = 0
for i in range(N):
    M = M- H[i]
    if 0<=M:
        result += 1
    else:
        break

print(result)




