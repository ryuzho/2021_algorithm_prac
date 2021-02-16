#1325번 효율적인 해킹
from collections import deque
import sys

# def dfs(graph, v, visited):
#     global edge_count
#     visited[v] = True

#     for i in graph[v]:
#         if not visited[i]:
#             edge_count += 1
#             dfs(graph, i, visited)
# dfs 시간초과

def bfs(start):
    edge_count = 0
    queue = deque([start])
    visited = [False]*(N+1)
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                edge_count += 1
                queue.append(i)
                visited[i] = True

    return edge_count


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[y].append(x)

temp = 0
result = []
for i in range(1,N+1):
    cnt = bfs(i)
    if cnt > temp:
        temp = cnt
        result = []
        result.append(i)
    elif cnt == temp:
        result.append(i)

for i in result:
    print(i, end = ' ')
    

    


