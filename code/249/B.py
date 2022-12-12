a = input()
lst = [x for x in a]
seen = []
unique_list = [x for x in lst if x not in seen and not seen.append(x)]
countUp = 0
countDown = 0

for str in lst:    
    if(str.islower()):
        countDown += 1
        
    if(str.isupper()):
        countUp += 1
        
if(countUp != 0):
  if(countDown != 0):
    # 重複
    if(len(lst) != len(unique_list)):
        print("No")
    else:
        print("Yes")
else:
    print("No") 
    


