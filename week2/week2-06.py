#10989번 수 정렬하기 3

import sys

N = int(input())
arr = [0]*10001
for i in range(N):
    arr[int(sys.stdin.readline())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)