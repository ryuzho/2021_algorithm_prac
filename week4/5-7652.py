#7652번 나이트의 이동
import sys
input = sys.stdin.readline
from collections import deque

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]
def bfs(x0, y0):
    q = deque([[x0,y0]])
    chess_board[x0][y0] = 1

    while q:
        a,b = q.popleft()
        if a == target_x and b == target_y:
            print(chess_board[a][b] - 1)
            return

        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < line_length and 0 <= y < line_length and chess_board[x][y] == 0:
                chess_board[x][y] = chess_board[a][b] + 1 #각 자리에 이동횟수를 기록
                q.append([x,y])


T = int(input())
for _ in range(T):
    line_length = int(input())
    chess_board = [[0]*line_length for _ in range(line_length)]
    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    bfs(start_x, start_y)