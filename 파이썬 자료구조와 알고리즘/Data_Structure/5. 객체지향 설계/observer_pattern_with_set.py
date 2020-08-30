class Subscriber(object):
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print("{0}, {1}".format(self.name, message))

class Publisher(object):
    def __init__(self):
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self, who):
        self.subscribers.discard(who)
    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

pub = Publisher()

beom = Subscriber('Beom')
ben = Subscriber('Ben')
seok = Subscriber('Seok')

pub.register(beom)
pub.register(ben)
pub.register(seok)

pub.dispatch("점심시간입니다.")
pub.unregister(ben)
pub.dispatch("저녁시간입니다.")
