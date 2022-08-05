class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        mapped = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                sum = nums[i] + nums[j]
                if sum in mapped:
                    temp = mapped[sum]
                    if i < j:
                        temp.add((i, j))
                    else:
                        temp.add((j, i))
                else:
                    curr = (i, j) if i < j else (j, i)
                    mapped[sum] = set()
                    mapped[sum].add(curr)


        answer = []
        for i in range(len(nums)):
            curr = nums[i]
            if -curr in mapped:
                curr_lists = mapped[-curr]
                curr_lists = list(filter(lambda x: i not in x, curr_lists))
                for temp in curr_lists:
                    first = nums[temp[0]]
                    second = nums[temp[1]]
                    another_temp = [curr, first, second]
                    another_temp.sort()
                    if another_temp not in answer:
                        answer.append(another_temp)


        return answer

nums = [-1,0,1,2,-1,-4]
solution = Solution()
print(solution.threeSum(nums))





