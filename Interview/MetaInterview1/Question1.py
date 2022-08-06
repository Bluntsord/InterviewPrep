from typing import *

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first_node = ListNode(float('-inf'))
        temp = first_node
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                first_node.next = list1
                list1 = list1.next
            else:
                first_node.next = list2
                list2 = list2.next
            first_node = first_node.next

        first_node.next = list1 if list1 is not None else list2

        return temp.next
