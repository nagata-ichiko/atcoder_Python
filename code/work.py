def min_product(N, M):
    for a in range(1, N + 1):
        b = -(-M // a)  # ceil(M / a)
        if b <= N:
            return a * b
    return -1

# 標準入力から N, M を受け取る
N, M = map(int, input().split())

# 条件を満たす最小の正整数 X を求める
result = min_product(N, M)

# 結果を出力する
print(result)
