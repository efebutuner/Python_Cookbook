for i, char in enumerate('Helloooo'): #Enumerate returns the index counter of the iterated objects
    print(i, char)

for  i, char in enumerate(list(range(100))):
    if char == 50:
        print(i, char)
    