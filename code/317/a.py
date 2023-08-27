# 入力を受け取る
N, H, X = map(int, input().split())
P = list(map(int, input().split()))

# モンスターの体力をX以上にするために必要な傷薬の番号を求める
for i in range(N):
    if H + P[i] >= X:
        print(i + 1)
        break
