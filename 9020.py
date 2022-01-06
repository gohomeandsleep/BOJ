def is_it_prime(n):
    result = 0
    sqrt = int(n ** 0.5) + 1

    for i in range(2, sqrt):
        if (n % i == 0):
            result = 1 #합성수
    
    if (result == 1): #합성수이면 1
        return 1
    else: #소수이면 0
        return 0

test_case = int(input())

for i in range(test_case):
    num = int(input())
    half = int(num / 2)
    for i in range(half):
        target = half - i
        ans = is_it_prime(target)
        target2 = half + i
        ans2 = is_it_prime(target2)
        if (ans == 0 and ans2 == 0):
            print(target, target2)
            break