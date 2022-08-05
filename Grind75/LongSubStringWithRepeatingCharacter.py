class Solution(object):
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #
    #     prefix_string = [0 for _ in range(len(s))]
    #     prefix_string[len(s) - 1] = 1
    #     # Key of visited is letter and values is position
    #     visited = {s[len(s) - 1 ]: len(s) - 1}
    #
    #     for i in range(len(s) - 2, -1, -1):
    #         curr_letter = s[i]
    #         if curr_letter not in visited:
    #             prefix_string[i] = prefix_string[i + 1] + 1
    #             visited[curr_letter] = i
    #         else:
    #             stop_pos = visited[curr_letter]
    #             temp = min(stop_pos - i, prefix_string[i + 1] + 1)
    #             prefix_string[i] = temp
    #             visited[curr_letter] = i
    #
    #     print(prefix_string)
    #     return max(prefix_string)
    #


    def lengthOfLongestSubstring(self, s):
        visited = set()
        curr_longest = 0
        curr = 0
        left_ptr = 0

        for i in range(len(s)):
            curr_letter = s[i]
            while curr_letter in visited:
                visited.remove(s[left_ptr])
                left_ptr += 1
            curr = len(visited) + 1
            visited.add(curr_letter)
            curr_longest = max(curr_longest, curr)

        return curr_longest
s = "abba"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))








