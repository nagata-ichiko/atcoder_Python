# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# なくした整数を求める
missing_number = sum(range(min(A), max(A)+1)) - sum(A)
print(missing_number)
