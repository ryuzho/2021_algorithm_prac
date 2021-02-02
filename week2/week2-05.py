#2751번 수 정렬하기 2

N = int(input())

arr = []

for i in range(N):
    arr.append(int(input()))

arr = sorted(arr)

for i in range(N):
    print(arr[i])
