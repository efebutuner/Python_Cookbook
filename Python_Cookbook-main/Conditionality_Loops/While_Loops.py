#While: keeps looping until the condition beside it turns false

i = 0 
while i < 50:
    print(i)
    break

#break, breaks while loop 

i = 0
while i < 50:
    print(i)
    i += 1
    break
else:
    print("Done")

#else statement can be used after a while that has the break function

#While loops are beneficial to use when we dont know how many times we want to loop through something and usually we do not use while with basic iterables

while True:
    response = input("Say something: ")
    if(response == "bye"):
        break