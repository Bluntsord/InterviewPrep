import random
from typing import *
from functools import lru_cache

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:

        @lru_cache(None)
        def dp(left_pointer, right_pointer, piles):
            if left_pointer == right_pointer and piles == 1:
                return float('inf')
            elif piles == 1:
                if right_pointer - left_pointer + 1 == k:
                    return sum_stones(left_pointer, right_pointer)
                return float('inf')

            answer = float('inf')
            for i in range(left_pointer + 1, right_pointer):
                curr = dp(left_pointer, i, 1) + dp(i + 1, right_pointer, k - 1)
                answer = min(curr, answer)

            return answer

        @lru_cache(None)
        def sum_stones(left_pointer, right_pointer):
            answer = sum(stones[left_pointer: right_pointer])
            return answer

        return dp(0, len(stones) - 1, 1)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # create a new linked list to store the result
    result = ListNode()
    curr = result

    # create a min heap to store the nodes from the input lists
    heap = []

    # add the first node from each list to the heap
    for i in range(len(lists)):
        if lists[i]:
            heap.append(lists[i])

    # keep looping until the heap is empty
    while heap:
        # get the node with the smallest value from the heap
        minNode = min(heap, key=lambda x: x.val)

        # add the node to the result linked list
        curr.next = minNode
        curr = curr.next

        # remove the node from the heap and add its next node (if any)
        heap.remove(minNode)
        if minNode.next:
            heap.append(minNode.next)

    # return the result linked list (excluding the dummy node at the beginning)
    return result.next


solution = Solution()
# stones = [random.randint(1, 30) for i in range(100)]
stones = [3, 2, 4, 1]
print(stones)
k = 2
print(solution.mergeStones(stones, k))
print(m)

