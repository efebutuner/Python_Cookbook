for item in 'zero to mastery': #"zero to mastery" is an iterable here.
    print(item)

#iteration in list
for item in [1,2,3,4,5]:
    print(item)

#iteration in set
for item in {1,2,3,4,5}:
    print(item)

#iteration in tuple
for item in (1,2,3,4,5):
    print(item)

for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(item, x)