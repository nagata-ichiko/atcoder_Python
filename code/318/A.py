def count_full_moon_days(N, M, P):
    days = [M + i * P for i in range(N//P + 1) if M + i * P <= N]
    return len(days)

# 標準入力から値を受け取る
N, M, P = map(int, input().split())
print(count_full_moon_days(N, M, P))
