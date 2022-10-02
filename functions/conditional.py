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