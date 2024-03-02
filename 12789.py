import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

temp_list = []
stat = True
current = 1
loop = True

while loop == True:
    #if num_list != [] and temp_list != []:
        #print(current, num_list[0], temp_list[-1])

    if num_list == [] and temp_list == []:
        #넘리스트와 임시리스트가 모두 비었을경우 정지
        print("Nice")
        loop = False

    elif num_list != [] and current == num_list[0]: 
        #넘리스트값이 현재와 같을경우 제거
        num_list.remove(current)
        current += 1
        #print(num_list, temp_list)

    elif temp_list != [] and current == temp_list[-1]: 
        #임시리스트 마지막값이 현재와 같을 경우 제거
        temp_list.remove(current)
        current += 1
        #print(num_list, temp_list)

    elif num_list != [] and current < num_list[0]:
        #넘리스트0 값이 큰 경우 임시리스트로 이동
        temp_list.append(num_list[0])
        num_list.pop(0)
        #print(num_list, temp_list) 

    elif num_list == [] and current != temp_list[-1]:
        #넘리스트가 비었고 임시리스트 마지막 값이 다를경우 불가능
        print("Sad")
        loop = False
    
#wow!