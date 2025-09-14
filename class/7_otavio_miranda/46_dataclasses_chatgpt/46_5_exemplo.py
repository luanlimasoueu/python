from dataclasses import dataclass, field

@dataclass
class Team:
    name: str
    members: list = field(default_factory=list)

t = Team("Pythonistas")
t.members.append("Luiz")
print(t.members)  # ['Luan']
