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


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())