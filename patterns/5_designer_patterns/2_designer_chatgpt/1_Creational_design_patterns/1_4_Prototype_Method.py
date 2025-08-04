from abc import ABC, abstractmethod
import copy

class Documento(ABC):
    def __init__(self, titulo):
        self.titulo = titulo

    @abstractmethod
    def clone(self):
        pass

    def exibir(self):
        print(f"Documento: {self.titulo}")


class DocumentoTexto(Documento):
    def __init__(self, titulo, conteudo):
        super().__init__(titulo)
        self.conteudo = conteudo

    def clone(self):
        return copy.deepcopy(self)

    def exibir(self):
        print(f"[Texto] {self.titulo}:\n{self.conteudo}")

class DocumentoPDF(Documento):
    def __init__(self, titulo, paginas):
        super().__init__(titulo)
        self.paginas = paginas

    def clone(self):
        return copy.deepcopy(self)

    def exibir(self):
        print(f"[PDF] {self.titulo} - {self.paginas} páginas")

def main():
    doc1 = DocumentoTexto("Relatório", "Este é o conteúdo original.")
    doc2 = doc1.clone()
    doc2.titulo = "Relatório Clonado"
    doc2.conteudo = "Este é o conteúdo clonado e modificado."

    doc1.exibir()
    print()
    doc2.exibir()

if __name__ == "__main__":
    main()
