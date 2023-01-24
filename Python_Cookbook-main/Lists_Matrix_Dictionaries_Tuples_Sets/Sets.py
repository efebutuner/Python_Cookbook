#Sets
#Unordered collections of unique objects

my_set = {1, 2, 3, 4, 5}
print(my_set) #output = {1, 2, 3, 4, 5} / as can be seen, only unique elements are printed
my_set.add(100)
my_set.add(2)
print(my_set)

print(len(my_set))
print(list(my_set))

new_set = my_set.copy()
my_set.clear()
print(new_set)

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set))
print(my_set.discard(5))
print(my_set.difference_update(your_set))
print(my_set.intersection(your_set)) # print(my_set & your_set)
print(my_set.isdisjoint(your_set))
print(my_set.union(your_set)) # print(my_set | your_set)
print(my_set.issubset(your_set)) 
print(my_set.issuperset(your_set))