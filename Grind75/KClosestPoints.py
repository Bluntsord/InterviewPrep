class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        euclid_dist = list(map(lambda x: (x, x[0]**2 + x[1] **2), points))
        self.points_list = euclid_dist
        self.k = k
        answer = self.quickSelect(0, len(self.points_list) - 1)
        answer = list(map(lambda x: x[0], answer))
        return answer

    def quickSelect(self, low: int, high: int) -> list:
        pivot_point = self.points_list[high]
        pivot_euclid_dist = pivot_point[1]
        p_ptr = low

        if p_ptr == self.k:
            return self.points_list[0: self.k]

        for i in range(low, high):
            curr_euclid = self.points_list[i][1]
            if curr_euclid < pivot_euclid_dist:
                self.points_list[i], self.points_list[p_ptr] = self.points_list[p_ptr],self.points_list[i]
                p_ptr += 1
        self.points_list[high], self.points_list[p_ptr] = self.points_list[p_ptr], self.points_list[high]

        if p_ptr > self.k:
            return self.quickSelect(low, p_ptr - 1)
        elif p_ptr < self.k:
            return self.quickSelect(p_ptr + 1, high)
        return self.points_list[0: p_ptr]


solution = Solution()