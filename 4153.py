check = 1
while check != 0:
    x,y,z = input().split()
    x = int(x)
    y = int(y)
    z = int(z)
    if (x == 0 and y == 0 and z == 0):
        check = 0
    elif (x ** 2 + y ** 2 == z ** 2 or y ** 2 + z ** 2 == x ** 2 or x ** 2 + z ** 2 == y ** 2):
        print("right")
    else:
        print("wrong")

