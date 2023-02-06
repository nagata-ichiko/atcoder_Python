import io
import sys
import statistics
import math
import queue
import heapq

s = input()
ans = 0
a = ["A", "T", "C", "G"]
for i in range(len(s)):
    cnt = 0
    for j in range(i, len(s)):
        if s[j] not in a:
            break
        cnt += 1
    ans = max(ans, cnt)
print(ans)