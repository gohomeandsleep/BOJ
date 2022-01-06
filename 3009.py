x = []
y = []

for i in range(3):
    value_x,value_y = input().split()
    value_x = int(value_x)
    value_y = int(value_y)
    x.append(value_x)
    y.append(value_y)

if (x.count(x[0]) != 2):
    print(x[0], end=' ')
elif (x.count(x[1]) != 2):
    print(x[1], end=' ')
else:
    print(x[2], end=' ')

if (y.count(y[0]) != 2):
    print(y[0])
elif (y.count(y[1]) != 2):
    print(y[1])
else:
    print(y[2])