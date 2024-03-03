import sys
input = sys.stdin.readline
#n은 입력되는 단어의 수, m은 최소 길이(이상)
n, m = map(int, input().split())

word_list = []
word_freq = []
word_len = []
#단어 길이 확인해보고 m보다 길면 추가, 빈도와 길이 추가
for i in range(n):
    word = input().rstrip()
    if len(word)>=m:
        if word not in word_list:
            word_list.append(word)
            word_freq.append(1)
            word_len.append(len(word))
        else:
            temp_freq = word_list.index(word)
            word_freq[temp_freq] += 1
#빈도, 길이는 내림차순인데 사전순은 오름차순이므로 빈도,길이를 역전
max_freq = max(word_freq)
max_len = max(word_len)
for i in range(len(word_list)):
    word_freq[i] = max_freq- word_freq[i]
    word_len[i] = max_len - word_len[i]
#정렬을 위해 빈도, 길이, 단어를 한 리스트에 묶음
array = []
for i in range(len(word_list)):
    temp_array = (word_freq[i], word_len[i], word_list[i])
    array.append(temp_array)
#정렬 후 출력
sorted_array = sorted(array, key=lambda x: (x[0],x[1],x[2]))
for i in range(len(word_list)):
    print(sorted_array[i][2])
