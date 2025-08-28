from abc import ABC, abstractmethod


# ===== Subject =====
class FileServer(ABC):
    @abstractmethod
    def read_file(self, filename: str) -> None: ...


# ===== RealSubject =====
class RealFileServer(FileServer):
    def read_file(self, filename: str) -> None:
        print(f"📂 Lendo conteúdo do arquivo: {filename}")


# ===== Proxy =====
class FileServerProxy(FileServer):
    def __init__(self, user_role: str):
        self._user_role = user_role
        self._real_server = RealFileServer()

    def read_file(self, filename: str) -> None:
        if self._has_permission(filename):
            print("✅ Permissão concedida")
            self._real_server.read_file(filename)
        else:
            print("⛔ Acesso negado ao arquivo:", filename)

    def _has_permission(self, filename: str) -> bool:
        # Regras de permissão simples
        if self._user_role == "admin":
            return True
        if self._user_role == "guest" and filename.endswith(".txt"):
            return True
        return False


# ===== Client =====
def main():
    print("\n--- Cliente admin ---")
    admin_proxy = FileServerProxy("admin")
    admin_proxy.read_file("dados_confidenciais.pdf")

    print("\n--- Cliente guest ---")
    guest_proxy = FileServerProxy("guest")
    guest_proxy.read_file("notas.txt")
    guest_proxy.read_file("dados_confidenciais.pdf")


if __name__ == "__main__":
    main()
