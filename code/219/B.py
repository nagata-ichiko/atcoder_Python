
A = input()
B = input()
C = input()

# 文字列を取得1文字ずつリストに格納
T = list(input())

for i in range(len(T)):
    if T[i] == "1":
        print(A, end="")
    elif T[i] == "2":
        print(B, end="")
    else:
        print(C, end="")


