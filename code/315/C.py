N = int(input())
a = [list(map(int, input().split())) for l in range(N)]

array = sorted(a, key=lambda x: x[1], reverse=True)
topAji = array[0][0]
secondAji = 0
dict = {}
for i in range(N):
    a,b = array[i]
    dict.setdefault(a, []).append(b)
    if topAji != a:
        secondAji = a
        break


result = 0
result2 = 0

if 2 <= len(dict.get(topAji)):
    result = dict.get(topAji)[0] + dict.get(topAji)[1]/2

if secondAji != 0:
    result2 = dict.get(topAji)[0] + dict.get(secondAji)[0]

if result < result2:
    result = result2
print(int(result))
