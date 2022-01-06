array = input()

sent = []

for i in range(len(array)):
    sent.append(array[i])

alpha = []

for i in range(26):
    alpha.append(0)

mxm_count = 0
mxm_char = 0
same_count = 0

for i in range(len(sent)):

    if (ord(sent[i]) > 64 and ord(sent[i]) < 91):
        num = int(ord(sent[i])) - 65
        alpha[num] = int(alpha[num]) + 1
        if (alpha[num] > mxm_count):
            mxm_count = alpha[num]
            mxm_char = num
            same_count = 0
        elif (alpha[num] == mxm_count):
            same_count = 1
    if (ord(sent[i]) > 96 and ord(sent[i]) < 123):
        num = int(ord(sent[i])) - 97
        alpha[num] = int(alpha[num]) + 1
        if (alpha[num] > mxm_count):
            mxm_count = alpha[num]  
            mxm_char = num  
            same_count = 0
        elif (alpha[num] == mxm_count):
            same_count = 1

if (same_count == 1):
    print("?")
else:
    print(chr(mxm_char + 65))