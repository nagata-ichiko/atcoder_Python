T = int(input())
for _ in range(T):
    N, K = map(int, input().strip().split())
    N_base_3 = ""
    while N > 0:
        N_base_3 = str(N % 3) + N_base_3
        N //= 3
    if N_base_3.count('2') > 0 or N_base_3.count('1') > K:
        print("NO")
    else:
        print("YES")
