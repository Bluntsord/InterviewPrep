from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head

        first, second = head, head.next
        even = second

        while second is not None and second.next is not None:
            first.next = first.next.next
            first = first.next

            second.next = first.next
            second = second.next

        first.next = even
        return head

firstNode = ListNode(1)
secondNode = ListNode(2)
thirdNode = ListNode(3)
fourthNode = ListNode(4)
fifthNode = ListNode(5)
sixthNode = ListNode(6)

firstNode.next = secondNode
secondNode.next = thirdNode
thirdNode.next = fourthNode
fourthNode.next = fifthNode
fifthNode.next = sixthNode

head = firstNode

solution = Solution()
print(solution.oddEvenList(firstNode))

while head is not None:
    print(head.val)
    head = head.next

