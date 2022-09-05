class Solution:
    def count_palindrome(self, curr_string, k):
        counter = 0
        self.k = k
        for i in range(len(curr_string)):
            counter += self.count_palindrome_around_centre(curr_string, i, i)
            counter += self.count_palindrome_around_centre(curr_string, i, i + 1)

        return counter

    def count_palindrome_around_centre(self, curr_string, left_mid, right_mid):
        counter = 0
        while left_mid >= 0 and right_mid < len(curr_string) and curr_string[left_mid] == curr_string[right_mid]:
            if right_mid - left_mid + 1 >= self.k:
                counter += 1
            left_mid -= 1
            right_mid += 1
        return counter

s = "aabc"
solution = Solution()
print(solution.count_palindrome(s, 2))