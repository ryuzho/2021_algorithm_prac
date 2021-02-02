#2798번 블랙잭

N, M = map(int, input().split())
cards = list(map(int, input().split()))
temp = 0
cards_sum = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and j !=k and i != k:
                cards_sum = cards[i] + cards[j] + cards[k]
                if cards_sum >= temp and cards_sum <= M:
                    temp = cards_sum
                else:
                    cards_sum = temp

print(cards_sum)



