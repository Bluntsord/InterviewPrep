from typing import *

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        acc = Counter(s[:len(p)])
        answer = []
        s_len, p_len = len(s), len(p)
        self.reference_dict = Counter(p)

        if s_len < p_len:
            return answer
        elif self.check_if_all_in(acc):
            answer.append(0)

        for i in range(1, s_len - p_len + 1):
            if s[i - 1] in acc and acc[s[i - 1]] == 1:
                acc.pop(s[i - 1])
            else:
                acc[s[i - 1]] -= 1

            next = s[i + len(p) - 1]
            if next in acc:
                acc[next] += 1
            else:
                acc[next] = 1

            if self.check_if_all_in(acc):
                answer.append(i)

        return answer

    def check_if_all_in(self, first_dict):
        return first_dict == self.reference_dict

s = "abab"
p = "ab"

# s = "cbaebabacd"
# p = "abc"
solution = Solution()
print(solution.findAnagrams(s, p))