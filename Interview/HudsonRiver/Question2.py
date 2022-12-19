def Rhombic_cipher(table):
    matrix = []
    for i in range(len(table)):
        matrix.append([])
        for j in range(len(table[0])):
            matrix[i].append(table[i][j])

    diag = []
    for i in range(len(matrix)):
        diag.append(get_diag_of_matrix((i, 0), matrix))
        diag.append(get_diag_of_matrix((0, i), matrix))

    diag = [x for x in diag if len(x) > 1]
    return diag


def get_diag_of_matrix(coord, matrix):
    diag = []
    x, y = coord
    while x < len(matrix) and y < len(matrix[0]):
        diag.append(matrix[x][y])
        x -= 1
        y += 1

        x %= len(matrix)
        y %= len(matrix[0])
    return diag
