from queue import PriorityQueue

def solution(m, n, queries):
    removed_rows = set()
    removed_cols = set()

    def helper():
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i in removed_rows or j in removed_cols:
                    continue
                return i * j
        return

    answer = []
    for query in queries:
        if len(query) == 1:
            temp = helper()
            print(temp)
            answer.append(helper())
        else:
            if query[0] == 1:
                removed_rows.add(query[1])
            elif query[0] == 2:
                removed_cols.add(query[1])

    return answer


queries = [[1,3], [1,2], [1,4], [0], [1,1], [0]]
n, m = 5, 1
print(solution(m, n, queries))