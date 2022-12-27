class Node:
def __init__(self, data = None):
self.data = data
self.next = None

class LinkedList:
def __init__(self):
self.head = None

def push(self, val):
    new_node = Node(val)
    # no node currently
    if self.head is None:
        self.head =new_node
        return
    # otherwise, reach the end and then insert
    last = self.head
    while last.next is not None:
        last = last.next
        last.next = new_node

def pop(self):
    if self.head is None:
        raise Exception("cannot pop. No value.")
        # case where there is only one node
        if self.head.next is None:
            print("case 1")
            val = self.head.val
            self.head=None
            return val
        print ("case 2")
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next

def insert(self, index, val):
    new_node = Node(val)
    if index == 0:
        print("case 1")
        new_node.next = self.head
        self.head = new_node
        return
    print("case 2")
    temp = self.head
    counter = 0
    while temp is not None adn counter < index:
        prev = temp
        temp = temp.next
        counter += 1
        # print(counter)
        # print ("Will insert after: ",prev.val)
        prev.next = new_node
        new_node.next = temp
        LinkedList.insert = insert
        