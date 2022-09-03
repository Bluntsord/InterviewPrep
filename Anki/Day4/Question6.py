from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        wish = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return wish

    def another_reverse(self, head):
        first_pointer, second_pointer = None, head

        while second_pointer is not None:
            third_pointer = second_pointer.next
            second_pointer.next = first_pointer
            first_pointer = second_pointer
            second_pointer = third_pointer

        return second_pointer
