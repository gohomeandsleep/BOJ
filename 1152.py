array = input()

sent = []
conf_sent = []

for i in range(len(array)):
    sent.append(array[i])

word_num = 0

# 공백은 아스키 코드로 32번

if (ord(sent[0]) == 32): 
    if (ord(sent[len(sent) - 1]) == 32):
        for i in range(len(sent) - 2):
            conf_sent.append(sent[i+1])    
    else:
        for i in range(len(sent) - 1):
            conf_sent.append(sent[i+1])
elif (ord(sent[len(sent) - 1]) == 32):
    for i in range(len(sent) - 1):
        conf_sent.append(sent[i])
else:
    for i in range(len(sent)):
        conf_sent.append(sent[i])

for i in range(len(conf_sent)):
    if (ord(conf_sent[i]) == 32):
        if (ord(conf_sent[i-1]) != 32):
            word_num = word_num + 1

if (len(conf_sent) == 0):
    print("0")
elif (len(conf_sent) == 1 and ord(conf_sent[0]) == 32):
    print("0")
elif (ord(conf_sent[len(conf_sent) - 1]) == 32):
    print(word_num)
else:
    print(word_num + 1)