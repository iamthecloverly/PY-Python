class Node:
    def _init_(self, data=None):
        self.data = data
        self.next = None


class SStack:
    def __init__(self):
        self.head = None

    def _init_(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node()
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next


# Example usage
stack = SStack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.display()  # Output: 4 3 2 1

stack.pop()
stack.pop()

stack.display()  # Output: 2 1

print(stack.peek())
