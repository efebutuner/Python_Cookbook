#*args and *kwargs

def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5,6,7,8,9,10, num1 = 10, num2 = 5))

#Rule: params, *args, default parameters, **kwargs ==> Order of defining function parameters

def highest_even(li):
    h = 0
    for i in li:
        if i % 2 == 0 and i > h:
            h = i
    return print(f'Highest Even Number in your list is {h}')


highest_even([10,2,3,2,4,8,11])

#Alternative Method 

def highest(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(highest([10,2,3,2,4,8,11]))
