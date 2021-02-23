#1916번 최소비용 구하기
import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start):
    distances[start] = 0
    heapq.heappush(heap, (distances[start], start))

    while heap:
        current_distance, current_destination = heapq.heappop(heap)

        if distances[current_destination] < current_distance:
            continue

        for new_distance, new_destination in graph[current_destination]:
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(heap, (distance, new_destination))
    
    return distances



N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distances = [INF]*(N+1)
heap = []
for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((w,v))
start_num, dest_num = map(int, input().split())

dijkstra(start_num)
print(distances[dest_num])