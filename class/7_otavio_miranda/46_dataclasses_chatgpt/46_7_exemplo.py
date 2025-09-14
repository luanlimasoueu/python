from dataclasses import dataclass, field

@dataclass
class Secret:
    username: str
    password: str = field(repr=False)

s = Secret("admin", "1234")
print(s)  # Secret(username='admin')
