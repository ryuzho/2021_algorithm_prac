#2210번 숫자판 점프
import sys
num_board = []

for _ in range(5):
    num_board.append(list(sys.stdin.readline().split()))

def dfs(x, y, num):

    if len(num) == 6:
        if num not in result:
            result.append(num)
        return
        
    for i in range(4):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + num_board[nx][ny])


result = []
for i in range(5):
    for j in range(5):
        dfs(i,j,num_board[i][j])

print(len(result))