from string import Template 
MAX_ITER = 100

FORWARD_CHAIN_FIRE = "[iter {iteration} FIRED {name} -> {fact}={value}]"
GEMINI_MODEL = "gemini-flash-latest"
API_KEY_ERROR = "Error: The api-key cannot be found. Please recheck if the input gemini key in config/settings.py is correct."
JSON_LOAD_ERROR = "Error: The response from gemini isn't correct json format."


HEAD_TEMPLATE = "\n*****************\n*****************\n==== INFERENCE ENGINE ===="
INPUT_MSG = "\n Write things you are worried about. Current support (farm support) \n => "
INPUT_MSG_ERROR = Template("""
                           You need to enter the value for $seed_fact . 
                           It was missing or out of options. Options are [$options] 
                           """)


RESULT_DETAILS_INFERENCE = "\n=== 🧾🧾🧾 DETAILED RESULT with Why explained === \n"
RESULT_INFERENCE = "\n=== 🧾RESULT === \n"
FACT_TEMPLATE = "\n📬 FACT!\n"
WHY_TEMPLATE ="\nWhy above fact is derived. Because :\n"
DETAILS_ABOVE = "\nLOOK above for more details of why!\n"
RUN_INFERENCE ="\n EVALUATING.....\n"

ALLOWED_RAIN_VALUE = {"none", "low", "high"}
ALLOWED_TEMPERATURE_VALUE =  {"low", "medium", "high"}
ALLOWED_WIND_VALUE = {"low", "high"}
ALLOWED_CROP_VALUE = {"low", "medium", "high"}
ALLOWED_HUMIDITY_VALUE = {"low", "high"}
VALID = "isValid"
