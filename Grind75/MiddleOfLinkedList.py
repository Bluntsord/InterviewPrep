# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tortoise, hare = head, head
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next

        return tortoise
