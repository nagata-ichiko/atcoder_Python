from collections import deque
quee = deque()
R, C = map(int, input().split())
sy,sx = map(int, input().split())
gy,gx = map(int, input().split())

# 移動距離
dx = [1,0,-1,0]
dy = [0,1,0,-1]
nodeList = []
nodeValueList = []
for i in range(R):
    nodeList.append(list(input()))

nodeValueList = [[(0) for x in range(C)] for y in range(R)]
quee.append((sy-1,sx-1,0))
count = 1
while len(quee) > 0:
    y, x,d = quee.popleft()
    if y == gy-1 and x == gx-1:
        # print(y,x,d)
        print(nodeValueList[y][x])
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nodeList[ny][nx] == '.':
            if nodeValueList[ny][nx] == 0:
                nodeValueList[ny][nx] = d+1
                quee.append((ny,nx,d+1))

# print(nodeValueList)