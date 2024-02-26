import bisect

N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 1. 並び替え
A.sort()
B.reverse()

result = -1

# 2分探査
for b in B:
    # 値+Dするとbより大きい差がD以下の値のうち最大の値のインデックスを返す
    target= bisect.bisect_right(A, b + D) -1
    if target >= 0 and A[target] >= b - D:
        # 要素がある、かつさがD以下
        if result < A[target] + b:
            result = A[target] + b
		
print(result)
