# ===== Subsystems =====
class Light:
    def on(self): print("💡 Luzes acesas")
    def off(self): print("💡 Luzes apagadas")

class SoundSystem:
    def on(self): print("🔊 Som ligado")
    def set_volume(self, level: int): print(f"🔊 Volume ajustado para {level}")
    def off(self): print("🔊 Som desligado")

class Projector:
    def on(self): print("📽️ Projetor ligado")
    def wide_screen_mode(self): print("📽️ Modo tela cheia ativado")
    def off(self): print("📽️ Projetor desligado")


# ===== Facade =====
class HomeTheaterFacade:
    def __init__(self, light: Light, sound: SoundSystem, projector: Projector):
        self.light = light
        self.sound = sound
        self.projector = projector

    def watch_movie(self):
        print("\n🎬 Preparando para assistir ao filme...")
        self.light.off()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.sound.on()
        self.sound.set_volume(7)
        print("🍿 Pronto! Bom filme!\n")

    def end_movie(self):
        print("\n🛑 Encerrando sessão de cinema...")
        self.light.on()
        self.sound.off()
        self.projector.off()
        print("🎬 Sessão encerrada.\n")


# ===== Client =====
def main():
    # Subsistemas criados
    light = Light()
    sound = SoundSystem()
    projector = Projector()

    # Facade simplificando a interação
    home_theater = HomeTheaterFacade(light, sound, projector)

    # Cliente usa apenas o Facade
    home_theater.watch_movie()
    home_theater.end_movie()


if __name__ == "__main__":
    main()
