#Docstrings

def test(a):
    '''
    Info: This function prints the statement inside.
    '''
    print(a)

test(10)
test("Helllooooooo")
test("Test function prints the statement inside")

help(test)
print(test.__doc__)