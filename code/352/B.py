S = input()
T = input()

count =0
result = []


for i in range(len(T)):
    if S[count] == T[i]:
        count += 1
        result.append(i+1)

print(" ".join(map(str, result)))

