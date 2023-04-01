import sys

def generate_strings(H, W, A):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []

    for i in range(H):
        row = ''
        for j in range(W):
            if A[i][j] == 0:
                row += '.'
            else:
                row += alphabet[A[i][j] - 1]
        result.append(row)

    return result

# 標準入力からH, Wおよび行列Aを取得
H, W = map(int, sys.stdin.readline().strip().split())
A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(H)]

strings = generate_strings(H, W, A)
for s in strings:
    print(s)
