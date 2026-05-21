from rule_engine.engine.memory import ExplainableWM
from rule_engine.dsl.parse import load_rules
from rule_engine.engine.inference_engine import forward_chain
from agent.extractor import extract_facts
from rule_engine.utils.user_input import input_processing

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

user_input = input_processing()
extracted_data = extract_facts("a",user_input)
for seed_fact,seed_value in extracted_data.items():
    print(f"{seed_fact} = {seed_value} ")