from dataclasses import dataclass
from typing import Any
@dataclass
class condition:
    fact: str
    value: str

@dataclass
class rule:
    name: str
    conditions: list[condition]
    conclusion: condition

@dataclass(frozen=True)
class fact:
    name: str 
    value: Any = True

    def __str__(self)-> str:
        return f"{self.name}={self.value}" if self.value is not True else self.name
    
@dataclass
class derivation:
    fact: fact
    rule: rule | None
    children: list
