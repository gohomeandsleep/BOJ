import math as m
target = int(input())
check = 0

if (target != 1):
    while check == 0:
        target_count = int(m.sqrt(target + 1)) - 1
        count = 0

        for i in range(2, int(m.sqrt(target + 1)) + 1):
            if (target % i == 0):
                print(i)
                target = int(target) / i
                break
            else:
                count = count + 1

        if (target_count == count):
            print(int(target))
            check = 1
            break
        
        