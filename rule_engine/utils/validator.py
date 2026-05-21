import config.string_literals as literals
from rule_engine.utils.user_input import take_input

def validate(seed_fact:str,seed_value:str) -> str:
    if seed_fact == "rainfall" and seed_value not in literals.ALLOWED_RAIN_VALUE:
        new_seed_value = take_input(seed_fact,literals.ALLOWED_RAIN_VALUE)
        return new_seed_value
    if seed_fact == "temperature" and seed_value not in literals.ALLOWED_TEMPERATURE_VALUE:
        new_seed_value = take_input(seed_fact,literals.ALLOWED_TEMPERATURE_VALUE)
        return new_seed_value
    if seed_fact == "wind_speed" and seed_value not in literals.ALLOWED_WIND_VALUE:
        new_seed_value = take_input(seed_fact,literals.ALLOWED_WIND_VALUE)
        return new_seed_value
    if seed_fact == "crop_stage" and seed_value not in literals.ALLOWED_CROP_VALUE:
        new_seed_value = take_input(seed_fact,literals.ALLOWED_CROP_VALUE)
        return new_seed_value
    if seed_fact == "humidity" and seed_value not in literals.ALLOWED_HUMIDITY_VALUE:
        new_seed_value = take_input(seed_fact,literals.ALLOWED_HUMIDITY_VALUE)
        return new_seed_value
    return literals.VALID
