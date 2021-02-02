#2231번 분해합

def n_sum(num):
    temp = 0
    while num > 0:
        temp += num % 10
        num //= 10
    return temp




N = int(input())

count = 0
temp = N
while temp > 0:
    temp //= 10
    count += 1

M = N - 9*count

for i in range(M, N+1):
    if i + n_sum(i) == N:
        print(i)
        break
    if i == N:
        print(i-N)




    