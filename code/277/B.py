N = int(input())
dict = {}
for i in range(1,N):
    dict[i] = []

for i in range(N):
    a, b = map(int, input().split())
    dict.setdefault(a, []).append(b)
    dict.setdefault(b, []).append(a)
Mastercount = 0

# キーで辞書を逆ソート
sortDict = sorted(dict.items(), key=lambda x: x[0], reverse=True)

array = [1]
used = set()
max =1
while len(array)>0:
    key = array.pop()
    for v in dict[key]:
        if v > max:
            max = v
        if v in used:
            continue
        used.add(v)
        array.append(v)

print(max)