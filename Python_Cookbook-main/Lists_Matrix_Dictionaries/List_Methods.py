basket = [1,2,3,4,5]
print(len(basket))

#adding 
basket.append(100)
new_list = basket.extend([100, 101])
print(basket)
print(new_list)

#removing 
basket.pop()
print(basket)
basket.pop(5) #Takes an index
basket.remove(100) #Takes the item that will be removed from the list

new_list = basket.clear() #Clears the whole list
print(new_list)

mylist = ['a', 'b', 'y', 'c', 'd', 'e', 'd']
print(mylist.index('d')) #Returns the index of item given as a parameter that belongs to the list
print('d' in mylist)
print('x' in mylist)

print(mylist.count('d'))
#mylist.sort()  #Sorts the list alphabetically
print(mylist)
print(sorted(mylist)) #sorted function creates a copy of the list inside its paranthesis and rearranges it alphabetically

my_first_list = basket.copy()

basket.reverse()
print(basket)