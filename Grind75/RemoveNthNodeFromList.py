import queue as q
from typing import *


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        queue = q.Queue()
        curr = head
        for i in range(n):
            queue.put(curr)
            curr = curr.next

        while curr is not None:
            queue.put(curr.next)
            curr = curr.next
            if curr is None:
                break
            queue.get()

        first = queue.get()
        node_to_remove = queue.get()
        last = queue.get()

        first.next = last
        node_to_remove.head = None

        return head


