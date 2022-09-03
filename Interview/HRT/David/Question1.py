from typing import *
import queue as q

class Solution:
    def solution(self, first_deck, second_deck):
        first_queue = q.Queue()
        for i in first_deck:
            first_queue.put(i)

        second_queue = q.Queue()
        for i in second_deck:
            second_queue.put(i)

        while not first_queue.empty() and not second_queue.empty():
            first_card = first_queue.get()
            second_card = second_queue.get()

            if first_card >= second_card:
                first_queue.put(first_card)
                first_queue.put(second_card)
            else:
                second_queue.put(first_card)
                second_queue.put(second_card)

