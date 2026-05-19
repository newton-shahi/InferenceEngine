
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
def parse_rule(text: str)-> rule:
    text = text.strip()
    rule_name, remain_part = text.split(":",1)
    if_part,then_part = remain_part.split("THEN")
    cond_part = if_part.replace("IF","").strip()
    concl_part = then_part.strip()
    cond = []
    for f in cond_part.split("AND"):
        fact,_,value = f.partition("IS")
        fact = fact.strip()
        value = value.strip()

        cond.append(condition(fact,value))
    
    fact,_,value = concl_part.partition("IS")
    fact = fact.strip()
    value = value.strip()
    conclusion = condition(fact,value)
    name = rule_name.replace("RULE","").strip()
    return rule(name,cond,conclusion)

def evaluate_rule(rule:rule,wm:WorkingMemory):
    for cond in rule.conditions:
        actual = wm.get_value(cond.fact)
        if(actual!=cond.value):
            return False
    return True

def forward_chain(rules: list[rule],wm:WorkingMemory, max_iter:int = 100):
    for iteration in range(max_iter):
        fired_any = False
        for rule in rules:
            if evaluate_rule(rule,wm):
                c = rule.conclusion
                if not wm.holds(c.fact):
                    wm.assert_fact(c.fact,c.value)
                    fired_any = True
                    print(f"[iter {iteration} FIRED {rule.name} -> {c.fact}={c.value}]")
        if not fired_any:
            print(f"Fixed point at iter {iteration}")
            return 
    raise RuntimeError("Infinite loop detected")

rules = [
    parse_rule("RULE r1: IF soil_moisture IS low AND temperature IS high THEN irrigate IS true"),
    parse_rule("RULE r2: IF irrigate IS true AND water_supply IS available THEN pump_on IS true"),
]


wm = WorkingMemory()
wm.assert_fact("soil_moisture", "low")
wm.assert_fact("temperature",   "high")
wm.assert_fact("water_supply",  "available")
forward_chain(rules, wm)
print([str(f) for f in wm.allFacts()])
