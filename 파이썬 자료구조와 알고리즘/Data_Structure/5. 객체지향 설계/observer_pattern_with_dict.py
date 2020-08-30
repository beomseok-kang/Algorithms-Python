class SubscriberOne(object):
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print("{0} {1}".format(self.name, message))

class SubscriberTwo(object):
    def __init__(self, name):
        self.name = name
    def receive(self, message):
        print("{0} {1}".format(self.name, message))

class Publisher(object):
    def __init__(self):
        self.subscribers = dict()
    def register(self, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.subscribers[who] = callback
    def unregister(self, who):
        del self.subscribers[who]
    def dispatch(self, message):
        for subscriber, callback in self.subscribers.items():
            callback(message)

pub = Publisher()
beom = SubscriberOne('Beom')
seok = SubscriberTwo('Seok')
ben = SubscriberOne('Ben')

pub.register(beom, beom.update)
pub.register(seok, seok.receive)
pub.register(ben)

pub.dispatch('점심시간입니다')
pub.unregister(ben)
pub.dispatch('퇴근시간입니다')