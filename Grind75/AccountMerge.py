from typing import List


class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.nodeMap = {}
        self.answer = {}
        self.nameMap = {}
        self.visited = {}
        for account in accounts:
            for email in account[1:]:
                if account[1] not in self.nodeMap:
                    self.nodeMap[account[1]] = set()
                if email not in self.nodeMap:
                    self.nodeMap[email] = set()
                self.nodeMap[account[1]].add(email)
                self.nodeMap[email].add(account[1])
                self.nameMap[email] = account[0]

        answer = []
        for node in self.nodeMap:
            if node in self.visited:
                continue
            curr_island = list(self.dfs(node))
            curr_island.sort()
            curr_name = self.nameMap[node]
            temp = [curr_name]
            temp.extend(curr_island)
            answer.append(temp)
            self.visited[node] = 1

        answer.sort(key= lambda x: x[0])
        return answer


    def dfs(self, email_node):
        stack = [email_node]
        island = set()
        while len(stack) != 0:
            curr_node = stack.pop()
            island.add(curr_node)
            if curr_node not in self.nodeMap:
                continue
            neighbours = self.nodeMap[curr_node]

            for neighbour in neighbours:
                if neighbour not in self.visited:
                    stack.append(neighbour)
                    self.visited[neighbour] = 1

        return list(island)

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
solution = Solution()
print(solution.accountsMerge(accounts))









