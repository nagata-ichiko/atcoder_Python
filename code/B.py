def distance_between_points(p, q):
    points = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    distances = [3, 1, 4, 1, 5, 9]

    # ポイント間の距離を計算
    total_distances = [0]
    for d in distances:
        total_distances.append(total_distances[-1] + d)

    # 入力された2つの点のインデックスを取得
    p_index = points.index(p)
    q_index = points.index(q)

    # 2つの点間の距離を計算
    return abs(total_distances[p_index] - total_distances[q_index])


p, q = input().strip().split()
print(distance_between_points(p, q))
