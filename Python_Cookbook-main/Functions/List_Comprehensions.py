#List, Set, Dictionary

#Comprehension ==>> Quick Way to generate lists sets or dicts

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

my_list1 = [char for char in 'Hello']  # Using list comprehension we did it with ease
print(my_list1)

my_list2 = [num*2 for num in range(0,100)]
my_list3 = [num**2 for num in range(0,100)] 
my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]
print(my_list4)