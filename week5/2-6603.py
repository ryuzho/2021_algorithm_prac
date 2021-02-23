#6603번 로또
import sys
input = sys.stdin.readline

def dfs(start,length):
    if length == 6:
        for i in range(6):
            print(lotto[i], end = ' ')
        print()
        return

    for i in range(start,k):
        lotto[length] = numbers[i]
        dfs(i+1, length+1)

lotto = [0 for _ in range(6)]

while True:
    numbers = list(map(int, input().split()))
    k = numbers.pop(0)
    if k == 0:
        break
    dfs(0,0)
    print()


