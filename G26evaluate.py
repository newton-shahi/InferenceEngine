
from lark import Lark,Transformer       
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

GRAMMAR = """
    rule:   "RULE" NAME ":" "IF" conditions "THEN" conclusion
    conditions: condition ("AND" condition)*
    condition:  NAME "IS" VALUE
    conclusion:  NAME "IS" VALUE
    VALUE:      /[a-zA-Z_][a-zA-Z0-9_]*/
    NAME:       /[a-zA-Z_][a-zA-Z0-9_]*/
    %ignore /\\s+/

"""

parser = Lark(GRAMMAR, start ="rule")

class RuleTransformer(Transformer):
    def rule(self,items):
        name, conditions, conclusion = items
        return rule(str(name),conditions,conclusion)
    def conditions(self,items):
        return items
    def condition(self,items):
        return condition(str(items[0]),str(items[1]))
    def conclusion(self,items):
        return condition(str(items[0]),str(items[1]))

def evaluate_rule(rule:rule,wm:WorkingMemory):
    for cond in rule.conditions:
        actual = wm.get_value(cond.fact)
        if(actual!=cond.value):
            return False
    return True

tree = parser.parse(
    "RULE r1: IF soil_moisture IS low AND temperature IS high THEN irrigate IS true"
)

transformer = RuleTransformer()
rule = transformer.transform(tree)
print(rule)

wm= WorkingMemory()
wm.assert_fact("soil_moisture", "low")
wm.assert_fact("temperature", "high")
print(evaluate_rule(rule,wm)) #true