from rule_engine.engine.memory import ExplainableWM
from rule_engine.dsl.parse import load_rules
from rule_engine.engine.inference_engine import forward_chain

rules = load_rules("rule/agro_rules.dsl")
print(rules)
wm = ExplainableWM()
wm.assert_seed("crop_stage", "low")
wm.assert_seed("rainfall", "none")
wm.assert_seed("temperature", "high")
wm.assert_seed("humidity", "low")
wm.assert_seed("wind_speed", "high")

forward_chain(rules, wm)
print([str(f) for f in wm.all_facts()])
print(wm.explain("water_emergency"))


