#1021번 회전하는 큐
import sys
class bidirection_queue():
    def __init__(self):
        self.arr = []

    def func2(self):
        temp = self.arr.pop(0)
        self.arr.append(temp)
        return self.arr
    def func3(self):
        temp = self.arr.pop()
        self.arr.insert(0,temp)
        return self.arr


N, M = map(int, input().split())

queue = bidirection_queue()
queue.arr = [i for i in range(1, N+1)]
nums = 0
func2_count = 0
func3_count = 0

nums = map(int, sys.stdin.readline().split())
for num in nums:
    index = 0 # 내가 찾는 숫자의 위치 
    while queue.arr[index] != num:
        index += 1
    while queue.arr[0] != num:
        if (index + 1) <= (len(queue.arr)//2) +1: #내가 찾는 숫자의 위치가 배열길이의 반 이하라면 2번 연산 수행
            queue.func2()
            func2_count += 1
        else:                                      #배열길이의 반보다 크면 3번 연산 수행
            queue.func3()
            func3_count += 1

    queue.arr.pop(0)


print(func2_count+func3_count)
        

