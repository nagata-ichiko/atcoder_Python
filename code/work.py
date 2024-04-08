N = int(input())
minimu_dict = {}

for i in range(0, N):
    A,C = map(int, input().split())
    if C in minimu_dict:
        minimu_dict[C] = min(minimu_dict[C], A)
    else:
        minimu_dict[C] = A
ans =-1

# 全検索 
for i in minimu_dict.values():
    ans = max(ans, i)
    
print(ans)