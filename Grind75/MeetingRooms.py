class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        temp = intervals.copy()
        temp.sort(key=lambda x:x[0])
        print(temp)
        for i in range(len(temp) - 1):
            if temp[i][1] > temp[i + 1][0]:
                return False
        return True

a = [[5, 8], [6, 8], [3, 8]]
solution = Solution()
print(solution.canAttendMeetings(a))