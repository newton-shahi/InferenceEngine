from config.settings import GEMINI_API_KEY
import google.genai as genai 
import os
import config.string_literals as literals
import resources.prompts as prompts
import json

def configure_gemini():
    try:
        api_key = os.environ.get("GEMINI_API_KEY") or GEMINI_API_KEY
    except:
        print(literals.API_KEY_ERROR)
        return
    client = genai.Client(api_key=api_key)
    return client


def sanitize_gemini_json(text:str) ->str:
    sanitize_rule = [
        str.strip,
        lambda t: t.removeprefix("```json"),
        lambda t: t.removeprefix("```Json"),
        lambda t: t.removeprefix("```"),
        lambda t: t.removesuffix("```"),
        str.strip
    ]
    for rule in sanitize_rule:
        text = rule(text)
    return text

def domain_classifier(domain:str)->str:
    #pass to llm and check which domain it is 
    return "agriculture"

def extract_facts(domain:str,user_input:str) -> dict:
    client = configure_gemini()
    domain_to_check = domain_classifier(domain)
    if(domain_to_check == "agriculture"):
        prompt = prompts.AGRICULTURE_EXTRACT_PROMPT.substitute(nl_query=user_input)
    response = client.models.generate_content(
        model = literals.GEMINI_MODEL,
        contents=prompt
    )
    text = response.text
    print(text)
    data = sanitize_gemini_json(text)
    try:
        data = json.loads(data)
    except:
        print(literals.JSON_LOAD_ERROR)
    return data

    