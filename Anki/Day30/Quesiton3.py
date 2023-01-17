from typing import *

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tortoise = hare = head
        for _ in range(n - 1):
            hare = hare.next

        while hare.next is not None:
            hare = hare.next
            tortoise = tortoise.next

        tortoise.next = tortoise.next.next
        return head





