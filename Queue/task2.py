from Stack.task2 import Stack

class Queue(object):
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self,new_elem):
        self.inbox.append(new_elem)

    def dequeue(self):
        if len(self.outbox) == 0:
            length = len(self.inbox)
            while length > 0:
                self.outbox.append(self.inbox.pop())
                length -= 1
        return self.outbox.pop()

class Queue2(object):
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self,new_elem):
        self.inbox.push(new_elem)

    def dequeue(self):
        if self.outbox.size() == 0:
            while self.inbox.size() > 0:
                self.outbox.push(self.inbox.pop())
        return self.outbox.pop()


q = Queue2()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())

q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

print(q.dequeue())
print(q.dequeue())

q.enqueue(7)
q.enqueue(8)
q.enqueue(9)

print(q.dequeue())
print(q.dequeue())