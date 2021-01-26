#1018번 체스판 다시 칠하기

N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]

W_chess = [['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W']]

B_chess = [['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B'],
           ['B','W','B','W','B','W','B','W'],
           ['W','B','W','B','W','B','W','B']]

temp = 3000 #MAX

for i in range(N):
    arr[i] = list(input())


pick_arr = [[0]*8 for _ in range(8)]

for a in range(0, N-7):
    for b in range(0, M-7):
        for i in range(8):
            for j in range(8):
                pick_arr[i][j] = arr[i+a][j+b]

        count_w = 0
        count_b = 0

        for i in range(8):
            for j in range(8):
                if pick_arr[i][j] != W_chess[i][j]:
                    count_w += 1
                if pick_arr[i][j] != B_chess[i][j]:
                    count_b += 1
        min_count = min(count_w, count_b)
        if min_count <= temp:
            temp = min_count

print(temp)
            
                








