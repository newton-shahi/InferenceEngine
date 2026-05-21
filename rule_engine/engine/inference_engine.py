from rule_engine.engine.memory import ExplainableWM,rule
import config.string_literals as literals
MAX_ITER = 100

def evaluate_rule(rule:rule,wm:ExplainableWM):
    for cond in rule.conditions:
        actual = wm.get_value(cond.fact)
        if(actual!=cond.value):
            return False
    return True

def forward_chain(rules: list[rule],wm:ExplainableWM, max_iter:int = MAX_ITER):
    for iteration in range(max_iter):
        fired_any_global = False
        while True:
            fired_any = False
            for rule in rules:
                if evaluate_rule(rule,wm):
                    c = rule.conclusion
                    if not wm.holds(c.fact):
                        wm.assert_derived(c.fact,c.value,rule)
                        fired_any = True
                        fired_any_global = True
                        print(literals.FORWARD_CHAIN_FIRE.format(iteration=iteration,name = rule.name,fact = c.fact,value = c.value))
                        # print(f"[iter {iteration} FIRED {rule.name} -> {c.fact}={c.value}]")
            if not fired_any:
                break
        if not fired_any_global:
            print(f"Fixed point at iter {iteration}")
            return  
    raise RuntimeError("Infinite loop detected")

