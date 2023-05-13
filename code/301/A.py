N = int(input())
S = input()

T_count = 0
A_count = 0

for c in S:
    if c == 'T':
        T_count += 1
        if T_count > A_count:
            winner = 'T'
    elif c == 'A':
        A_count += 1
        if A_count > T_count:
            winner = 'A'

print(winner)
