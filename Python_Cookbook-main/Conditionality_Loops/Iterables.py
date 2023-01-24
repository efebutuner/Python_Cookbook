#Iterable: List, Dictionary, Tuple, Set, String to be iterated
#Iterate: one by one check each item in the collection

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user.items():  #items() return key value pairs as tuple
    print(item)

for item in user.values(): #values() return values assigned to the keys
    print(item)

for item in user.keys(): #keys() return keys that belong to the values
    print(item)

for key, value in user.items(): #Seperates the keys and values of items inside a dictionary
    print(key, value)