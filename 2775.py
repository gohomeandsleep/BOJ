test_case = int(input())

k = []
n = []
mxm_k = 0
mxm_n = 0

for i in range(test_case):
    k.append(int(input()))
    if (k[i] + 1 > mxm_k + 1):
        mxm_k = k[i] + 1

    n.append(int(input()))
    if (n[i] > mxm_n):
        mxm_n = n[i]


apt = [[0 for col in range(mxm_n)] for row in range(mxm_k + 1)]

for i in range(mxm_n): #세로 줄에 1을 배치
    apt[0][i] = i + 1

for j in range(mxm_k+1): #가로 줄에 n을 배치
    apt[j][0] = 1

#array[가로(호수)][세로(층)]

for j in range(mxm_k):
    for i in range(mxm_n - 1):
        apt[j+1][i+1] = int(apt[j+1][i]) + int(apt[j][i+1])

for i in range(test_case):
    print(apt[k[i]][n[i] - 1])
