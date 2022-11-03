def solution(figure, field):



def sum_matrix(first_matrix, second_matrix):
    answer = [[-1 for _ in range(len(first_matrix[0]))] for _ in range(len(first_matrix))]
    for i in range(len(first_matrix)):
        for j in range(len(first_matrix[0])):
            answer[i][j] = first_matrix[i][j] + second_matrix[i][j]

    return answer

def check_valid(matrix):
    answer = False
    for i in reversed(range(len(matrix))):
        curr_row = True
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                return False
            elif matrix[i][j] == 0:
                curr_row = False
        answer = answer or curr_row

    return answer
