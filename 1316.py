test_case = int(input())

word_box = []

group_word = 0

for i in range(test_case):
    checker = 0
    array = []
    word = input()
    for i in range(len(word)):
        array.append(word[i])

    alpha = []
    for i in range(len(word)):
        if (alpha.count(array[i]) == 0):
            alpha.append(array[i])
        elif (array[i] != array[i-1]):
            checker = 1
    
    if (checker == 0):
        group_word = group_word + 1
            
print(group_word)