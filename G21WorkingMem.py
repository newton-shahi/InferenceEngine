from dataclasses import dataclass
from typing import Any

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
wm1 = WorkingMemory()
wm1.assert_fact("temp","low")
wm1.assert_fact("cold")
wm1.assert_fact("disease",False)
print(wm1.holds("cold")) #true
print(wm1.holds("hot")) #false
print(wm1.get_value("temp")) #low
print(wm1.allFacts()) #all will be printed
wm1.retract_fact("cold")
print(wm1.holds("cold")) #false
snapped = wm1.snapshot()
print(snapped)
wm1.retract_fact("temp")
print(wm1.allFacts()) #all will be printed except temp
print(snapped) #temp still there



