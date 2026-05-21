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
class Fact:
    name: str 
    value: Any = True

    def __str__(self)-> str:
        return f"{self.name}={self.value}" if self.value is not True else self.name
    
@dataclass
class derivation:
    fact: Fact
    rule: rule | None
    children: list

class WorkingMemory:
    #constructor,assert_fact(name,value),holds ? ,get_value,allfacts
    def __init__(self):
        self._facts : set[Fact] = set() 
    
    def assert_fact(self,name:str, value = True):
        self._facts.add(Fact(name,value))

    def holds(self,name:str):
        return any(f.name == name for f in self._facts)

    def get_value(self,name:str) -> Any | None:
        for f in self._facts:
            if f.name == name : 
                return f.value 
        return None
    def allFacts(self) -> list:
        return sorted(self._facts, key = lambda f: f.name)

    def retract_fact(self,name:str):
        val = self.get_value(name)
        self._facts.remove(Fact(name,val))

    def snapshot(self):
        return self._facts.copy()
    
class ExplainableWM(WorkingMemory):
    def __init__(self):
        super().__init__()
        self._why: dict[str,derivation] = {}
    def assert_seed(self,name:str,value = True):
        self.assert_fact(name,value)
        f = Fact(name,value)
        self._why[name] = derivation(f,None,[])

    def assert_derived(self,name :str,value,rule:rule):
        self.assert_fact(name,value)
        f = Fact(name,value)
        children = [self._why[c.fact] for c in rule.conditions if c.fact in self._why]
        self._why[name] = derivation(f,rule,children)

    def explain(self,fact_name:str,indent=0) -> str:
        d = self._why.get(fact_name)
        if not d: return f"{' '*indent}? {fact_name}(unknown)"
        prefix = ' '*indent
        if d.rule is None:
            return f"{prefix}-> {d.fact} (GIVEN)"
        lines = [f"{prefix}->{d.fact} [via rule: {d.rule.name}]"]
        for child in d.children:
            lines.append(self.explain(child.fact.name,indent+1))

        return "\n".join(lines)

