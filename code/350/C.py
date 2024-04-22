def check (list):
    flg = True
    for i in range(len(list)):
        if list[i] != i+1:
            flg = False
            break
    return flg

def sort(list):
    actionListA = []
    actionListB = []
    for i in range(len(list)):
        if list[i] == i+1:
            continue
        actionListA.append(i)
        buf = list[i]
        list[i] = list[buf-1]
        list[buf-1] = buf
        actionListB.append(buf-1)
    return actionListA, actionListB, list


N = int(input())
A = list(map(int, input().split()))

flg = False
actionListA = []
actionListB = []
while flg == False:
    # print(A)
    flg = check(A)
    if flg == True:
        break
    
    actionA, actionB, list = sort(A)
    A = list
    for i in range(len(actionA)):
        actionListA.append(actionA[i])
        actionListB.append(actionB[i])

if len(actionListA) == 0:
    print(0)
else:
    print(len(actionListA))
    for i in range(len(actionListA)):
        if actionListA[i] < actionListB[i]:
            print(actionListA[i]+1, actionListB[i]+1)
        else:
            print(actionListB[i]+1, actionListA[i]+1)