#Range

print(range(100))

for i in range(0, 10):
    print(i)
    print('email email list')

for _ in range(0, 100): #_ underscore means i dont care what variable name comes here, we just want to use range
    print(_)

for i in range(0, 100, 10): # third parameter in range is the stepover
    print(i)

for _ in range(2):
    print(list(range(10)))