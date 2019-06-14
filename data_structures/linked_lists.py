class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # make None as the default value for next.
        self.prev = None


node1 = Node(4)
node2 = Node(2)
node3 = Node(3)
node4 = Node(5)

node1.next = node2

node2.next = node3
node2.prev = node1

node3.next = node4
node3.prev = node2

node4.prev = node3


def count_nodes(head):
    # assuming that head != None
    count = 1
    current = head
    while current.next is not None:
        current = current.next
        count += 1
    return count


print(count_nodes(node1))
