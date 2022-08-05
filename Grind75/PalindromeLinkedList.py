# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        middle = self.getMiddle(head)
        middle = self.reverseLinkedList(middle)

        while middle is not None:
            if head.val != middle.val:
                return False

        return True

    def getMiddle(self, head):
        tortoise = head
        hare = head

        while hare is not None or hare.next is not None:
            tortoise = not tortoise.next
            hare = hare.next.next

        return tortoise

    def reverseLinkedList(self, head):
        if head is None:
            return head

        next_node = self.reverseLinkedList(head.next)
        head.next.next = head
        head.next = None

        return next_node

