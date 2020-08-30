from queue import Queue

class AnimalShelter(object):
    def __init__(self):
        DogQ = Queue()
        CatQ = Queue()
        self.set = [DogQ, CatQ]
    
    def size(self):
        return (self.set[0].size(), self.set[1].size())

    def enqueue_dog(self, name):
        self.set[0].enqueue(name)
    def dequeue_dog(self):
        value = self.set[0].dequeue()
        if value is not None:
            return value
        else:
            print("Got no Dog...")
    
    def enqueue_cat(self, name):
        self.set[1].enqueue(name)
    def dequeue_cat(self):
        value = self.set[1].dequeue()
        if value is not None:
            return value
        else:
            print("Got no Cat...")

    def peek_dog(self):
        value = self.set[0].peek()
        if value is not None:
            return value
        else:
            print("Got no Dog...")
    def peek_cat(self):
        value = self.set[1].peek()
        if value is not None:
            return value
        else:
            print("Got no Cat...")

    def __repr__(self):
        return repr(self.set)

s = AnimalShelter()
s.enqueue_cat('Kitty')
s.enqueue_cat('Nabi')
s.dequeue_cat()
s.enqueue_dog('Dangdang')
s.dequeue_dog()
s.dequeue_dog()
print(s)
