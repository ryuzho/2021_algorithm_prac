#2178번 미로 탐색
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    q = deque([[x,y]])
    maze[x][y] = 1

    while q:
        a,b = q.popleft()
        if a == N-1 and b == M-1:
            print(maze[a][b])

        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and maze[x][y] == 1:
                maze[x][y] = maze[a][b] + 1
                q.append([x,y])

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().strip())))

bfs(0,0)

