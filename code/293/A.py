t = input()
count =len(t)
result = ''
for i in range(0,int(count),2):
    result += t[i+1]
    result += t[i]    
print(result)