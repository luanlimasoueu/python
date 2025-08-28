from abc import ABC, abstractmethod

# ----------------------------
# Observer Interface
# ----------------------------
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

# ----------------------------
# Concrete Observers
# ----------------------------
class NewsSubscriber(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, subject):
        print(f"{self.name} recebeu a notícia: {subject.state}")


# ----------------------------
# Subject Interface
# ----------------------------
class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for obs in self._observers:
            obs.update(self)


# ----------------------------
# Concrete Subject
# ----------------------------
class NewsPublisher(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()  # notifica todos os observers


# ----------------------------
# Exemplo de uso
# ----------------------------
if __name__ == "__main__":
    publisher = NewsPublisher()

    alice = NewsSubscriber("Alice")
    bob = NewsSubscriber("Bob")

    publisher.attach(alice)
    publisher.attach(bob)

    # Publicando notícias
    publisher.state = "Nova notícia: Lua cheia hoje!"
    publisher.state = "Nova notícia: Chuva de meteoros amanhã!"
