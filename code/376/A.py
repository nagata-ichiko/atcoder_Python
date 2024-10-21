import sys
def count_candies(N, C, T):
    candies = 0
    last_time = -C  # Initialize to a value that allows the first candy to be received

    for time in T:
        if time - last_time >= C:
            candies += 1
            last_time = time

    return candies

input = sys.stdin.read
data = input().split()

N = int(data[0])
C = int(data[1])
T = list(map(int, data[2:2+N]))

print(count_candies(N, C, T))
