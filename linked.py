class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_val):
        current = self.head
        if self.head:
            while self.next:
                current = current.next
            current.next = new_val
        else:
            self.head = new_val

p = Element(5)

link = LinkedList()
link.append(p)

while link.head:
    print(link.head)
            