a,b,k = map(int, input().split())

alist = []
blist = []
for i in range(1,a+1):
    if a % i == 0:
        alist.append(i)

for i in range(1,b+1):
    if b % i == 0:
        blist.append(i)

merge = set(alist) & set(blist)
print(sorted(merge,reverse=True)[k-1])