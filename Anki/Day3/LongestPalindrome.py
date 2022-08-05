class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_dict = Counter(s)
        have_odd = False
        answer = 0
        for key in s_dict:
            if s_dict[key] % 2 == 0:
                answer += s_dict[key]
            else:
                if not have_odd:
                    answer += 1
                answer += (s_dict[key] - 1)

        return answer

