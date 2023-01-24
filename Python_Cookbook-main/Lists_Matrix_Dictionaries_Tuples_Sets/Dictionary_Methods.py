#Dictionary Methods

user = {
    'basket' : [1,2,3],
    'greet' : 'hello',
    'age': 20
}

print(user.get('age')) # ==> .get() functions try to return the key's value but would not give error and stop the program. In case, it returns None.
print(user.get('age', 55)) # try to get age' keys value, if not exists use 55 instead.

user2 = dict(name = 'JarJar')

print('basket' in user)
print('size' in user)
print('hello' in user.keys())
print('hello' in user.values())

print(user.items())
print(user.clear())
print(user)

user3 = user.copy()
print(user3)

print(user.popitem()) #last item in the dictionary gets removed but may be random so be careful (as dictionary is not sorted)
print(user.update({'age':55})) #also can be used to add new keys to the dictionary.
print(user)