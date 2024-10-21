import sys
from collections import deque

def calculate_minimum_operations(N, Q, operations):
    total_operations = 0
    left_hand = 1
    right_hand = 2

    for H, T in operations:
        if H == 'L':
            current = left_hand
            other_hand = right_hand
        else:
            current = right_hand
            other_hand = left_hand

        if current == T:
            continue

        # BFSを用いて最小ステップ数を計算（他方の手が保持しているパーツを通過不可）
        visited = [False] * (N + 1)  # パーツ番号は1からNまで
        queue = deque()
        queue.append((current, 0))  # (現在の位置, ステップ数)
        visited[current] = True
        found = False
        min_steps = 0

        while queue and not found:
            pos, steps = queue.popleft()
            for move in [-1, 1]:  # 反時計回りと時計回りの移動
                next_pos = pos + move
                if next_pos < 1:
                    next_pos = N
                elif next_pos > N:
                    next_pos = 1

                if next_pos == other_hand:
                    continue  # 他方の手が保持しているパーツは通過不可

                if not visited[next_pos]:
                    if next_pos == T:
                        min_steps = steps + 1
                        found = True
                        break
                    visited[next_pos] = True
                    queue.append((next_pos, steps + 1))

        total_operations += min_steps

        # 手の位置を更新
        if H == 'L':
            left_hand = T
        else:
            right_hand = T

    return total_operations

def main():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    Q = int(input_data[1])
    operations = []
    for i in range(Q):
        H = input_data[2 + 2 * i]
        T = int(input_data[3 + 2 * i])
        operations.append((H, T))
    
    result = calculate_minimum_operations(N, Q, operations)
    print(result)

if __name__ == "__main__":
    main()