def has_pair_with_difference(A, X):
    A_set = set(A)  # 数列Aの要素をセットに変換
    for a in A_set:
        target = a - X
        if target in A_set:  # セット内で高速検索
            return True
    return False

# 標準入力から数列の長さ N と整数 X を受け取る
N, X = map(int, input().split())

# 標準入力から数列 A を受け取る
A = list(map(int, input().split()))

# A_i - A_j = X となる i, j のペアが存在するかどうかを判断する
result = has_pair_with_difference(A, X)

# 結果を出力する
if result:
    print("Yes")
else:
    print("No")
