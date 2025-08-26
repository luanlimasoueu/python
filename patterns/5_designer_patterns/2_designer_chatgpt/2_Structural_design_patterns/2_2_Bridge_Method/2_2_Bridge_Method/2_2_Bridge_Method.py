from abc import ABC, abstractmethod


# ===== Implementor =====
class Device(ABC):
    @abstractmethod
    def enable(self) -> None: ...
    
    @abstractmethod
    def disable(self) -> None: ...
    
    @abstractmethod
    def set_volume(self, percent: int) -> None: ...


# ===== Concrete Implementors =====
class TV(Device):
    def enable(self):
        print("📺 TV ligada")
    def disable(self):
        print("📺 TV desligada")
    def set_volume(self, percent: int):
        print(f"📺 TV volume ajustado para {percent}%")


class Radio(Device):
    def enable(self):
        print("📻 Rádio ligado")
    def disable(self):
        print("📻 Rádio desligado")
    def set_volume(self, percent: int):
        print(f"📻 Rádio volume ajustado para {percent}%")


# ===== Abstraction =====
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        print("🔘 Alternando energia...")
        self.device.enable()

    def volume_up(self):
        print("🔘 Volume up")
        self.device.set_volume(70)


# ===== Refined Abstraction =====
class AdvancedRemote(RemoteControl):
    def mute(self):
        print("🔇 Mutando...")
        self.device.set_volume(0)


# ===== Client =====
def main():
    tv = TV()
    radio = Radio()

    # Controle simples
    remote_tv = RemoteControl(tv)
    remote_tv.toggle_power()
    remote_tv.volume_up()

    print("----")

    # Controle avançado
    remote_radio = AdvancedRemote(radio)
    remote_radio.toggle_power()
    remote_radio.mute()


if __name__ == "__main__":
    main()
