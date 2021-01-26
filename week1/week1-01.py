#2739번 구구단

N = int(input())
for i in range(1, 10):
    print("{0} * {1} = {2}".format(N, i, N*i))