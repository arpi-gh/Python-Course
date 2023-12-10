from Class_Node import Node


class LinkedList:
    __attr_count = 0

    @classmethod
    def __increment_count(cls):
        cls.__attr_count += 1

    @classmethod
    def __decrement_count(cls):
        if cls.__attr_count != 0:
            cls.__attr_count -= 1

    def __init__(self):
        self.__head = Node(None)
        self.__tail = Node(None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, data: Node):
        if type(data) != Node:
            raise ValueError('The head should be a node. ')
        data.next = self.__head.next
        self.__head = data

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self,data: Node):
        if type(data) != Node:
            raise ValueError('The tail should be a node. ')
        data.prev = self.__tail.prev
        self.__tail = data

    def __len__(self) -> int:
        return self.__attr_count

    def is_empty(self) -> bool:
        return len(self) == 0  # True if empty, False if not empty

    def prepend(self, data: Node):  # insert at the beginning, prev is None, next is None
        self.__head.data = data.data
        self.__increment_count()

    def append(self, data: Node):  # insert at the end, prev is None, next is None
        self.__tail.data = data.data
        self.__increment_count()

    def search(self, target_data, beginning=1):
        # No point in this actually if it's gonna be outside. Useful inside the class
        if beginning == 1:
            current_node = self.__head
            while current_node.data != target_data.data:
                current_node = current_node.next
        elif beginning == -1:
            current_node = self.__tail
            while current_node.data != target_data.data:
                current_node = current_node.prev
        else:
            raise ValueError('The beginning must be either 1 or -1.')
        return current_node

    def insert_after(self, target_data: Node, data: Node):
        if self.__head.data == target_data.data:
            tmp = self.__head.next
            self.__head.next = data
            data.prev = self.__head
            tmp.prev = data
            data.next = tmp
        elif self.__tail.data == target_data.data:
            tmp = self.__tail
            self.__tail = data
            data.prev = tmp
            tmp.next = data
        else:
            target = self.search(target_data)
            tmp = target.next
            target.next = data
            data.prev = target
            data.next = tmp
            tmp.prev = data
        self.__increment_count()

    def insert_before(self, target_data: Node, data: Node):
        if self.__head.data == target_data.data:
            tmp = self.__head
            self.__head = data
            data.next = tmp
            tmp.prev = data
        elif self.__tail.data == target_data.data:
            tmp = self.__tail.prev
            self.__tail.prev = data
            data.prev = tmp
            tmp.next = data
            data.next = self.__tail
        else:
            target = self.search(target_data, beginning=-1)
            temp = target.prev
            target.prev = data
            data.prev = temp
            data.next = target
            data.prev.next = data
        self.__increment_count()

    def delete(self, data: Node):
        if data.data == self.__head.data:
            self.__head = self.__head.next
            self.__head.prev = None
            self.__decrement_count()
        elif data.data == self.__tail.data:
            self.__tail = self.__tail.prev
            self.__tail.next = None
            self.__decrement_count()
        else:
            target = self.search(data)
            target.prev.next = target.next
            target.next.prev = target.prev
            del target
            self.__decrement_count()

    def __str__(self):
        print_string = f'[{self.__head}, {self.__tail}]'
        if len(self) != 0:
            current = self.__head
            print_string = '['
            while current != self.__tail:
                print_string += f'{current},'
                current = current.next
            print_string += f'{self.__tail}]'
        return print_string


