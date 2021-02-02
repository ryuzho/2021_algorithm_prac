#1874 스택 수열
class stack:
    
    def __init__(self):
        self.arr = []
    def push(self, n):
        self.arr.append(n)
    def pop(self):
        if len(self.arr) == 0:
            return -1
        else:
            self.arr.pop()
    def top(self):
        if len(self.arr) == 0:
            return -1
        else:
            return self.arr[-1]


N = int(input())
N_list = []
for i in range(N):
    N_list.append(int(input()))


s = stack()
i = 0
j = 0
result=[]
cnt = 1

while j < N:

    if len(result) > 2* N:
        print("NO")
        cnt = 0
        break

    elif s.top() == N_list[j]: # 4 3 6 8 7 5 2 1
        s.pop()
        result.append("-")
        j += 1
    
    else:
        i += 1
        s.push(i)
        result.append("+")

    

if cnt != 0:
    for i in result:
        print(i)
