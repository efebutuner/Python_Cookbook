is_old = bool('hello')
is_licenced = bool(5)

print(is_old) #True
print(is_licenced) #True

if is_old and is_licenced:
    print("Truthy")
else:
    print("Falsy") #Falsy values are fractions, empty strings, integer 0... 
