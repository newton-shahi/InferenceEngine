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

def load_rules(path: str) -> list[rule]:
    with open(path) as f:
        lines = [l.strip() for l in f if l.strip() and not l.startswith('#')]
    return [parse_rule(line) for line in lines if line.startswith("RULE")]

rules = load_rules("agro_rules.txt")
print(rules)

