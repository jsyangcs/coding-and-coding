from collections import deque


class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = deque()

    def push(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.popleft()

    def empty(self):
        return len(self.items) == 0


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve1(self, head):
        val_stack = Stack()
        while head:
            val_stack.push(head.val)
            head = head.next

        while not val_stack.empty():
            print(val_stack.pop())

    def solve2(self, head):
        if head.next is not None:
            self.solve2(head.next)
        print(head.val)


def test():
    s = Solution()
    llist = Node(0, Node(1, Node(2)))
    s.solve1(llist)
    print("---")
    s.solve2(llist)


if __name__ == "__main__":
    test()
