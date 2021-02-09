#11279번 최대힙
import heapq
import sys
heap = []

N = int(sys.stdin.readline())
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-x, x))



# class MaxHeap:
#     def __init__(self):
#         self.data = [None] #힙은 1번 인덱스부터 시작, 0번은 비워둠
    
#     def insert(self, item):
#         self.data.append(item)
#         i = len(self.data)-1

#         while i>1:
#             if self.data[i] > self.data[i//2]:
#                 self.data[i],self.data[i//2] = self.data[i//2],self.data[i]
#                 i = i//2
#             else: break
    
#     def remove(self):
#         if len(self.data) > 1:
#             self.data[1],self.data[-1] = self.data[-1],self.data[1]
#             data = self.data.pop()
#             self.maxHeapify(1)
#         else:
#             data = None
#         return data

    
#     def maxHeapify(self, i):
#         left = i*2
#         right = i*2 + 1
#         temp = i

#         if left<len(self.data) and self.data[i] < self.data[left]:
#             temp = left
#         if right<len(self.data) and self.data[i] < self.data[right]:
#             temp = right
        
#         if temp != i:
#             self.data[i], self.data[temp] = self.data[temp], self.data[i]
#             self.maxHeapify(temp)

# h = MaxHeap()
# result = []
# N = int(input())
# for i in range(N):
#     x = int(input())
#     if x == 0:
#         top = h.remove()
#         if top == None:
#             result.append(0)
#         else:
#             result.append(top)
#     else:
#         h.insert(x)

# for i in result:
#     print(i)