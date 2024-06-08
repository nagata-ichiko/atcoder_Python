S = input()

komozi = sum(1 for c in S if c.islower())
oomozi = sum(1 for c in S if c.isupper())


if komozi > oomozi:
    print(S.lower())
else:
    print(S.upper())

