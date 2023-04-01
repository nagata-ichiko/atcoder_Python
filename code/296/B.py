def find_piece_position(strings):
    for i, row in enumerate(strings):
        if '*' in row:
            column = row.index('*')
            row_number = 8 - i
            column_letter = chr(ord('a') + column)
            return column_letter + str(row_number)

strings = []
for i in range(8):
    strings.append(input())
piece_position = find_piece_position(strings)
print(piece_position)