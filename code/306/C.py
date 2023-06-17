N = int(input().strip())
A = list(map(int, input().strip().split()))

indices = [0] * (N + 1)
f = [0] * (N + 1)

# Count the appearance of each number
for i, a in enumerate(A, 1):
    indices[a] += 1
    if indices[a] == 2:
        f[a] = i

# Sort numbers based on the index of their second appearance
order = sorted(range(1, N + 1), key=lambda x: f[x])
print(' '.join(map(str, order)))
