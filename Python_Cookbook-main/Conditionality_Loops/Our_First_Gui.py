picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
]

# for i in picture:
#     for j in i:
#         if j == 0:
#             print('', end = '*')
#         elif j == 1:
#             print("*")

for image in picture:
    for pixel in image:
        if (pixel == 1):
            print("*", end = '')
        else:
            print(" ", end = '')
    print('')