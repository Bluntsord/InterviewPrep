from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        even = odd.next
        even_head = even
        while odd is not None and even is not None:
            odd.next = even.next
            odd = even.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return head
