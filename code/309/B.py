N = int(input())

# 2次元マス目を作成
A = []
for _ in range(N):
    A.append(list(map(int, list(input()))))

# 外側のマスを保存するリスト
outer = []
# 1行目、1列目、N列目、N行目の順に追加
outer.extend(A[0])
for i in range(1, N-1):
    outer.append(A[i][-1])
outer.extend(A[-1][::-1])
for i in range(N-2, 0, -1):
    outer.append(A[i][0])

# 外側のマスを時計回りに1つずらす
outer = [outer[-1]] + outer[:-1]

# 新しいマス目を作成
B = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        # 外側のマス
        if i == 0: # 1行目
            B[i][j] = outer[j]
        elif j == N-1: # N列目
            B[i][j] = outer[N+i-1]
        elif i == N-1: # N行目
            B[i][j] = outer[3*N-j-3]
        elif j == 0: # 1列目
            B[i][j] = outer[4*N-i-4]
        else: # 内側のマス
            B[i][j] = A[i][j]

# 新しいマス目を出力
for i in range(N):
    print(''.join(map(str, B[i])))
