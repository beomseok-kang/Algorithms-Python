from stack import Stack

class SetOfStacks(object):

    def __init__(self, sizeEachStack):
        self.sets = []
        self.sizeEachStack = sizeEachStack
    
    def isEmpty(self):
        return not bool(self.sets)
    
    def push(self, value):
        length = len(self.sets)
        if length:
            if self.sets[length-1].size() == self.sizeEachStack:
                self.sets.append(Stack())
                self.sets[length].push(value)
            else:
                self.sets[length-1].push(value)
        else:
            self.sets.append(Stack())
            self.sets[0].push(value)
    
    def pop(self):
        length = len(self.sets)
        if length:
            if not self.sets[length-1].isEmpty():
                return self.sets[length-1].pop()
            else:
                self.sets.pop()
        else:
            print("Stack Set is empty.")

    def size(self):
        size = 0
        for i in self.sets:
            size += i.size()
        return size
    
    def peek(self):
        length = len(self.sets)
        if length:
            return self.sets[length-1].peek()
        else:
            print("Stack Set is empty.")

    def __repr__(self):
        return repr(self.sets)

s = SetOfStacks(10)
for i in range(30):
    s.push(i)
print(s)
while not s.isEmpty():
    s.pop()
print(s)