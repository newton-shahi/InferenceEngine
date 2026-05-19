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

parser = Lark(GRAMMAR, start ="rule")


tree = parser.parse(
    "RULE irrigation_needed: IF soil_moisture IS low AND temperature IS high THEN irrigate IS true"
)

print(tree.pretty())