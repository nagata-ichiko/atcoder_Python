import collections

a = input()
l = list(map(str, input().split()))
c = collections.Counter(l)

print(c.most_common()[-1][0])
