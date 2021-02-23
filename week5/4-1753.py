#1753번 최단경로
import heapq
import sys
input = sys.stdin.readline

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



V, E = map(int, input().split())
K = int(input())
distances = [float('inf')]*(V+1)
graph = [[] for _ in range(V+1)]
heap = []
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((w,v))
    
dijkstra(K)
for i in range(1,V+1):
    if distances[i] == float('inf'):
        print("INF")
    else: print(distances[i])