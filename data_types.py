# integer
a = 1

# float
b = 2.2

# string
c = "cat"

# list
d = [1, 2, 3]

e = [1, "cat", 3.3]

f = e * 2

g = e + e

h = list(range(0, 11))

# dictionary
i = {"Marry": 1, "Sam": 2}

# tuples (immutable vs list which is mutable [1, 2, 3])
j = (1, 2, 3)

# example: dictionary and tuples
k = {'morning': (1.1, 2.2, 3.3), 'evening': (4.4, 5.5, 6.6)}

print(a, b, c, d, e, f, g, h, i, j, k)


# ----- cheatsheet -----
# Integers are used to represent whole numbers:
# rank = 10
# eggs = 12
# people = 3

# Floats represent decimal numbers:
# temperature = 10.2
# rainfall = 5.98
# elevation = 1031.88

# Strings represent text:
# message = "Welcome to our online shop!"
# name = "John"
# serial = "R001991981SW"

# Lists represent arrays of values that may change during the course of the program:
# members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
# pixel_values = [252, 251, 251, 253, 250, 248, 247]

# Dictionaries represent pairs of keys and values:
# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
# volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}

# Keys of a dictionary can be extracted with:
# phone_numbers.keys()

# Values of a dictionary can be extracted with:
# phone_numbers.values()

# Tuples represent arrays of values that are not to be changed during the course of the program:
# vowels = ('a', 'e', 'i', 'o', 'u')
# one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# You can get a list of attributes of a data type has using:
# dir(str)
# dir(list)
# dir(dict)

# You can get a list of Python builtin functions using:
# dir(__builtins__)

# You can get the documentation of a Python data type using:
# help(str)
# help(str.replace)
# help(dict.values)