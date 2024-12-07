""" # frequency of each char
string = input("Enter the string - ")
char_count = {}
for char in string:
    char_count[char] = char_count.get(char,0) + 1
    print(char_count)

"""
from enum import unique

""" # find missing keys
dict1 = {"a":1,"b":2,"c":3}
dict2 = {"a":1,"b":2}
missing_keys=set(dict1.keys())-set(dict2.keys())
print(missing_keys)

"""
""" # Find max or min number
def max_value_dict(dictionary):
    return max(dictionary.values())
    # return min(dictionary.values())
print(max_value_dict({"a":10,"b":20,"c":30}))
"""

""" # Removing duplicates
my_dict = {"a": 1, "b": 2, "c": 1, "d": 4}
unique_value = set()
result = {}
for key, value in my_dict.items():
    if value not in unique_value:
        result[key] = value
        unique_value.add(value)
        print(result)
"""