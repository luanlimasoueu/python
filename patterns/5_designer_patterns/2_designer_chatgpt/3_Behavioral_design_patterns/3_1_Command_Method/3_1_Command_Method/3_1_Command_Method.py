from abc import ABC, abstractmethod


# ===== Command =====
class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    @abstractmethod
    def undo(self) -> None: ...


# ===== Receiver =====
class Light:
    def on(self): print("💡 Luz ligada")
    def off(self): print("💡 Luz desligada")


# ===== Concrete Commands =====
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


# ===== Invoker =====
class RemoteControl:
    def __init__(self):
        self.history = []  # Para suportar undo

    def submit(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            cmd = self.history.pop()
            cmd.undo()
        else:
            print("⛔ Nada para desfazer")


# ===== Client =====
def main():
    # Receiver
    light = Light()

    # Concrete Commands
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Invoker
    remote = RemoteControl()

    # Executando comandos
    remote.submit(light_on)   # Liga
    remote.submit(light_off)  # Desliga
    remote.undo_last()        # Desfaz último (Liga de novo)


if __name__ == "__main__":
    main()
