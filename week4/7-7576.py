#7576번 토마토
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    q = deque([])

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                q.append([i,j])

    while q:
        a,b = q.popleft()
        result_x,result_y = a,b
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and box[x][y] == 0:
                box[x][y] = box[a][b] + 1
                q.append([x,y])
    return box[a][b]

    
                
M, N = map(int, input().split())
box = []
for _ in range(N):
    box.append(list(map(int, input().split())))

result = bfs()
is_zero_exist = False
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            is_zero_exist = True

if is_zero_exist == False:
    print(result - 1)
else: print(-1)

    



    

    
# #7576번 토마토
# from collections import deque
# import sys
# input = sys.stdin.readline
# import copy

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# def bfs(x,y):
#     q = deque([[x,y]])
#     box[x][y] = 1

#     while q:
#         a,b = q.popleft()
#         if box[a][b] == stop_sign:
#             return 

#         for i in range(4):
#             x = a + dx[i]
#             y = b + dy[i]
#             if 0 <= x < N and 0 <= y < M and box[x][y] == 0:
#                 box[x][y] = box[a][b] + 1
#                 q.append([x,y])
                


# M, N = map(int, input().split())
# box = []
# for _ in range(N):
#     box.append(list(map(int, input().split())))
    

# temp = copy.deepcopy(box)

# starts = []
# for i in range(N):
#     for j in range(M):
#         if box[i][j] == 1:
#             starts.append([i,j])



# for stop_sign in range(1, N*M):
#     is_zero_exist = False
#     all_tomato_good = False
#     for start in starts:
#         bfs(start[0], start[1])

#     for i in range(N):
#         for j in range(M):
#             if box[i][j] == 0:
#                 is_zero_exist = True

#     if is_zero_exist == False:
#         print(stop_sign - 1)
#         all_tomato_good = True
#         break        
#     box = copy.deepcopy(temp)

# if all_tomato_good == False:
#     print("-1")


    

    