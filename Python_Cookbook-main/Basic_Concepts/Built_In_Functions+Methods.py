print(len("Heloooooooooo")) #Prints the length of the string inside its brackets.

greet = 'Helloooooo'
print(greet[0:len(greet)])

#len() is an example of Python Built-in Functions
#Methods are starting with . after the variable

quote = "to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))  #returns the index of first occurance of the string that being seeked to find.
print(quote.replace('be', 'me')) #This way we only overrided the string which we did not change the original string(immutability)
