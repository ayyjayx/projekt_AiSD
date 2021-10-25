from Zad1 import LinkedList, Node
from typing import Any

class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __str__(self):
        node = self._storage.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        values = '\n'.join(str(v) for v in reversed(nodes)) + '\n__\n'
        return str(values)

    def push(self, element: Any) -> None:
        add_node = Node(element)
        current = self._storage.head
        if current == None:
            self._storage.head = add_node
        else:
            while current.next:
                current = current.next
            else:
                current.next = add_node

    def pop(self) -> Any:
        current = self._storage.head
        while current.next.next:
            current = current.next
        else:
            x = current.next
            current.next = None
            return x

stack = Stack()
assert stack._storage.len() == 0

stack.push(3)
stack.push(10)
stack.push(1)

print('\n\nStos po pushnieciu 3, 10 i 1:\n')
print(stack)
assert stack._storage.len() == 3

top_value = stack.pop()
print('Stos po usunieciu elementu na szczycie:\n')
print(stack)
assert str(top_value) == '1'

assert stack._storage.len() == 2
