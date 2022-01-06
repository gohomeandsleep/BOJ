#endp만 받는 함수
"""
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

stp = int(input())
print(prime_list(stp))
"""
def prime_list(stp, endp):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (endp + 1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(endp ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(2 * i, endp + 1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    for i in range(stp, endp + 1):
        if (i != 1):
            if (sieve[i] == True):
                print(i)

stp, endp = input().split()
stp = int(stp)
endp = int(endp)
prime_list(stp, endp)

#이전 코드
"""
stp = int(stp)
endp = int(endp)

for i in range(stp, endp + 1):
    sqrt = int(i ** 0.5)
    count = 0
    target = sqrt
    #소수인지 판별
    for j in range(2, sqrt + 1):
        if (i % j == 0):
            break
        else:
            count = count + 1
    #소수임이 확인되면 출력
    if (count == sqrt - 1):
        print(i)
"""