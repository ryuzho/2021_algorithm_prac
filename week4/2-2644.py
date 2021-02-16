#2644번 촌수계산
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    arr = []
    queue = deque([start])
    visited = [False]*(n+1)
    visited[start] = True

    while queue:
        v = queue.popleft()
        arr.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return arr       
        

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
dfs_arr = []
for i in range(m):
    x, y = map(int, input().split()) # x는 y의 부모
    graph[y].append(x)

A = set(bfs(a))
B = set(bfs(b))

result = len((A|B) - (A&B))
if result == len(A) + len(B):
    print("-1")
else:
    print(result)


