N, Q = map(int,input().split())
a = [list(map(int, input().split())) for l in range(N + Q)]
 
for count in range(Q):    
    # N番目の値を縦軸 横軸に
    Y = a[N + count][0]
    X = a[N + count][1]
    print(a[Y-1][X])
    