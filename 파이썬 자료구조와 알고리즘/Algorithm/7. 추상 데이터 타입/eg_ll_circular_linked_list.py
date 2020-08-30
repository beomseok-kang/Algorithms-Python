from linkedListFIFO import LinkedListFIFO
from node import Node

class CircularLinkedListFIFO(LinkedListFIFO):
    def _add(self, value):
        self.length += 1
        node = Node(value, self.head)
        if self.tail:
            self.tail.pointer = node
        self.tail = node

def isCircularll(ll):
    p1 = ll.head
    p2 = ll.head

    while p2:
        try:
            p1 = p1.pointer
            p2 = p2.pointer.pointer
        except:
            break
        
        if p1 == p2:
            return True
    return False

ll = LinkedListFIFO()
for i in range(10):
    ll.addNode(i)
print(isCircularll(ll))

lcirc = CircularLinkedListFIFO()
for i in range(10):
    lcirc.addNode(i)
print(isCircularll(lcirc))