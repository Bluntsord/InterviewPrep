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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeKLists(lists):
    # create a new linked list to store the result
    result = ListNode()
    curr = result

    # create a min heap to store the nodes from the input lists
    heap = []

    # add the first node from each list to the heap
    for i in range(len(lists)):
        if lists[i]:
            heap.append(lists[i])

    # keep looping until the heap is empty
    while heap:
        # get the node with the smallest value from the heap
        minNode = min(heap, key=lambda x: x.val)

        # add the node to the result linked list
        curr.next = minNode
        curr = curr.next

        # remove the node from the heap and add its next node (if any)
        heap.remove(minNode)
        if minNode.next:
            heap.append(minNode.next)

    # return the result linked list (excluding the dummy node at the beginning)
    return result.next





solution = Solution()
lists = [[1,4,5],[1,3,4],[2,6]]
print(mergeKLists(lists))
