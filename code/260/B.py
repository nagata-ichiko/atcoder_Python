N,X,Y, Z = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

NotOKDict1  = {}
NotOKDict2  = {}
NotOKDict3  = {}
OKDict = {}
# 不合格者名簿
for i in range(N):
    NotOKDict1[i] = A[i]
    NotOKDict2[i] = B[i]
    NotOKDict3[i] = A[i]+B[i]

NotOKDict1 = dict(sorted(NotOKDict1.items(), key=lambda x:x[1], reverse=True))
NotOKDict2 = dict(sorted(NotOKDict2.items(), key=lambda x:x[1], reverse=True))
NotOKDict3 = dict(sorted(NotOKDict3.items(), key=lambda x:x[1], reverse=True))

count=0
# 数学
for key in list(NotOKDict1.keys()):
    if(count != X):
        count+=1
        OKDict[key] = key
        NotOKDict1.pop(key)
        NotOKDict2.pop(key)
        NotOKDict3.pop(key)

count = 0
# 英語
for key in list(NotOKDict2.keys()):
    if(count != Y):
        count+=1
        OKDict[key] =key
        NotOKDict1.pop(key)
        NotOKDict2.pop(key)
        NotOKDict3.pop(key)
count = 0

# 合計
for key in list(NotOKDict3.keys()):
    if(count != Z):
        count+=1
        OKDict[key] = NotOKDict3.get(key)
        NotOKDict1.pop(key)
        NotOKDict2.pop(key)
        NotOKDict3.pop(key)


OKDict = dict(sorted(OKDict.items()))
for key in list(OKDict.keys()):
    print(key+1) 
