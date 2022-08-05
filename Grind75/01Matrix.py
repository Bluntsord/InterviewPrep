from queue import Queue


class Solution(object):
    def __init__(self):
        self.memo = {}
        self.mat = None

    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        visited = set()
        queue = Queue()
        self.mat = mat
        answer = [[-1] * n for _ in range(m)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    answer[i][j] = 0
                    queue.put((i, j))
                    visited.add((i, j))

        dist = 0
        while not queue.empty():
            for i in range(queue.qsize()):
                row, col = queue.get()
                if mat[row][col] == 1:
                    answer[row][col] = dist
                for neighbour in self.validNeighbour((row, col)):
                    if neighbour not in visited:
                        queue.put(neighbour)
                        visited.add(neighbour)

            dist += 1
        return answer

    def validNeighbour(self, coord):
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        answer = list(map(lambda x: (coord[0] + x[0], coord[1] + x[1]), directions))
        answer = list(filter(self.valid_coord, answer))
        return answer

    def valid_coord(self, coord):
        if 0 <= coord[0] < len(self.mat) and 0 <= coord[1] < len(self.mat[0]):
            return True
        return False




mat = [[0,0,0],[0,1,0],[0,0,0]]
solution = Solution()
print(solution.updateMatrix(mat))

def createZeroMatrix(self, n):
    """
    type n: int
    :rtype: List[List[int]]
    """
    answer = [[0] * n for _ in range(n)]
    return answer

def createIdentityMatrix(self, n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        answer[i][i] = 1
    return answer


createIdentityMatrix(4)