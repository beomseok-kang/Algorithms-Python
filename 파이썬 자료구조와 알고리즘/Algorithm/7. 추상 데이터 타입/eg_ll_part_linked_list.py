from linkedListFIFO import LinkedListFIFO

def part_linked_list(ll, n):
    result_ll = LinkedListFIFO()
    ll_temp = ll
    
    node = ll_temp.head
    i = 0
    while node:
        if node.value < n:
            result_ll.addNode(node.value)
            ll_temp.deleteNode(i)
        elif node.value == n:
            ll_temp.deleteNode(i)
        else:
            i += 1
        node = node.pointer
    
    result_ll.addNode(n)

    node = ll_temp.head
    while node:
        result_ll.addNode(node.value)
        node = node.pointer
    
    return result_ll

def part_linked_list_answer_book(ll, n):
    more = LinkedListFIFO()
    less = LinkedListFIFO()

    node = ll.head
    while node:
        item = node.value
        if item < n:
            less.addNode(item)
        elif item > n:
            more.addNode(item)
        
        node = node.pointer
    
    less.addNode(n)
    nodemore = mode.head
    while nodemore:
        less.addNode(nodemore.value)
        nodemore = nodemore.pointer
    return less

ll_test = LinkedListFIFO()
for i in [4,7,2,9,8,5,2,4,1]:
    ll_test.addNode(i)

part_linked_list(ll_test, 5)._printList()


