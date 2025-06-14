# Reversing a string using Stack from deque
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isempty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def rev(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    reversed_str = ''
    while not stack.isempty():
        reversed_str += stack.pop()
    return reversed_str

if __name__ == "__main__":
    n = input("Enter the string: ")
    revstr = rev(n)
    print("Reversed string:", revstr)
