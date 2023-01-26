#Nonlocal Keyword

def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()

#Why do we need scopes?
#Garbage collector in python understands when we are done with a function so that it goes and clears the memory that holds the variables inside the functions scope
#So we can say that scopes are used to increase the efficiency of our programs