import itertools

test_case = int(input())

test_case_list = []
weight = []
height = []

for i in range(test_case):
    test_case_list.append(i)

for i in range(test_case):
    x, y = input().split()
    x = int(x)
    y = int(y)
    weight.append(x)
    height.append(y)

result = list(itertools.combinations(test_case_list,2))

score_list = []
for i in range(test_case):
    score_list.append(0)

for i in range(len(result)):
    w_a = weight[result[i][0]]
    w_b = weight[result[i][1]]
    h_a = height[result[i][0]]
    h_b = height[result[i][1]]
    if (w_a > w_b and h_a > h_b):
        score_list[result[i][0]] = score_list[result[i][0]] + 2
        #print(score_list)
    elif (w_b > w_a and h_b > h_a):
        score_list[result[i][1]] = score_list[result[i][1]] + 2
        #print(score_list)       
    else:
        if ((w_a == w_b and h_a > h_b) or (h_a == h_b and w_a > w_b)):
            score_list[result[i][0]] = score_list[result[i][0]] + 2
        elif ((w_b == w_a and h_b > h_a) or (h_b == h_a and w_b > w_a)):
            score_list[result[i][1]] = score_list[result[i][1]] + 2   
        else:                
            score_list[result[i][0]] = score_list[result[i][0]] + 1
            score_list[result[i][1]] = score_list[result[i][1]] + 1
        #print(score_list)

#print(score_list)
#score_list에 있는 값들 정렬, 내림차순 정리

#print(score_list)

pset=sorted(score_list)
pset.reverse()

#print(pset)

p_ind=[]
#p_ind에 순위값을 기록
for i in score_list:
    ans = pset.index(i) + 1
    p_ind.append(ans)

for i in range(test_case):
    for j in range(test_case):
        if (weight[i] == weight[j] or height[i] == height[j]):
            if (p_ind[i] > p_ind[j]):
                p_ind[i] = p_ind[i] - 1

#print(p_ind)
#정리된 값을 출력
for i in range(test_case):
    print(p_ind[i], end='')
    if (i != test_case - 1):
        print("",end=' ')