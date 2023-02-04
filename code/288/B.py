itr, outnum = map(int, input().split())
 
S = []
for i in range(outnum):
    S.append(input())
S.sort()
 
for s in range(outnum):
    print(S[s])