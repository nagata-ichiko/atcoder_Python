N = int(input())
flg = True
position = [0,0,0]
for i in range(N):
    t1,x1,y1 = position
    t2,x2,y2 = map(int,input().split())
    
    dt = t2 - t1
    distance = abs(x2 - x1) + abs(y2 - y1)
    
    position = [t2,x2,y2]
    
    if dt < distance or (dt - distance) % 2 != 0:
        flg = False
        break

if flg:
    print("Yes")
else:
    print("No")
    
    