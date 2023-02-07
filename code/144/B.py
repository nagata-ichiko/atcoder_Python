num = int(input())
result = False

for i in range(1,10):
    for c in range(1,10):
        buf = i * c
        if num == buf:
            result = True
            break
        

if result:
    print("Yes")
else:
    print(("No"))            