numbers = [.1, .2, .3]

at_one = numbers.__getitem__(1) # same and can be used with bracket pattern
bracket_one = numbers[1]
print(at_one)
print(bracket_one)

# --- slicing list --- 

days = ['monday', 'tuesday', 'wednesday', 'thursday'] #[-4, -3, -2, -1]

# ['monday', 'tuesday'] last index is not inclusive
print(days[0:2]) 

# short-hand
print(days[:2])

# ['monday', 'tuesday', 'wednesday', 'thursday']
print(days[0:])
print(days[:4])

# negative index
print(days[-1]) # last element of list i.e. thursday
print(days[-3:-1]) #['tuesday', 'wednesday'] (last element is not inclusive)