import typing


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: typing.Optional[ListNode], list2: typing.Optional[ListNode]) -> typing.Optional[ListNode]:
        if len(list1) == 0 or len(list2) == 0:
            return list2 if len(list1) == 0 else list1

        first_pointer = 0
        second_pointer = 0
        final_list = []

        while first_pointer != len(list1) or second_pointer != len(list2):
            first_curr = list1[first_pointer]
            second_curr = list2[second_pointer]

            if first_curr >= second_curr:
                curr = first_curr
                first_pointer += 1
            else:
                curr = second_curr
                second_pointer += 1

            final_list.append(curr)

        if first_pointer == len(list1):
            final_list.extend(list2[second_pointer:])
        else:
            final_list.extend(list1[first_pointer:])

        return final_list




