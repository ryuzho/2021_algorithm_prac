#1182번 부분수열의 합
import sys
input = sys.stdin.readline
# from itertools import combinations

# N, S = map(int, input().split())
# num_list = []
# result = 0
# num_list = list(map(int, input().split()))

# for i in range(len(num_list)):
#     combination_Set = list(combinations(num_list, i+1))
#     for j in range(len(combination_Set)):
#         if sum(combination_Set[j]) == S:
#             result += 1

# print(result)
N, S = map(int, input().split())
num_list = list(map(int, input().split()))
result = 0

def sum_set(idx, total):
    global result
    if idx > N-1:
        return
    total += num_list[idx]
    if total == S:
        result += 1
    
    sum_set(idx+1,total-num_list[idx])
    sum_set(idx+1,total)

sum_set(0,0)
print(result)