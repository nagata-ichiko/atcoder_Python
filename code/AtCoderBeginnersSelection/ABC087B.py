from unittest import result

A = int(input())
B = int(input())
C = int(input())
X = int(input())

result = 0

for acount in range(0,A + 1):
    for bcount in range(0, B + 1):
        for ccount in range(0, C + 1):
            buf = 500 * acount + 100 * bcount + 50 * ccount
            if X == buf:
                result += 1
                
print(result)
