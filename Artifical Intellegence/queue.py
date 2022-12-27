class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:

    def __init__(self):
        self.front = self.rear = None
    def isEmpty(self):
        return self.front == None

def _inc(self, idx):
    if idx + 1== self.size:
        return 0
    else:
        return idx + 1
    queue._inc = _inc

# Method to add an item to the queue
def EnQueue(self, item):
    temp = Node(item)

    if self.rear == None:
        self.front = self.rear = temp
        return
    self.rear.next = temp
    self.rear = temp

# Method to remove an item from queue
def DeQueue(self):

    if self.isEmpty():
        return
    temp = self.front
    self.front = temp.next

    if (self.front == None):
        self.rear = None

    if __name__ == '__main__':
        q = Queue()
        q.EnQueue(2)
        q.EnQueue(4)
        q.EnQueue(6)
        q.DeQueue()
        q.DeQueue()
        q.DeQueue()
        q.EnQueue(10)
        q.EnQueue(20)
    print("Queue Front " + str(q.front.data))
    print("Queue Rear " + str(q.rear.data))
