class HashTableLL(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self._createHashTable()

    def _createHashTable(self):
        for i in range(self.size):
            self.slots.append([])
    
    def _find(self, item):
        return item % self.size # mod
    
    def _add(self, item):
        index = self._find(item) # slot index
        self.slots[index].append(item)

    def _delete(self,item):
        index = self._find(item)
        self.slots[index].remove(item)

    def _print(self):
        for i in range(self.size):
            print("slot ({0})".format(i))
            print(self.slots[i])
    
H1 = HashTableLL(3)
for i in range(20):
    H1._add(i)

H1._print()
H1._delete(0)
H1._delete(1)
H1._delete(2)

print('\n0, 1, 2 삭제\n')

H1._print()