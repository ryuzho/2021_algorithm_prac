#2667번 단지번호 붙이기 
from collections import deque
import sys
input = sys.stdin.readline

q = deque([])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    house_cnt = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < N and matrix[x][y] == 1:
                matrix[x][y] = 0
                house_cnt += 1
                q.append([x,y])

    return house_cnt

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().strip())))

result = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            matrix[i][j] = 0
            q.append([i,j])
            result.append(bfs())


print(len(result))
for ans in (sorted(result)):
    print(ans)