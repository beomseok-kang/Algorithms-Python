import heapq

class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        # 작은 값부터 반환하기 때문에 priority가 높을 수록 인덱스 내에 들어가는 값이 작아야 한다.
        # 이를 -priority로 구현한다.
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "Item({0!r})".format(self.name)

q = PriorityQueue()

q.push(Item('most prior'), 3)
q.push(Item('prior'), 2)
q.push(Item('not prior'), 1)

print(q.pop())
print(q.pop())
print(q.pop())