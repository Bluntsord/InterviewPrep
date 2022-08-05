class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort(key= lambda x: x[0])
        answer = self.merge_intervals(intervals)

        return answer

    def merge_intervals(self, intervals):
        stack = [intervals[0]]
        if len(intervals) == 0:
            return [[]]

        for start, end in intervals[1:]:
            # Merge interval
            if stack[-1][1] >= start:
                stack[-1][1] = max(stack[-1][1], end)
            else:
                stack.append([start, end])

        return stack



nums = [[1,2],[3,5],[6,7],[8,10],[12,16]]
nums2 = [[1, 5]]
a = [4,8]
b = [2, 8]

solution = Solution()
print(solution.insert(nums, a))