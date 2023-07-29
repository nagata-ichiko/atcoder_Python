def is_adjacent(A, B):
    # 3x3の盤面
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # 盤面上のAとBの位置を見つける
    position_A = position_B = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == A:
                position_A = (i, j)
            if board[i][j] == B:
                position_B = (i, j)

    # AとBの位置が隣接しているかチェック
    if position_A and position_B:
        i_A, j_A = position_A
        i_B, j_B = position_B

        # 同じ行に存在し、列が1つしか違わない場合は隣接していると判断
        if i_A == i_B and abs(j_A - j_B) == 1:
            return "Yes"
    
    return "No"

input_line = input().split()
A = int(input_line[0])
B = int(input_line[1])

print(is_adjacent(A, B))
