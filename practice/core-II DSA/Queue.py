# Implementing queue using deque from collections
from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.append(val)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self.container.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self.container[0]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
