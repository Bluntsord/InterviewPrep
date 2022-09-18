class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {-1: 0, 0: 1}

