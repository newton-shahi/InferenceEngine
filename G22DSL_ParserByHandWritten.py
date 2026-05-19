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

rule1 = parse_rule("RULE irrigation_rule : IF soil_moisture IS low AND temperature IS high THEN irrigate IS true ")
print(rule1)