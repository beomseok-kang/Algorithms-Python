from linkedListFIFO import LinkedListFIFO
from node import Node

class KthFromLast(LinkedListFIFO):
    def find_kth_to_last(self, k):
        p1, p2 = self.head, self.head
        i = 0
        while p1:
            if i > k-1:
                try:
                    p2 = p2.pointer
                except AttributeError:
                    break
            p1 = p1.pointer
            i += 1
        return p2.value

k = KthFromLast()
for i in range(1, 11):
    k.addNode(i)
k._printList()

k_from_last = k.find_kth_to_last(3)

print(k_from_last)