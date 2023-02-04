n = int(input()) 
pair = [list(map(int, input().split())) for i in range(n)]
for a, b in pair:
    print(a + b)
