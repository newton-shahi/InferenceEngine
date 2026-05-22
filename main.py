from rule_engine.engine.memory import ExplainableWM
from rule_engine.dsl.parse import load_rules
from rule_engine.engine.inference_engine import forward_chain
from agent.extractor import extract_facts
from rule_engine.utils.user_input import input_processing
from rule_engine.utils.validator import validate
import config.string_literals as literals

rules = load_rules("rule/agro_rules.dsl")
wm = ExplainableWM()

def detailed_output():
    print(literals.RESULT_DETAILS_INFERENCE)
    for f in wm.all_facts():
        print(literals.FACT_TEMPLATE)
        print(str(f))
        print(literals.WHY_TEMPLATE)
        print(wm.explain(f.name))

def short_output():
    print(literals.RESULT_INFERENCE)
    print(literals.FACT_TEMPLATE)
    for f in wm.all_facts():
        print(str(f))
        #print("\n")



user_input = input_processing()
extracted_data = extract_facts("a",user_input)
for seed_fact,seed_value in extracted_data.items():
    val = validate(seed_fact,seed_value)
    if(val != literals.VALID) : seed_value = val
    wm.assert_seed(seed_fact,seed_value)

print(literals.RUN_INFERENCE)
forward_chain(rules, wm)
detailed_output()
print(literals.DETAILS_ABOVE)
short_output()

