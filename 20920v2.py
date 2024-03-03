import sys
input = sys.stdin.readline

n, m = map(int, input().split())

word_list = {}

for i in range(n):
    word = input().rstrip()
    if len(word)<m: continue
    if word not in word_list: word_list[word] = 1
    else: word_list[word] += 1

res = sorted(word_list.items(), key=lambda x : (-x[1], -len(x[0]) , x[0]))

for i in range(len(res)):
    print(res[i][0])