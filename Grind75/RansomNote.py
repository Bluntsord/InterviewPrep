from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        my_dict = Counter(magazine)
        other_dict = Counter(ransomNote)

        for keys in other_dict.keys():
            if keys not in my_dict or my_dict[keys] < other_dict[keys]:
                return False

        return True

solution = Solution()
print(solution.canConstruct("a","abcb"))