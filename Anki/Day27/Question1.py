from typing import *

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
        wish_left = self.sortList(head)
        wish_right = self.sortList(mid)

        return self.merge(wish_left, wish_right)

    def get_mid(self, head):
        tortoise, hare = None, head

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next if tortoise is not None else head
            hare = hare.next.next

        mid = tortoise.next
        tortoise.next = None
        return mid

    def merge(self, first, second):
        if first is None and second is None:
            return None
        elif first is None:
            return second
        elif second is None:
            return first

        if first.val > second.val:
            first, second = second, first

        next_node = self.merge(first.next, second)
        first.next = next_node

        return first

solution = Solution()
list_one = [4,2,1,3]
list_two = [-1,5,3,4,0]
list_three = []
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
