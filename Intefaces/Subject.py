from Intefaces.Observer import Observer


class Subject:
    def __init__(self):
        self._observers = []
        pass

    def attach(self, observer: Observer):
        self._observers.append(observer)
        pass

    def detach(self, observer: Observer):
        self._observers.remove(observer)
        pass

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)
        pass
