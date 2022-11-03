from typing import *
import queue as q

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        queue = q.Queue()
        queue.put(start)
        answer = 1
        visited = {}

        while not queue.empty():
            for i in range(queue.qsize()):
                curr_word = queue.get()
                neighbours = list(filter(lambda x: self.get_distance(curr_word, x) == 1, bank))

                for neighbour in neighbours:
                    if neighbour == end:
                        return answer
                    elif neighbour in visited:
                        continue
                    visited[neighbour] = curr_word
                    queue.put(neighbour)
            answer += 1
        return -1



    def get_distance(self, first_word, second_word):
        answer = 0
        for i in range(len(first_word)):
            if first_word[i] != second_word[i]:
                answer += 1

        return answer

solution = Solution()
start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
print(solution.minMutation(start, end, bank))
