def calculate_sum(A):
    return sum(a * 2 ** i for i, a in enumerate(A))

A = list(map(int, input().strip().split()))
print(calculate_sum(A))
