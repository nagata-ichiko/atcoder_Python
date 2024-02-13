N, K = map(int, input().split())
A = list(map(int, input().split()))

result = 0

buff = [0] * (N - 1)

for i in range(0, N - 1):
	if i == 0:
		buff[i] = 0
	else:
		buff[i] = buff[i - 1]
  
    # 数がなくなるまで、数値を超えるまで
	while buff[i] < (N - 1) and ( A[buff[i]+1] - A[i]) <= K:
		buff[i] += 1

for i in range(0, N-1):
	result += (buff[i] - i)
print(result)