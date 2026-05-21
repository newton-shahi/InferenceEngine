RULE drought_persistence: IF rainfall IS none AND temperature IS high THEN drought_duration IS high

RULE pest_warning: IF humidity IS high AND temperature IS medium THEN pest_risk IS high

RULE frost_warning: IF temperature IS low AND humidity IS high THEN frost_risk IS high

RULE heatwave_alert: IF temperature IS high AND humidity IS low THEN heatstroke_risk IS high

RULE wind_damage: IF wind_speed IS high AND crop_stage IS low THEN crop_damage_risk IS high

RULE crop_stress_heat_drought: IF rainfall IS none AND temperature IS high THEN crop_stress IS high

RULE growth_slowdown: IF wind_speed IS high AND crop_stage IS medium THEN growth_rate IS low

RULE drought_emergency: IF drought_duration IS high AND crop_stress IS high THEN water_emergency IS true

RULE yield_reduction_risk: IF crop_stress IS high AND growth_rate IS low THEN yield_risk IS high

RULE cold_stress: IF frost_risk IS high AND growth_rate IS low THEN cold_damage_risk IS high

RULE heat_failure_risk: IF heatstroke_risk IS high AND crop_stress IS high THEN crop_failure_risk IS high