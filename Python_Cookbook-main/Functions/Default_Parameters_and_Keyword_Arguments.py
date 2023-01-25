#Positional Arguments

#Keyword Arguments

def say_hello(name, emoji):
    print(f'Helloo {name} {emoji}')

say_hello(name='BoBo', emoji = ':D')

#Default Parameters

def say_hello_lord(name='Darth Vader', emoji='[<('):
    print(f'Helloo {name} {emoji}')

say_hello_lord()