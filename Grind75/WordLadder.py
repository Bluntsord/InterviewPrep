from typing import *
from collections import defaultdict
import queue as q


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        if endWord not in wordList:
            return 0

        neighbours = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                neighbours[pattern].add(word)

        visited = {beginWord: 1}
        queue = q.Queue()
        queue.put(beginWord)
        level = 0
        while not queue.empty():
            for i in range(queue.qsize()):
                curr_word = queue.get()
                if curr_word == endWord:
                    return level + 1
                for j in range(len(curr_word)):
                    curr_pattern = curr_word[:j] + "*" + curr_word[j + 1:]
                    current_neighbours = neighbours[curr_pattern]
                    for current_neighbour in current_neighbours:
                        if current_neighbour not in visited:
                            visited[current_neighbour] = 1
                            queue.put(current_neighbour)
            level += 1

        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
solution = Solution()
print(solution.ladderLength(beginWord, endWord, wordList))