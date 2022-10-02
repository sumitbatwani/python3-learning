def mean(values):
    if type(values) == dict:
        mean_value = sum(values.values()) / len(values)
    else:
        mean_value = sum(values) / len(values)
    return mean_value

list_data = [1,2,3,4]
dictionary_data = {'sumit': 1, 'john': 2}
print(mean(list_data))
print(mean(dictionary_data))

# Case II

def check_temperature(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

print(check_temperature(10))