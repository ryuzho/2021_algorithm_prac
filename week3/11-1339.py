#1339번 단어 수학
import sys

N = int(sys.stdin.readline())
num = [0,1,2,3,4,5,6,7,8,9]
words = []
alpha = {}

for i in range(N):
    words = list(sys.stdin.readline().strip())
    for j in range(len(words)):
        if words[j] not in alpha:
            alpha[words[j]] = 10**(len(words)-j-1)
        else:
            alpha[words[j]] += 10**(len(words)-j-1)

alpha = sorted(alpha.items(), key = lambda x : -x[1])

sum = 0
for i in alpha:
    sum += i[1]*num.pop()

print(sum)