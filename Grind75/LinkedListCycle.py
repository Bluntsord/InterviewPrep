# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tortoise = head.next
        hare = head.next.next

        while hare.val != tortoise.val:
            if hare is None or hare.next is None:
                return True
            tortoise = tortoise.next
            hare = hare.next.next

        return False
