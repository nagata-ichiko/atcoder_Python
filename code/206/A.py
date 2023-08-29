def find_day(N):
    total = 0
    day = 0
    
    while total < N:
        day += 1
        total += day
    
    return day

# テスト
N = int(input())
print(find_day(N))
