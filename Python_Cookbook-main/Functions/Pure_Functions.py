#A function should result same for all inputs ( must act same )

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))

#A pure function does not effect the outside world.