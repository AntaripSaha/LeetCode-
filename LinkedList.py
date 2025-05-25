class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def insert_at_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')


ll = LinkedList()
ll.insert_at_head(10)
ll.insert_at_tail(2)
ll.insert_at_tail(4)
ll.insert_at_head(5)
ll.print_list()


