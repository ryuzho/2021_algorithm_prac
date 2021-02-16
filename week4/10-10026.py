#10026번 적록색약
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque([])
def bfs(rgb):
    while q:
        a,b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < N and visited[x][y] == False and matrix[x][y] in rgb:
                visited[x][y] = True
                q.append([x,y])

    

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(input().strip()))

visited = [[False] * N for _ in range(N)]
section = 0
rg_section = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            if matrix[i][j] == "R":
                visited[i][j] = True
                q.append([i,j])
                bfs(["R"])
                section += 1
            elif matrix[i][j] == "G":
                visited[i][j] = True
                q.append([i,j])
                bfs(["G"])
                section += 1
            elif matrix[i][j] == "B":
                visited[i][j] = True
                q.append([i,j])
                bfs(["B"])
                section += 1
        
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            if matrix[i][j] == "R" or matrix[i][j] == "G":
                visited[i][j] = True
                q.append([i,j])
                bfs(["R","G"])
                rg_section += 1
            elif matrix[i][j] == "B":
                visited[i][j] = True
                q.append([i,j])
                bfs(["B"])
                rg_section += 1

print("{0} {1}".format(section, rg_section))
