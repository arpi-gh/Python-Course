from Class_LinkedList import LinkedList
from Class_Node import Node
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
    print('insert node2 after node1: ', ls,)
    ls.insert_before(node4, node3)
    print('insert node3 before node4: ', ls)
    ls.insert_after(node4, node5)
    print('insert node5 after node4: ', ls)
    ls.insert_after(node5, node7)
    print('insert node7 after node5: ', ls)
    ls.insert_before(node7, node6)
    print('insert node6 before node7: ', ls)
    ls.delete(node7)
    print('delete node7: ', ls)
    ls.delete(node1)
    print('delete node1: ', ls)
    ls.delete(node5)
    print('delete node5: ', ls)
    print('final list:', ls)
    print('length of the list: ', len(ls))
    print('The list is empty: ', ls.is_empty())
    print('___________________________')
    ls.head = Node(0)
    print(ls)
    # ls.tail = 8
