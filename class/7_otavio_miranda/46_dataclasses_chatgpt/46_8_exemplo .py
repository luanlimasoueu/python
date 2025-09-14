from dataclasses import dataclass, field

@dataclass(frozen=True)
class Config:
    host: str
    port: int

c = Config("localhost", 8080)
# c.port = 9090  # ❌ Erro! Classe imutável
