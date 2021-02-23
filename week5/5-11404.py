#11404 플로이드
import sys
input = sys.stdin.readline

INF = float('inf')

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(n):
    graph[i+1][i+1] = 0

for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == k or b == k:
                continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in graph[1:]:
    for x in range(1,n+1):
        if i[x] == INF:
            i[x] = 0
        print(i[x], end = ' ')
    print()