from typing import *
from collections import defaultdict

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        most_popular_video, creator_dict = {}, defaultdict(int)
        for i in range(len(creators)):
            temp = most_popular_video.get(creators[i], (float("-inf"), 0))
            if views[i] > temp[0]:
                most_popular_video[creators[i]] = (views[i], ids[i])
            elif views[i] == temp[0] and ids[i] < temp[1]:
                most_popular_video[creators[i]] = (views[i], ids[i])
            creator_dict[creators[i]] += views[i]

        max_key = max(creator_dict.values())
        print(max_key)
        print(most_popular_video)
        answer = set(creators[i] for i in range(len(creators)) if creator_dict[creators[i]] == max_key)
        answer = list(map(lambda x: [x, most_popular_video[x][1]], list(answer)))

        return answer


solution = Solution()
creators = ["a"]
ids = ["a"]
views = [0]
print(solution.mostPopularCreator(creators, ids, views))
