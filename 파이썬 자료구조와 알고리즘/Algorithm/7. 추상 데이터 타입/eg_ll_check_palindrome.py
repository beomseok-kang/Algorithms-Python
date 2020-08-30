from linkedListFIFO import LinkedListFIFO

def ll_check_palindrome(string):
    str_temp = ''
    for i in string.lower():
        if not i in ' \'"':
            str_temp += i
        else:
            continue
    
    mid_i = len(str_temp) // 2
    from_fwd_ll = LinkedListFIFO()
    from_back_ll = LinkedListFIFO()

    for i in range(mid_i):
        from_fwd_ll.addNode(str_temp[i])
        from_back_ll.addNode(str_temp[-1-i])
    
    fwd_node = from_fwd_ll.head
    back_node = from_back_ll.head
    while fwd_node and back_node:
        if fwd_node.value == back_node.value:
            fwd_node = fwd_node.pointer
            back_node = back_node.pointer
        else:
            return False
    return True

########

def isPal(l1):
    if len(l1) < 2:
        return True
    if l1[0] != l1[-1]:
        return False
    return isPal(l1[1:-1])

def checkllPal(ll):
    node = ll.head
    l = []
    while node is not None:
        l.append(node.value)
        node = node.pointer
    return isPal(l)

ll = LinkedListFIFO()
l1 = [1,2,3,2,1]
for i in l1:
    ll.addNode(i)
print(checkllPal(ll))
ll.addNode(2)
print(checkllPal(ll))

########

palindrome = 'Madam I\'m Adam'
not_palindrome = 'Hello World!'

print(ll_check_palindrome(palindrome))
print(ll_check_palindrome(not_palindrome))