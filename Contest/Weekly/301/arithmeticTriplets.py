class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        num_dict = {}
        for i in range(len(nums)):
            num_dict[nums[i]] = 1

        answer = 0
        for i in range(len(nums)):
            curr = nums[i]
            if curr + diff in num_dict and (curr + (diff * 2)) in num_dict:
                answer += 1
        return answer