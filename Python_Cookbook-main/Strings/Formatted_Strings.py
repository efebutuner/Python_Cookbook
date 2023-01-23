#Formatted Strings

name = 'Efe'
age = 22
print('Hi ' + name + '. You are ' + str(age) + ' years old.')
print(f"Hi {name}. You are {age} years old.")

#f character inside print function allows us to create formatted strings using curly brackets.

print("Hi {1}. You are {0} years old".format(name, age))