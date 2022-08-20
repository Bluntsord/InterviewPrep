from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head

        mid = self.get_mid(head)
        first_half = self.sortList(head)
        second_half = self.sortList(mid)
        answer = self.merge(first_half, second_half)
        return answer

    def merge(self, first_head, second_head):
        if first_head is None and second_head is None:
            return None
        elif first_head is None:
            return second_head
        elif second_head is None:
            return first_head

        if first_head.val < second_head.val:
            curr_node = first_head
            answer = self.merge(first_head.next, second_head)
        else:
            curr_node = second_head
            answer = self.merge(first_head, second_head.next)

        curr_node.next = answer
        return curr_node

    def get_mid(self, head):
        tortoise = None
        hare = head

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next if tortoise is not None else head
            print(hare)
            print(hare.next)
            print(hare.next.next)
            print("=============")
            hare = hare.next.next

        mid = tortoise.next
        tortoise.next = None
        return mid

first_node = ListNode(1)
second_node = ListNode(2)
third_node = ListNode(3)
forth_node = ListNode(4)
fifth_node = ListNode(5)
sixth_node = ListNode(6)

first_node.next = second_node
second_node.next = third_node
third_node.next = forth_node
forth_node.next = fifth_node
fifth_node.next = sixth_node


solution = Solution()
head = first_node
print(solution.sortList(head))
while head is not None:
    print(head.val)
    head = head.next
