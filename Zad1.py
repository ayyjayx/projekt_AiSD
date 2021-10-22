# ZADANIE 1 PROJEKT AiSD

from typing import Any


class Node:
    value: Any
    # next: 'Node'
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


class LinkedList:
    head: Node
    def __init__(self):
        self.head = None


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        return " -> ".join(nodes)


    def push(self, value:Any) -> None:
        add_node = Node(value)
        add_node.next = self.head
        self.head = add_node

    def append(self, value:Any) -> None:
        add_node = Node(value)
        current = self.head
        while current.next:
            current = current.next
        else:
            current.next = add_node

    def node(self, at: int) -> Node:
        current = self.head
        counter = 0
        while current:
            if counter == at:
                return current
            counter += 1
            current = current.next

    def insert(self, value: Node, after: Node) -> None:
        p = after.next
        after.next = value
        value.next = p

    def pop(self) -> Any:
        x = self.head
        p = self.head.next
        self.head = p
        return x

    def remove_last(self) -> Any:
        current = self.head
        while current.next.next:
            current = current.next
        else:
            x = current.next
            current.next = None
            return x

    def remove(self, after: Node) -> Any:
        p = after.next.next
        after.next = p

    def length(self):
        x = self.head
        counter = 0
        while x:
            x = x.next
            counter += 1
        return counter


list_ = LinkedList()
assert list_.head == None
# print(list_)

list_.push('1')
list_.push('0')

# print(list_)

assert str(list_) == '0 -> 1'

list_.append('9')
list_.append('10')

# print(list_)

assert str(list_) == '0 -> 1 -> 9 -> 10'

# print(list_.node(2))

middle_node = list_.node(at=1)
list_.insert(Node('5'), after=middle_node)

# print(list_)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()
# print(list_)
assert first_element == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
print(list_)
assert last_element == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)
print(list_)
assert str(list_) == '1 -> 5'

print(list_.length())
