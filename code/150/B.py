import io
import sys
import statistics
import math
import queue
import heapq

num = int(input())
s = input()

ans = 0
a = "ABC"
for i in range(0,num-2):
    if s[i] == "A":
        if s[i+1] == "B":
            if s[i+2] == "C":
                ans+=1
print(ans)