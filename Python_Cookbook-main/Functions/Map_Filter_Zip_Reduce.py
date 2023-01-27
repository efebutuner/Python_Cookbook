#map, filter, zip and reduce

#MAP allows us to simplify the code.

def multiply_by2(item):
    # new_list = []
    # for item in li:
    #     new_list.append(item*2)
    # return new_list
    return item*2

#Instead of writing that much code, we write 1 line of code.

print(list(map(multiply_by2, [1,2,3])))

#FILTER allows us to fiter our results

my_list = [1,2,3]

def only_odd(item):
    return item % 2  != 0

print(list(filter(only_odd, my_list)))


#ZIP allows us to zip 2 iterables together (each indexed items are assigned to a tuple)

your_list = [10,20,30]

print(list(zip(my_list, your_list)))   #[(1, 10), (2, 20), (3, 30)]

#REDUCE (imported from functools)

from functools import reduce

def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))
