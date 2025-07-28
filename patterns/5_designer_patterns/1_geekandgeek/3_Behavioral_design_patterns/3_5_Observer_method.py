class Originator:
    def __init__(self, text):
        self.text = text

    def set_text(self, text):
        self.text = text

    def create_memento(self):
        return Memento(self.text)

    def restore_memento(self, memento):
        self.text = memento.get_state()
        
    def __str__(self):
        return self.text


class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self):
        self._mementos = []
        self._current_index = -1

    def save(self, memento):
        # Remove future states if any
        if self._current_index + 1 < len(self._mementos):
            self._mementos = self._mementos[:self._current_index + 1]

        self._mementos.append(memento)
        self._current_index += 1

    def undo(self):
        if self._current_index > 0:
            self._current_index -= 1
            return self._mementos[self._current_index]
        return None

    def redo(self):
        if self._current_index + 1 < len(self._mementos):
            self._current_index += 1
            return self._mementos[self._current_index]
        return None


# Example usage
if __name__ == "__main__":
    # Create an Originator (Text Editor)
    editor = Originator("Initial Text")

    # Create a Caretaker
    caretaker = Caretaker()

    # Save the initial state
    caretaker.save(editor.create_memento())

    # Make changes and save the state
    editor.set_text("First Edit")
    caretaker.save(editor.create_memento())

    editor.set_text("Second Edit")
    caretaker.save(editor.create_memento())

    # Perform undo operations
    print("Current State:", editor)  # Output: "Second Edit"
    memento = caretaker.undo()
    if memento:
        editor.restore_memento(memento)
    print("After Undo:", editor)  # Output: "First Edit"

    # Perform redo operations
    memento = caretaker.redo()
    if memento:
        editor.restore_memento(memento)
    print("After Redo:", editor)  # Output: "Second Edit"