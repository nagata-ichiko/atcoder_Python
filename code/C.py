H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

min_i = min_j = float('inf')
max_i = max_j = -float('inf')

# クッキーが存在する領域の境界を見つける
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            min_i = min(min_i, i)
            max_i = max(max_i, i)
            min_j = min(min_j, j)
            max_j = max(max_j, j)

# クッキーが取り除かれたセルを見つける
for i in range(min_i, max_i+1):
    for j in range(min_j, max_j+1):
        if grid[i][j] == '.':
            print(i+1, j+1)
            exit(0)
