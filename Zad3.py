from Zad1 import LinkedList
import Zad2
from typing import Any

class Queue:
    _storage: LinkedList
    # _storage2: Stack


    def __init__(self):
        self._storage = LinkedList()
        LinkedList.__init__(self)

    def __str__(self):
        node = self._storage.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        values = ', '.join(str(v) for v in nodes)
        return str(values)

    def enqueue(self, element: Any) -> None:
        Zad2.Stack.push(self, element)

    def dequeue(self) -> Any:
        x = self._storage.head
        p = self._storage.head.next
        self._storage.head = p
        return x

queue = Queue()
assert queue._storage.len() == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
print('Kolejka po dodaniu 3 klientow:\n', queue)

assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()
print('Kolejka po osbluzeniu pierwszego klienta:\n', queue)

assert str(client_first) == 'klient1'
assert str(queue) == 'klient2, klient3'
assert queue._storage.len() == 2
