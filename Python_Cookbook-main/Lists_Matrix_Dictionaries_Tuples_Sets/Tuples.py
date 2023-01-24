#Tuple

my_tuple = (1,2,3,4,5)
#tuples are immutable so we cannot modify them
print(5 in my_tuple)
#tuples are faster than lists to be iterated

user = {
    (1,2) : [1,2,3],
    'greet' : 'hello',
    'age' : 20
}

print(user.items()) # Returns the items inside a dictionary as tuple's.

print(user[(1,2)]) #As tuples are immutable, they can be dictionary keys.

new_tuple = my_tuple[1:4]
x = my_tuple[0]

y,z,g, *other = (1,2,3,4,5)

#Tuples have only 2 methods which are .count() and .index()

my_tuple = (1,2,3,4,5)
print(my_tuple.count())
print(my_tuple.index(5))
print(len(my_tuple))