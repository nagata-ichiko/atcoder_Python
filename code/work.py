n, m = map(int, input().split())
li = list(map(int, input().split()))
result = []
for i in range(1,n+1):
    result.append(str(i))  

for i in li:
    result[i-1],result[i] = result[i],result[i-1]


sss= ""
for i in result:
    sss += i
    sss += " "
    
print(sss)