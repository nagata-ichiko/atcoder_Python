def solve():
    n = int(input())
    s = input()
    k = s.count("1")
    if k & 1:
        return -1
    adj = s.count("11")
    if k >= 4 or k == 0 or not adj:
        return k // 2
    if n == 3:
        return -1
    if s == "0110":
        return 3
    return 2
t = int(input())
for _ in range(t):
    print(solve())