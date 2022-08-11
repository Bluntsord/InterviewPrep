from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head)

    def helper(self, head):
        if head is None:
            return None
        elif head.next is None:
            return head

        first, second, third = head, head.next, head.next.next
        first.next = self.helper(third)
        second.next = head
        return second


first = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)
sixth = ListNode(6)
seven = ListNode(7)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth


solution = Solution()
head = solution.swapPairs(first)

while head is not None:
    print(head.val)
    head = head.next

