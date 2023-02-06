
def numCalc(n):
    a = []
    for i in range(1,n+1):
        if n % i == 0:
            a.append(i)
    a = set(a)
    return len(a)

N = int(input())

count = 0
for i in range(1,N+1):
    if numCalc(i) == 8 and i % 2 == 1:
        count+=1
        
print(count)