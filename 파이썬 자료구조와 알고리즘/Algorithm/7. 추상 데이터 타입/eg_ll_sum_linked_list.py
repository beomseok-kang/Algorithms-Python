from linkedListFIFO import LinkedListFIFO

def sum_linked_list(ll1, ll2):
    # 연결 리스트: 숫자 2671의 경우 1 7 6 2 순으로 되어있다.
    ll_result = LinkedListFIFO()

    node_1 = ll1.head
    node_2 = ll2.head

    def node_val_or_zero(node):
        if not node is None and node.value:
            return node.value
        else:
            return 0
    def node_pointer_or_None(node):
        if not node is None and node.pointer:
            return node.pointer
        else:
            return None

    pending = 0
    while node_1 or node_2:
        sum_val = node_val_or_zero(node_1) + node_val_or_zero(node_2) + pending
        pending = 0
        if sum_val < 10:
            ll_result.addNode(sum_val)
        else:
            ll_result.addNode(sum_val - 10)
            pending += 1
        node_1 = node_pointer_or_None(node_1)
        node_2 = node_pointer_or_None(node_2)
    
    return ll_result

list_2671 = [1, 7, 6, 2]
list_355 = [5, 5, 3]

ll_2671 = LinkedListFIFO()
ll_355 = LinkedListFIFO()
for i in list_2671:
    ll_2671.addNode(i)
for i in list_355:
    ll_355.addNode(i)

ll_result = sum_linked_list(ll_2671, ll_355)
ll_result._printList()

###########

class LinkedListFIFOYield(LinkedListFIFO):
    def _printList(self):
        node = self.head
        while node:
            yield node.value
            node = node.pointer

def sumlls(l1, l2):
    lsum = LinkedListFIFOYield()
    dig1 = l1.head
    dig2 = l2.head
    pointer = 0

    while dig1 and dig2:
        d1 = dig1.value
        d2 = dig2.value
        sum_d = d1 + d2 + pointer
        if sum_d > 9:
            pointer = sum_d // 10
            lsum.addNode(sum_d % 10)
        else:
            lsum.addNode(sum_d)
            pointer = 0
        dig1 = dig1.pointer
        dig2 = dig2.pointer
    
    if dig1:
        sum_d = pointer + dig1.value
        if sum_d > 9:
            lsum.addNode(sum_d % 10)
        else:
            lsum.addNode(sum_d)
        dig1 = dig1.pointer
    
    if dig2:
        sum_d = pointer + dig2.value
        if sum_d > 9:
            lsum.addNode(sum_d % 10)
        else:
            lsum.addNode(sum_d)
        dig2 = dig2.pointer
    
    return lsum

l1 = LinkedListFIFOYield()
l2 = LinkedListFIFOYield()

l1.addNode(1)
l1.addNode(7)
l1.addNode(6)
l1.addNode(2)

l2.addNode(5)
l2.addNode(5)
l2.addNode(3)

lsum = sumlls(l1, l2)
l = list(lsum._printList())
for i in reversed(l):
    print(i, end="")
print()

###########