#1012번 유기농 배추
import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000) #recursionlimit 반드시 걸어줘야 함

def dfs(x,y):
    matrix[x][y] = 0
    result.append((x,y))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == 1:
                dfs(nx,ny)


result = []
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[N-y-1][x] = 1



    count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                dfs(i,j)
                count += 1
                
    print(count)

