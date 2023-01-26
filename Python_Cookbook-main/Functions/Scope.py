#Scope ==> What variables do I have access to?

def some_func():
    total = 100

#print(total) ==> gives an error as total is not in global scope -
#We cannot access variables defined inside functions but we can access variables in global scope 


#Scope Rules

a = 1 

def confusion():
    a = 5
    return a

print(a)
print(confusion())

#Scope order in python functions
#1 - start with local scope (a inside the confusion function is an example)
#2 - Parent local scope (if there is a function outside the function (like a superset of function))
#3 - Global Scope
#4 - Built in python functions