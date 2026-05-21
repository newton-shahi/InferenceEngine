import config.string_literals as literals

def input_processing():
    print(literals.HEAD_TEMPLATE)
    user_input = input(literals.INPUT_MSG).strip
    return user_input