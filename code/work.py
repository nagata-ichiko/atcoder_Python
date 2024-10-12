N = int(input())
grid = [list(input().strip()) for _ in range(N)]

rotated_grid = list(zip(*grid[::-1]))
for row in rotated_grid:
    print("".join(row))
