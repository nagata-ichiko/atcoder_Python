# 入力をリストとして読み込む
S = list(map(int, input().split()))

# 条件を確認
if all(100 <= s <= 675 for s in S) and all(s % 25 == 0 for s in S) and S == sorted(S):
    print('Yes')
else:
    print('No')
