from typing import *


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        print("===========")
        print(nums)
        nums = self.merge_sort(nums)
        print(nums)
        print("===========")
        return nums

    def bubbleSort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums) - i):
                if j == len(nums) - 1:
                    pass
                elif nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            print(nums)
        return nums

    def merge_sort(self, nums):
        if len(nums) == 1 or len(nums) == 0:
            return nums
        mid_point = int(len(nums)/2)
        first_half = self.merge_sort(nums[:mid_point])
        second_half = self.merge_sort(nums[mid_point:])
        answer = self.merge_recursive(first_half, second_half)
        return answer


    def merge_recursive(self, first_sorted, second_sorted):
        if len(first_sorted) == 0:
            return second_sorted
        elif len(second_sorted) == 0:
            return first_sorted

        curr_first = first_sorted[0]
        curr_second = second_sorted[0]
        answer = []
        if curr_first < curr_second:
            answer.append(curr_first)
            wish = self.merge_recursive(first_sorted[1:], second_sorted)
        else:
            answer.append(curr_second)
            wish = self.merge_recursive(first_sorted, second_sorted[1:])
        answer.extend(wish)
        return answer


    def merge_iterative(self, first_sorted, second_sorted):
        first_pointer = 0
        second_pointer = 0
        answer = []
        while first_pointer < len(first_sorted) and second_pointer < len(second_sorted):
            curr_first = first_sorted[first_pointer]
            curr_second = second_sorted[second_pointer]

            if curr_first <= curr_second:
                answer.append(curr_first)
                first_pointer += 1
            else:
                answer.append(curr_second)
                second_pointer += 1

        if first_pointer == len(first_sorted):
            answer.extend(second_sorted[second_pointer:])
        else:
            answer.extend(first_sorted[first_pointer:])
        return answer

    def quick_sort(self, nums):
        self.nums = nums


nums = [5,1,1,2,0,0]
ans1 = [0,0,1,1,2,5]

nums2 = [5,2,3,1]
ans2 = [1,2,3,5]

nums3 = [0,0,1,1,2,5]
ans3 = [0,0,1,1,2,5]

nums4 = [7,2,5,3,5,6,10,12]
ans4 = [2, 3, 5, 5, 6, 7, 10, 12]


test_cases = [nums, nums2, nums3, nums4]
test_answers = [ans1, ans2, ans3, ans4]
test_cases = list(zip(test_cases, test_answers))

print(test_cases)
solution = Solution()
result = True

for test_case in test_cases:
    first = solution.sortArray(test_case[0])
    second = test_case[1]
    temp = first == second
    result = result and temp

print(result)



