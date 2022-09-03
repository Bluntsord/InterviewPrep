from typing import *


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Create edges between all emails of a name. Since this is island detection, we
        #  only need to connect one edge between all emails
        self.edge_list = {}
        for account in accounts:
            if len(account) == 2:
                self.edge_list[account[1]] = [account[1]]
                continue

            for i in range(1, len(account) - 1):
                first_email = account[i]
                second_email = account[i + 1]

                self.edge_list[first_email] = [second_email] + self.edge_list.get(first_email, [])
                self.edge_list[second_email] = [first_email] + self.edge_list.get(second_email, [])


        print(self.edge_list)
        self.answer = []
        self.visited = {}

        for account in accounts:
            curr_account = self.dfs(account)
            if curr_account: self.answer.append(curr_account)

        return self.answer

    def dfs(self, account):
        name = account[0]
        stack = [account[1]]
        answer = set()

        if account[1] in self.visited:
            return []
        else:
            self.visited[account[1]] = 1

        while len(stack) != 0:
            curr_email = stack.pop()
            answer.add(curr_email)
            neighbours = self.edge_list[curr_email]

            for neighbour in neighbours:
                if neighbour not in self.visited:
                    self.visited[neighbour] = 1
                    stack.append(neighbour)

        answer = list(answer)
        answer.sort()
        answer = [name] + answer
        return answer



accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]]

solution = Solution()
print(solution.accountsMerge(accounts))
