N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))

# 皿の色と価格を対応付ける辞書を作成
price = {D[i]: P[i+1] for i in range(M)}
price['default'] = P[0]

# 食べた料理の価格の合計を求める
total = 0
for c in C:
    total += price.get(c, price['default'])

print(total)
