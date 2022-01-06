import itertools as it

card_num, target_num = input().split()

card_num = int(card_num)
target_num = int(target_num)

card_deck = []

card_deck = input().split()

for i in range(card_num):
    card_deck[i] = int(card_deck[i])

result = list(it.permutations(card_deck,3))

answer = 0

for i in range(len(result)):
    ans = 0
    for j in range(3):
        ans = ans + result[i][j]
    if (ans <= target_num and ans > answer):
        answer = ans

print(answer)