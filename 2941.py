array = input()

sent = []

for i in range(len(array)):
    sent.append(array[i])

#First word is irrelative of Croatia Word, so primary value of word_num is 1
word_num = 1

#In second word, 'dz=' can make error, so have to make second detect code.
i = 1

#Code for Detect Croatia Word
if (len(sent) == 1):
    if (ord(sent[0]) == 32):
        word_num = 0
    else:
        word_num = 1

elif (ord(sent[i]) == 61):
    if (ord(sent[i-1]) != 99 and ord(sent[i-1]) != 115 and ord(sent[i-1]) != 122):
        word_num = word_num + 1
    
elif (ord(sent[i]) == 106):
    if (ord(sent[i-1]) != 108 and ord(sent[i-1]) != 110):
        word_num = word_num + 1
    
elif (ord(sent[i]) == 45):
    if (ord(sent[i-1]) != 100 and ord(sent[i-1]) != 99):
        word_num = word_num + 1
else:
    word_num = word_num + 1

#from third word, there is no problem.

for i in range(2, len(sent)):
    #Code for Detect Croatia Word
    if (ord(sent[i]) == 61):
        if (ord(sent[i-1]) == 122 and ord(sent[i-2]) == 100):
            word_num = word_num - 1 
        elif (ord(sent[i-1]) != 99 and ord(sent[i-1]) != 115 and ord(sent[i-1]) != 122):
            word_num = word_num + 1
    
    elif (ord(sent[i]) == 106):
        if (ord(sent[i-1]) != 108 and ord(sent[i-1]) != 110):
            word_num = word_num + 1

    elif (ord(sent[i]) == 45):
        if (ord(sent[i-1]) != 100 and ord(sent[i-1]) != 99):
            word_num = word_num + 1
    else:
        word_num = word_num + 1

print(word_num)