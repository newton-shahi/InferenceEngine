import config.string_literals as literals

def input_processing():
    print(literals.HEAD_TEMPLATE)
    user_input = input(literals.INPUT_MSG).strip()
    return user_input

def take_input(seed_fact,accepted_val) -> str:
    new_val = "unknown"
    while new_val not in accepted_val:
        print(literals.INPUT_MSG_ERROR.substitute(
            seed_fact = seed_fact,
            options = accepted_val
        ))
        val = input("=>")
        new_val = val
    return new_val