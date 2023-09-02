def covered_area(N, rectangles):
    plane = [[0] * 101 for _ in range(101)]
    
    for a, b, c, d in rectangles:
        for x in range(a, b):
            for y in range(c, d):
                plane[x][y] = 1
                
    area = sum(sum(row) for row in plane)
    return area

# 標準入力から値を受け取る
N = int(input())
rectangles = [list(map(int, input().split())) for _ in range(N)]
print(covered_area(N, rectangles))
