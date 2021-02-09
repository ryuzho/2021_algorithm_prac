#1431번 시리얼 번호

N = int(input())
info_arr = [] # info = [name, length, sum_of_nums, isAlpha]

for i in range(N):
    name = input()
    length = len(name)
    sum_of_nums = 0
    for i in name:
        if i.isdigit() == True:
            sum_of_nums += int(i)
   
    info_arr.append([name, length, sum_of_nums])

result = sorted(info_arr, key = lambda x : (x[1], x[2], x[0]))


for i in range(N):
    print(result[i][0])