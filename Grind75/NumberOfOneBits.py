class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer = 0
        while n != 0:
            answer += 1
            n &= (n - 1)

        return answer