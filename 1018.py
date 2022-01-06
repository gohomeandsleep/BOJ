total_x , total_y = input().split()

total_x = int(total_x)
total_y = int(total_y)

# 배열 생성 확인 코드
# for i in range(total_y):
#     for j in range(total_x):
#         array[i][j] = 0
#         print(array[i][j], end=' ')
#     print()

two_d = [list(input()) for _ in range(total_x)]
#print("List product ok...")
#print(two_d)
target = 32

total_try_count = (total_y - 7) * (total_x - 7)
#print(total_try_count)

for i in range(total_y - 7):
    for j in range(total_x - 7): 
        flip_count = 0 #뒤집는 횟수 초기화

        for k in range (8):
            for l in range (8):
                if (k % 2 == 0):
                    if (l % 2 == 0):
                        if (two_d[j+l][i+k] == "B"):
                            flip_count = flip_count + 1
                            #print("Change : ", j+l, i + k)                               
                    else:
                        if (two_d[j+l][i+k] == "W"):
                            flip_count = flip_count + 1
                            #print("Change : ", j+l, i + k)   
                else:
                    if (l % 2 == 0):
                        if (two_d[j+l][i+k] == "W"):
                            flip_count = flip_count + 1
                            #print("Change : ", j+l, i + k)                               
                    else:
                        if (two_d[j+l][i+k] == "B"):
                            flip_count = flip_count + 1
                            #print("Change : ", j+l, i + k)      
                # if (two_d[j + 2 * l][i+k] == "W"):
                #     print("Change : ", j + 2 * l, i + k)
                #     flip_count = flip_count + 1
                # if (two_d[j + 1 + 2 * l][i+k] == "B"):
                #     print("Change : ", 1 + j + 2 * l, i + k)                    
                #     flip_count = flip_count + 1
        #print(flip_count)            
        if (flip_count > 32):
            flip_count = 64 - flip_count
        if (flip_count < target):
            target = flip_count

print(target)