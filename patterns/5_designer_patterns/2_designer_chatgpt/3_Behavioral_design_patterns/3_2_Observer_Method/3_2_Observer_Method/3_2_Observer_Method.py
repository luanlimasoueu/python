from abc import ABC, abstractmethod
from typing import List


# ===== Observer =====
class Observer(ABC):
    @abstractmethod
    def update(self, headline: str) -> None: ...


# ===== Subject =====
class NewsAgency:
    def __init__(self):
        self._observers: List[Observer] = []
        self._latest_news = ""

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._latest_news)

    def add_news(self, headline: str):
        print(f"\n📰 Nova manchete: {headline}")
        self._latest_news = headline
        self.notify()


# ===== Concrete Observers =====
class MobileApp(Observer):
    def update(self, headline: str):
        print(f"📱 Notificação no app: {headline}")


class EmailSubscriber(Observer):
    def update(self, headline: str):
        print(f"📧 E-mail enviado: {headline}")


# ===== Client =====
def main():
    # Subject
    agency = NewsAgency()

    # Observers
    mobile = MobileApp()
    email = EmailSubscriber()

    # Registro
    agency.attach(mobile)
    agency.attach(email)

    # Publicando notícias
    agency.add_news("Mercado financeiro em alta")
    agency.add_news("Novo smartphone lançado")

    # Remover observador
    agency.detach(email)
    agency.add_news("Placar final da Copa: 3x1")


if __name__ == "__main__":
    main()
