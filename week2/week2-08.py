#10814번 나이순 정렬
import sys
N = int(input())

arr = []
for i in range(N):
    arr.append(sys.stdin.readline().split())

arr = sorted(arr, key = lambda x : int(x[0]))

for i in range(N):
    print("{} {}".format(arr[i][0], arr[i][1]))

