from rule_engine.engine.memory import ExplainableWM
from rule_engine.dsl.parse import load_rules
from rule_engine.engine.inference_engine import forward_chain

rules = load_rules("agro_rules.txt")
print(rules)
wm = ExplainableWM()
wm.assert_seed("soil_moisture", "low")
wm.assert_seed("rainfall", "none")
wm.assert_seed("temperature", "very_high")
wm.assert_seed("humidity", "high")
wm.assert_seed("soil_nutrients", "poor")
forward_chain(rules, wm)
print([str(f) for f in wm.allFacts()])
print(wm.explain("yield_risk"))


