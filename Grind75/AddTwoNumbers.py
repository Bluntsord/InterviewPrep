from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(l1, l2, None)

    def helper(self, first_list, second_list, carry):
        if first_list is None and second_list is None and carry is None:
            return None
        elif first_list is None and second_list is None:
            return ListNode(1)
        else:
            curr_val = 0
            curr_val += first_list.val if first_list is not None else 0
            curr_val += second_list.val if second_list is not None else 0
            carry = 0
            if curr_val >= 10:
                curr_val = 0
                carry = 1
            curr_node = ListNode(curr_val)
            next_first = first_list.next if first_list is not None else first_list
            next_second = second_list.next if second_list is not None else second_list
            next_carry = ListNode(1) if carry == 1 else None
            next = self.helper(next_first, next_second, next_carry)
            curr_node.next = next
            return curr_node




