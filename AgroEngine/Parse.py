from Memory import rule,condition
from lark import Lark,Transformer       

GRAMMAR = """
    rule:   "RULE" NAME ":" "IF" conditions "THEN" conclusion
    conditions: condition ("AND" condition)*
    condition:  NAME "IS" VALUE
    conclusion:  NAME "IS" VALUE
    VALUE:      /[a-zA-Z_][a-zA-Z0-9_]*/
    NAME:       /[a-zA-Z_][a-zA-Z0-9_]*/
    %ignore /\\s+/

"""
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


parser = Lark(GRAMMAR, start ="rule")

transformer = RuleTransformer()





# def parse_rule(text: str)-> rule:
#     text = text.strip()
#     rule_name, remain_part = text.split(":",1)
#     if_part,then_part = remain_part.split("THEN")
#     cond_part = if_part.replace("IF","").strip()
#     concl_part = then_part.strip()
#     cond = []
#     for f in cond_part.split("AND"):
#         fact,_,value = f.partition("IS")
#         fact = fact.strip()
#         value = value.strip()

#         cond.append(condition(fact,value))
    
#     fact,_,value = concl_part.partition("IS")
#     fact = fact.strip()
#     value = value.strip()
#     conclusion = condition(fact,value)
#     name = rule_name.replace("RULE","").strip()
#     return rule(name,cond,conclusion)


def load_rules(path: str) -> list[rule]:
    with open(path) as f:
        lines = [l.strip() for l in f if l.strip() and not l.startswith('#')]
    return [transformer.transform(parser.parse((line))) for line in lines if line.startswith("RULE")]

