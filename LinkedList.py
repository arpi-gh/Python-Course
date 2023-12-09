class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return f'prev: {self.prev}, data: {self.data}, next: {self.next}'

    def __str__(self):
        return f'<{self.data}>'


class LinkedList:
    attr_count = 0


    @classmethod
    def increment_count(cls):
        cls.attr_count += 1

    @classmethod
    def decrement_count(cls):
        if cls.attr_count != 0:
            cls.attr_count -= 1

    def __init__(self):
        self.linked_list = None
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __len__(self) -> int:  # implement later
        return self.attr_count

    def is_empty(self) -> bool:
        return len(self) == 0  # True if empty, False if not empty

    def prepend(self, data: Node):  # insert at the beginning, prev is None, next is None
        self.head.data = data.data
        self.increment_count()

    def append(self, data: Node):  # insert at the end, prev is None, next is None
        self.tail.data = data.data
        self.increment_count()

    def insert_after(self, target_data: Node, data: Node):
        not_found_data = True
        current_node = self.head
        while not_found_data:
            if current_node.data == target_data.data:
                if current_node.next is not None:
                    temp = current_node.next
                    current_node.next = data
                    data.prev = current_node
                    data.next = temp
                    data.next.prev = data
                else:
                    temp = self.tail
                    self.tail = data
                    self.tail.prev = temp
                    temp.next = self.tail
                self.increment_count()
                not_found_data = False
            current_node = current_node.next

    def insert_before(self, target_data: Node, data: Node):
        not_found_data = True
        current_node = self.tail
        while not_found_data:
            if current_node.data == target_data.data:
                if current_node.prev is not None:
                    temp = current_node.prev
                    current_node.prev = data
                    data.prev = temp
                    data.next = current_node
                    data.prev.next = data
                else:
                    temp = self.head
                    self.head = data
                    self.head.next = temp
                    temp.prev = self.head
                self.increment_count()
                not_found_data = False
            current_node = current_node.prev

    def delete(self, data: Node):
        not_found_data = True
        if data.data == self.head.data:
            self.head = self.head.next
            self.head.prev = None
            self.decrement_count()
        elif data.data == self.tail.data:
            self.tail = self.tail.prev
            self.tail.next = None
            self.decrement_count()
        else:
            current_node = self.head
            while not_found_data:
                if current_node.data == data:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    del current_node
                    self.decrement_count()
                not_found_data = False



    # def pop(self, data: Node):   # didn't work
    #     self.delete(data)
    #     # return data

    def __str__(self):
        print_string = f'{self.head},'
        current_node = self.head
        while current_node != self.tail and current_node.next is not None:
            print_string += f'{current_node.next},'
            current_node = current_node.next
        print_string = print_string[0:-1]
        return print_string


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    ls = LinkedList()
    print('initial list:', ls)
    ls.prepend(node1)
    print('prepend node1: ', ls)
    ls.append(node4)
    print('append node4: ', ls)
    ls.insert_after(node1, node2)
    print('insert node2 after node1: ', ls)
    # print(node1.next)
    # print(node2.next)
    # print(node4.prev)
    print('insert node3 before node4: ', ls)
    ls.insert_before(node4, node3)
    print('insert node5 after node4: ', ls)
    ls.insert_after(node4, node5)
    print('insert node7 after node5: ', ls)
    ls.insert_after(node5, node7)
    print('insert node6 before node7: ', ls)
    ls.insert_before(node7, node6)
    print('delete node7: ', ls)
    ls.delete(node7)
    print('delete node1: ', ls)
    ls.delete(node1)
    print('delete node5: ', ls)
    ls.delete(node5)

    # print('head:', ls.head)
    # print('tail:', ls.tail)
    print(ls)
    print(len(ls))
    print(ls.is_empty())

