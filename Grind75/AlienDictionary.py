from typing import *
import queue as q
from collections import defaultdict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        self.out_degree = defaultdict(set)
        self.in_degree = dict(Counter({c: 0 for word in words for c in word}))

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in self.out_degree[c]:
                        self.out_degree[c].add(d)
                        self.in_degree[d] += 1
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""
        #
        # for first_word, second_word in zip(words, words[1:]):
        #     for c, d in zip(first_word, second_word):
        #         if c != d:
        #             if d not in self.out_degree[c]:
        #                 self.out_degree[c].add(d)
        #                 self.in_degree[d] += 1
        #             break
        #     else:  # Check that second word isn't a prefix of first word.
        #         if len(second_word) < len(first_word): return ""

        queue = q.Queue()
        temp_stack = {key for key, value in self.in_degree.items() if value == 0}
        for node in temp_stack:
            queue.put(node)

        answer = ""

        while not queue.empty():
            curr_node = queue.get()
            answer = answer + curr_node
            neighbours = self.out_degree[curr_node]

            for neighbour in neighbours:
                self.in_degree[neighbour] -= 1
                if self.in_degree[neighbour] == 0:
                    queue.put(neighbour)

        if len(answer) < len(self.in_degree):
            return ""
        return answer





words = ["wrt","wrf","er","ett","rftt","te"]
solution = Solution()
print(solution.alienOrder(words))