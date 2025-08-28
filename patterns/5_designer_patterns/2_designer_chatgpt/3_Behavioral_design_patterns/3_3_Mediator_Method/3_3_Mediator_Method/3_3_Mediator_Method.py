from abc import ABC, abstractmethod
from typing import Dict


# ===== Mediator =====
class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, msg: str, user_name: str): ...


# ===== ConcreteMediator =====
class ChatRoom(ChatMediator):
    def __init__(self):
        self._users: Dict[str, "User"] = {}

    def register_user(self, user: "User"):
        self._users[user.name] = user
        print(f"👤 {user.name} entrou na sala de chat")

    def send_message(self, msg: str, user_name: str):
        for name, user in self._users.items():
            if name != user_name:  # não envia para si mesmo
                user.receive(msg, user_name)


# ===== Colleague =====
class User:
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self.mediator = mediator
        mediator.register_user(self)

    def send(self, msg: str):
        print(f"✉️ {self.name} envia: {msg}")
        self.mediator.send_message(msg, self.name)

    def receive(self, msg: str, from_user: str):
        print(f"📥 {self.name} recebeu de {from_user}: {msg}")


# ===== Client =====
def main():
    chatroom = ChatRoom()

    # Criando usuários
    ana = User("Ana", chatroom)
    bruno = User("Bruno", chatroom)
    carla = User("Carla", chatroom)

    # Mensagens
    ana.send("Oi pessoal!")
    bruno.send("Olá Ana, tudo bem?")
    carla.send("Boa tarde a todos!")


if __name__ == "__main__":
    main()
