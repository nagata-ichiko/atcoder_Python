N, Y = map(int,input().split())

end = 1

for acount in range(N + 1):
    if end == 0:
        break
    for bcount in range(N + 1):
        if N < acount + bcount:
            break
        ccount = N - acount - bcount
        buf = 10000 * acount + 5000 * bcount + 1000 * ccount

        if Y == buf:
            print(acount ,end=" ")
            print(bcount ,end=" ")
            print(ccount ,end=" ")
            end = 0
            break
        
if end == 1:
    print("-1 -1 -1")