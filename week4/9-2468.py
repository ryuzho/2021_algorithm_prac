#2468번 안전 영역
from collections import deque
import sys
input = sys.stdin.readline
import copy

N = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque([])
def bfs(matrix, rain_height):
    while q:
        a,b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < N and matrix[x][y] > rain_height:
                matrix[x][y] = 0
                q.append([x,y])


matrix = []
temp = 0
for _ in range(N):
    matrix.append(list(map(int, input().split())))


for rain_height in range(101):
    my_matrix = copy.deepcopy(matrix)
    result = 0
    for i in range(N):
        for j in range(N):
            if my_matrix[i][j] > rain_height:
                q.append([i,j])
                bfs(my_matrix, rain_height)
                result += 1

    temp = max(temp, result)

print(temp)