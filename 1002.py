test_case = int(input())

for i in range(test_case):
    x1, y1, r1, x2, y2, r2 = input().split()
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    r1 = float(r1)
    r2 = float(r2)

    sum_of_r = r1 + r2 #반지름합
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 #두 점 사이 거리
    if (r1 > r2):#큰반지름, 작은반지름
        big_r = r1
        small_r = r2
    else:
        big_r = r2
        small_r = r1
    
    if (x1 == x2 and y1 == y2 and r1 == r2): #두 원의 일치
        print("-1")
    elif (sum_of_r == dist): #외접
        print("1")
    elif (big_r == dist + small_r): #내접
        print("1")
    elif (sum_of_r < dist): #외부에 위치한 두 원, 만나지 않음
        print("0")
    elif (big_r > dist + small_r): #내부에 위치한 두 원, 만나지 않음
        print("0")
    else:
        print("2")
        

    
