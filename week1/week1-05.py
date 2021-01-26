#7568번 덩치

N = int(input())
arr = [0]*N

for i in range(N):
    x, y = map(int, input().split())
    arr[i] = [x,y]

for i in range(N):
    rank = 1
    for j in range(N):
        if i != j and arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1
    print(rank, end =" ")
        


