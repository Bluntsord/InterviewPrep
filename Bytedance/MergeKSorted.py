# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class WrapperNode():
    def __init__(self, listNode):
        self.node = listNode

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution(object):
    def mergeKLists(self, lists):
        pq = PriorityQueue()
        for baseNode in lists:
            wrapperNode = WrapperNode(baseNode)
            pq.put(wrapperNode)

        firstNode = pq.get().node
        if firstNode is None:
            return None

        prevNode = firstNode
        nextNode = prevNode.next
        if nextNode is None:
            return firstNode
        pq.put(wrapperNode(nextNode))

        while not pq.empty():
            nextNode = pq.get().node
            if nextNode.next is not None:
                pq.put(wrapperNode(nextNode.next))
            prevNode.next = nextNode
            prevNode = nextNode

        return firstNode


