from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {head.val: 1}
        first_pointer = head
        second_pointer = head.next
        while first_pointer is not None:
            if second_pointer is None:
                first_pointer.next = second_pointer
                first_pointer = second_pointer
            elif second_pointer.val in visited:
                first_pointer.next = second_pointer.next
                second_pointer = second_pointer.next
            else:
                visited[second_pointer.val] = 1
                first_pointer = second_pointer
                second_pointer = second_pointer.next

        return head



