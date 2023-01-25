#Excersize: Check out the duplicates in a list

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

my_list = []
for item in some_list:
    if some_list.count(item) > 1 and my_list.count(item) == 0:
        my_list.append(item)

print(my_list)