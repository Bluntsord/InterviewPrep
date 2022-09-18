from typing import *
import queue as q


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = q.PriorityQueue()
        for node in lists:
            if node:
                pq.put((node.val, node))

        head_val, head = pq.get()
        pq.put((head.next.val, head.next))
        curr = head

        while not pq.empty():
            next_node_val, next_node = pq.get()
            curr.next = next_node
            curr = curr.next
            next_node = next_node.next
            if next_node:
                pq.put((next_node.next.val, next_node.next))

        return head









