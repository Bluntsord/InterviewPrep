class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first_head, prev_last = None, None
        stack, count = [], k
        while head is not None:
            print(head.val, count)
            if count == 1:
                if first_head is None:
                    first_head = head
                next_node = head.next

                if prev_last is not None:
                    prev_last.next = head

                while len(stack) != 0:
                    head.next = stack.pop()
                    head = head.next
                    if len(stack) == 0:
                        prev_last = head
                head.next = next_node
                head = head.next
                count = k
            else:
                stack.append(head)
                head = head.next
                count -= 1
        return first_head


