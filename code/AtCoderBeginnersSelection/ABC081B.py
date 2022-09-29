
N = int(input())
x = list(map(int, input().split()))

flg = True
count = 0
while(flg):
    for i in range(N): 
        if x[i] % 2 != 0 :
            flg = False
            break
        
        x[i] = x[i] / 2

    if flg:
        count += 1
        
print(count)
