import sys
import math

input = sys.stdin.read
data = input().split()

N = int(data[0])
points = [(int(data[i*2+1]), int(data[i*2+2])) for i in range(N)]

total_cost = 0.0
current_x, current_y = 0, 0

for x, y in points:
    dx = current_x - x
    dy = current_y - y
    distance = math.sqrt(dx * dx + dy * dy)
    total_cost += distance
    current_x, current_y = x, y

total_cost += math.sqrt(current_x ** 2 + current_y ** 2)

print(total_cost)
