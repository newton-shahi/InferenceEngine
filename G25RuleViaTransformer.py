from lark import Lark,Transformer       
from dataclasses import dataclass
@dataclass
class condition:
    fact: str
    value: str

@dataclass
class rule:
    name: str
    conditions: list[condition]
    conclusion: condition


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

tree = parser.parse(
    "RULE irrigation_needed: IF soil_moisture IS low AND temperature IS high THEN irrigate IS true"
)

transformer = RuleTransformer()
rule = transformer.transform(tree)
print(rule)