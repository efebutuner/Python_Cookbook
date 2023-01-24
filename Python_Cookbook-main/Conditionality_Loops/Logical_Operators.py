# and / or / < / > / == are examples of logical operators

print(4>5) # False
print(5>4) # True

print("hello" == "hello") # True
print("a" > "A") # True because of the ACII table indexes

print(1 >= 0) # True
print(0 != 0) # False

print(not(True)) # False
print(not(False)) # True

#Excersize

is_magician = False
is_expert = True

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("At least you are getting there")
elif not is_magician:
    print("You need magic powers")