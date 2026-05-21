from string import Template

AGRICULTURE_EXTRACT_PROMPT =  Template("""
You are an information extraction system.

Your task is to read a natural language input describing farming or environmental conditions and convert it into a strict JSON object.

You must NOT add explanations, only return valid JSON.

OUTPUT FORMAT (STRICT):
Return exactly this structure:

{
  "rainfall": "",
  "temperature": "",
  "wind_speed": "",
  "crop_stage": "",
  "humidity": ""
}

FIELD DEFINITIONS:

1. rainfall:
- "none" → no rain, no rainfall, dry conditions
- "low" → light rain, occasional rain
- "high" → heavy rain, continuous rain, flooding rain

2. temperature:
- "low" → cold, freezing, chilly
- "medium" → normal, moderate, mild
- "high" → hot, very hot, extreme heat

3. wind_speed:
- "low" → calm, still air, gentle breeze
- "high" → strong wind, fast wind, stormy wind

4. crop_stage:
- "low" → just planted, seedling, just starting to grow
- "medium" → growing, vegetative, partially grown
- "high" → flowering, mature, harvest-ready

5. humidity:
- "low" → dry air, very low moisture
- "high" → humid, moist, sticky air, high moisture

RULES:
- Output ONLY valid JSON
- No explanations, no extra text
- Always include all 5 fields
- If field is absent then replace by _
- If ambiguous, choose the closest match
- Normalize synonyms:
  "no rain" → "none"
  "very hot" → "high"

EXAMPLE:

Input:
I am a farmer. My farm gets no rain. It is very hot and wind blows very fast. Crops are just starting to grow and humidity is very low.

Output:
{
  "rainfall": "none",
  "temperature": "high",
  "wind_speed": "high",
  "crop_stage": "low",
  "humidity": "low"
}

The natural language input is:                       
$nl_query                                           
                                       """)