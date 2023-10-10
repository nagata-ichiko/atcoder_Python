N, M = map(int, input().split())
dict = {}
for i in range(1,N):
    dict[i] = []

for i in range(M):
    a, b = map(int, input().split())
    dict.setdefault(a, []).append(b)
    dict.setdefault(b, []).append(a)
Mastercount = 0
# キーで辞書をソート
sortDict = sorted(dict.items(), key=lambda x: x[0])
for key, value in sortDict:
    count = 0
    for v in value:
        if  v < key:
            if count != 0:
                Mastercount -= 1
                count = 0
                break
        if  key > v:
            count += 1
            Mastercount += 1

print(Mastercount)