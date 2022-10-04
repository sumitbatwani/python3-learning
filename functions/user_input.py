def temp_check(temp):
    if temp > 25:
        return "Warm"
    else:
        return "Cold"

user_temperature = float(input("Enter temperature: "))

output = temp_check(user_temperature)

print(output)