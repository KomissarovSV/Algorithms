class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        if head.value:
            self.size = 1
        else:
            self.size = 0

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element
        self.size += 1

    def delete_first(self):
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            self.size -= 1
            return deleted_element
        else:
            return None


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(Element(top))

    def push(self, new_element):
        self.ll.insert_first(Element(new_element))

    def pop(self):
        return self.ll.delete_first().value

    def size(self):
        return self.ll.size


def test(sequence):
    stack = Stack()
    for ch in sequence:
        if ch is "(" or ch is "[" or ch is "{":
            stack.push(ch)
        elif ch is ")":
            if stack.pop() is not "(":
                return False
        elif ch is "]":
            if stack.pop() is not "[":
                return False
        elif ch is "}":
            if stack.pop() is not "{":
                return False
    if stack.size() == 0:
        return True
    else:
        return False


sequence = "({123}(ASD[ASD{ASD}]))"
print(test(sequence))
