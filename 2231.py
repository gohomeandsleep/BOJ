n = int(input())
answer = 1000000
for i in range(1, n):
    target = n - i
    target2 = target
    chr_n = str(target)

    for i in range(len(chr_n)):
        target2 = target2 + int(chr_n[i])

    if (n == target2):
        if (target < answer):
            answer = target

if (n == 2): 
    print("1")
elif (answer == 1000000):
    print("0")
else:
    print(answer)
