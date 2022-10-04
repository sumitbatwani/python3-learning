def temperature_check_1(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

def temperature_check_2(temp):
    if temp > 25:
        return "Hot"
    elif temp >= 15 and temp <= 25:
        return "Warm"
    elif temp < 15:
        return "Cold"