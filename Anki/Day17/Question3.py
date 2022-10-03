from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_pointer, second_pointer = l1, l2
        next_val = first_pointer.val + second_pointer.val
        carry = 0 if next_val < 10 else 1
        next_val = next_val if next_val < 10 else next_val % 10
        head = ListNode(next_val)
        answer = head
        while first_pointer and second_pointer:
            next_val = first_pointer.val + second_pointer.val + carry
            if next_val > 9:
                next_val = next_val % 10
                carry = 1

            next_node = ListNode(next_val)
            head.next = next_node
            head = head.next
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        last_node = first_pointer if first_pointer else second_pointer
        while last_node:
            next_val = last_node.val + carry
            if next_val > 9:
                next_val = next_val % 10
                carry = 1
            next_node = ListNode(next_val)
            head.next = next_node
            head = next_node
            last_node = last_node.next

        return answer








