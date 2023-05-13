N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mydict  = {}
mydict[0] = 0
c = 1
for i in A:
    mydict[c] = i
    c+=1
    
max_k_list = [kv[0] for kv in mydict.items() if kv[1] == max(mydict.values())]

c = 0
for i in range(len(B)):
    if B[i]  in max_k_list:
        c+=1

if c == 0:
    print("No")
else:
    print("Yes")
    
