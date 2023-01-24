#List Slicing

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

amazon_cart[0] = 'laptop'
print(amazon_cart)

#Lists are mutable (we can make changes and assignments after we set lists)

print(amazon_cart[1:3])

#While slicing lists, we create new lists or in other words a copy of list.

new_cart = amazon_cart[:] #If we wouldnt have written [:] we have directly assign the new list to the existing one which will end up by synching any modifications on our new list with the old one.
new_cart[0] = 'gum'

print(amazon_cart)
print(new_cart)