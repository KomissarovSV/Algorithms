class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)

    def min(self):
        minimum = self.peek()
        for item in self.storage:
            if minimum > item:
                minimum = item
        return minimum

    def max(self):
        maximum = self.peek()
        for item in self.storage:
            if maximum < item:
                maximum = item
        return maximum


# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())

q2 = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(4)
q.enqueue(8)
q.enqueue(-5)
print(q.max())
print(q.min())

