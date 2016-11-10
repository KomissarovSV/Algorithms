class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        if head is None:
            self.size = 0
        else:
            self.size = 1

    def append(self, new_element):
        if self.tail:
            self.tail.next = new_element
            new_element.prev = self.tail
            self.tail = new_element
        else:
            self.head = new_element
            self.tail = new_element
        self.size += 1

    def size(self):
        return self.size

    def get_position(self, position):
        if position < 1:
            return None
        if self.head:
            current = self.head
            curPos = 1
            while current and curPos <= position:
                if curPos == position:
                    return current
                current = current.next
                curPos += 1
        return None

    def insert(self, new_element, position):

        elem = self.get_position(position)
        if elem is not None:
            new_element.prev = elem.prev
            new_element.next = elem
            elem.prev.next = new_element
            elem.prev = new_element
            if position == 1:
                self.head = new_element
            self.size += 1

    def delete(self, value):
        if self.size > 0:
            current = self.head
            while current.value != value and current.next:
                current = current.next
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                    current.next.prev = None
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                    current.prev.next = None

    def reverse(self):
        current = self.head
        while current:
            elem = current
            self.change(elem)
            current = current.next
        tmp2 = self.head
        self.head = self.tail
        self.tail = tmp2

    def output(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next

    def reverse2(self):
        start = self.head
        end = self.tail
        while start != end and start.next != end:
            curStart = start
            curEnd = end
            start = start.next
            end = end.prev
            self.change(curStart)
            self.change(curEnd)
        if start != end:
            self.change(end)
        self.change(start)
        tmp2 = self.head
        self.head = self.tail
        self.tail = tmp2

    def change(self,start):
        tmp = start.prev
        start.prev = start.next
        start.next = tmp
        return


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
print(ll.size," size must be 1")

ll.append(e2)
print(ll.size," size must be 2")
ll.append(e3)
print(ll.size," size must be 3")

# Test get_position
# Should print 3
print (ll.head.next.next.value," must be 3")

# Should also print 3
print (ll.get_position(3).value," must be 3")

# Test insert
ll.insert(e4,3)
print(ll.size," size must be 4")
# Should print 4 now
print (ll.get_position(3).value," must be 4")

# Test delete
ll.delete(1)
# Should print 2 now
print (ll.get_position(1).value," must be 2")
# Should print 4 now
print (ll.get_position(2).value," must be 4")
# Should print 3 now
print (ll.get_position(3).value," must be 3")

ll.append(Element(6))
ll.append(Element(7))
ll.append(Element(9))
ll.output()
ll.reverse2()
print()
ll.output()