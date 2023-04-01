a = input()
l = list(map(int, input().split()))
result = []
for i in l:
    if i % 2 == 0:
        result.append(i)
        
print(*result)