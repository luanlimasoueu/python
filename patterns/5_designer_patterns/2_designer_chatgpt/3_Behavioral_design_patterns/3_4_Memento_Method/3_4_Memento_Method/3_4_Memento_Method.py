# ===== Memento =====
class TextMemento:
    def __init__(self, state: str):
        self._state = state  # estado imutável

    def get_state(self) -> str:
        return self._state


# ===== Originator =====
class TextEditor:
    def __init__(self):
        self._text = ""

    def write(self, text: str):
        self._text += text

    def show(self):
        print(f"📄 Texto atual: {self._text}")

    def save(self) -> TextMemento:
        return TextMemento(self._text)

    def restore(self, memento: TextMemento):
        self._text = memento.get_state()


# ===== Caretaker =====
class History:
    def __init__(self):
        self._mementos = []

    def backup(self, memento: TextMemento):
        self._mementos.append(memento)

    def undo(self) -> TextMemento:
        if not self._mementos:
            return None
        return self._mementos.pop()


# ===== Client =====
def main():
    editor = TextEditor()
    history = History()

    editor.write("Olá")
    history.backup(editor.save())  # salva

    editor.write(" mundo!")
    history.backup(editor.save())  # salva

    editor.show()  # 📄 Texto atual: Olá mundo!

    # Desfaz última mudança
    editor.restore(history.undo())
    editor.show()  # 📄 Texto atual: Olá

    # Desfaz novamente
    editor.restore(history.undo())
    editor.show()  # 📄 Texto atual: 

if __name__ == "__main__":
    main()
