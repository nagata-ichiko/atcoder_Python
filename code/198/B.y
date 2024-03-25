def isKaibun(s):
    return s == s[::-1]

A = int(input())

buf = A
count = 0
result = isKaibun(str(buf))
while result == False:
    buf = "0" + str(buf)
    result = isKaibun(str(buf))
    count += 1
    if count> len(str(A*2)):
        result = False
        break
    
 

if result:
    print("Yes")
else:
    print("No")




