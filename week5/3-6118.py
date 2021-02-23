#6118번 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    max_temp = 0
    q = deque([start])
    visited[start] = 1

    while q:
        n = q.popleft()
        result.append(n)

        for i in graph[n]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[n]+1

    

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
result = []
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(1)
answer = []
max_depth = sorted(visited)[N]

for i in range(1,N+1):
    if visited[i] == max_depth:
        answer.append(i)

print("{} {} {}".format(answer[0], max_depth-1, len(answer)))


