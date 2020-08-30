class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer
    
    def getData(self):
        return self.value

    def getNext(self):
        return self.pointer

    def setData(self, newData):
        self.value = newData

    def setNext(self, newPointer):
        self.pointer = newPointer