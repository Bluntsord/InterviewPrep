from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = self.get_mid(head)
        first_half = self.sortList(head)
        second_half = self.sortList(mid)
        return self.merge(first_half, second_half)

    def merge(self, first_head, second_head):
        if first_head is None and second_head is None:
            return None
        elif first_head is None:
            return second_head
        elif second_head is None:
            return first_head

        if first_head.val < second_head.val:
            wish = self.merge(first_head.next, second_head)
            first_head.next = wish
            return first_head

        wish = self.merge(first_head, second_head.next)
        second_head.next = wish
        return second_head

    def get_mid(self, head):
        tortoise = None
        hare = head

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next

        mid = tortoise.next
        tortoise.next = None
        return mid