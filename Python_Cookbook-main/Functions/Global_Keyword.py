#Global Keyword

total = 0 

def count():
    global total
    total  += 1
    return total

count()
count()
print(count())


#Dependency Injection

tot = 0

def count1(tot):
    tot += 1
    return tot

print(count1(count1(count1(tot))))