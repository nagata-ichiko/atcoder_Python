count = int(input())
l = list(map(int, input().split()))
mydict  = {}
mydict[0] = 0
c = 1
for i in l:
    mydict[c] = i
    c+=1
for key,value in mydict.items():
    mydict[value] = 0    
result  = []
for key, value in mydict.items():
    if value == 0:
        continue
    result.append(key)
print(len(result))
print(*result)