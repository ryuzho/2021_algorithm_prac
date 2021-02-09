#1927 최소 힙
import sys
import heapq

heap = []

N = int(sys.stdin.readline())
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print("0")
    
    else:
        heapq.heappush(heap, x)
        