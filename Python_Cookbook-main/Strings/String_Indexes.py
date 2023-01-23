#Strings are ordered sequence of characters
selfish = "me me me"
        #  01234567

print(selfish[0])
#We can adress the indexes inside a string using square brackets

#[start:stop]
print(selfish[0:2])

#[start:stop:stepover]
print(selfish[0:8:2])

#[start:]
print(selfish[2:])

#[:end]
print(selfish[:5])

#[::-1]
print(selfish[::-1]) # Reverses the order of string