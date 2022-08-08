import queue as q
from itertools import groupby


class Solution:

    def findOrder(self, numCourses, prerequisites):
        return self.Kahns_algo(numCourses, prerequisites)



    def get_neighbours(self, node):
        if node in self.adj_list:
            return self.adj_list[node]
        return []


    def Kahns_algo(self, numCourses, prerequisites):
        if numCourses == 0:
            return []
        prerequisites = list(map(lambda x:(x[0], x[1]), prerequisites))
        prerequisites2 = list(map(lambda x:(x[1], x[0]), prerequisites))
        self.adj_list = {k: [v[1] for v in g] for k, g in groupby(sorted(prerequisites2),lambda x: x[0])}
        in_degree = {k: 0 for k in range(numCourses)}
        for curr in prerequisites:
            in_degree[curr[0]] += 1

        answer = []
        queue = q.Queue()
        for node, degree in in_degree.items():
            if degree == 0:
                queue.put(node)
        print(in_degree)
        print(self.adj_list)


        while not queue.empty():
            curr_node = queue.get()
            answer.append(curr_node)
            neighbours = self.get_neighbours(curr_node)

            for neighbour in neighbours:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.put(neighbour)

        for degree in in_degree.values():
            if degree != 0:
                return []

        return answer



numCourses = 3
prerequisites = [[1,0],[1,2],[0,1]]


numCourses2 = 7
prerequisites2 = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]

# numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]
solution = Solution()
print(solution.findOrder(numCourses2, prerequisites2))