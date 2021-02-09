#1018번 체스판 다시 칠하기

N, M = map(int, input().split())
arr = []
temp = float('inf')
for i in range(N):
    arr.append(list(input()))

for a in range(0, N-7):
    for b in range(0, M-7):
        W_count = 0
        B_count = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2 == 0:
                    if arr[i][j] != "W":
                        W_count += 1
                    elif arr[i][j] != "B":
                        B_count += 1
                elif (i+j)%2 == 1:
                    if arr[i][j] != "B":
                        W_count += 1
                    elif arr[i][j] != "W":
                        B_count += 1
        if min(W_count, B_count) < temp:
            temp = min(W_count, B_count)


print(temp)





