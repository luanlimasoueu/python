from abc import ABC, abstractmethod

# ----------------------------
# State Interface
# ----------------------------
class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass


# ----------------------------
# Concrete States
# ----------------------------
class PlayingState(State):
    def handle(self, context):
        print("🎵 Música está tocando...")
        context.set_state(PausedState())  # muda dinamicamente para Pausado


class PausedState(State):
    def handle(self, context):
        print("⏸ Música está pausada.")
        context.set_state(StoppedState())  # muda para Parado


class StoppedState(State):
    def handle(self, context):
        print("⏹ Música parada.")
        context.set_state(PlayingState())  # volta para Tocando


# ----------------------------
# Context
# ----------------------------
class MusicPlayer:
    def __init__(self):
        self._state = StoppedState()  # começa parado

    def set_state(self, state):
        self._state = state

    def press_button(self):
        self._state.handle(self)


# ----------------------------
# Exemplo de uso
# ----------------------------
if __name__ == "__main__":
    player = MusicPlayer()

    # usuário pressiona várias vezes o botão
    player.press_button()  # Música parada -> começa a tocar
    player.press_button()  # Tocando -> pausa
    player.press_button()  # Pausado -> para
    player.press_button()  # Parado -> toca novamente
