#1969번 DNA

N, M = map(int, input().split())

H_distance = 0
DNA = []
result = []
for i in range(N):
    DNA.append(list(input()))



for i in range(M):
    DNA_cnt = [['A', 0],['T', 0],['G', 0],['C', 0]]
    for j in range(N):
        if DNA[j][i] == 'A':
            DNA_cnt[0][1] += 1
        elif DNA[j][i] == 'T':
            DNA_cnt[1][1] += 1
        elif DNA[j][i] == 'G':
            DNA_cnt[2][1] += 1
        elif DNA[j][i] == 'C':
            DNA_cnt[3][1] += 1
    
    New_DNA = sorted(DNA_cnt, key = lambda x : (-x[1], x[0]))
    print(New_DNA[0][0],end='')

    for j in range(N):
        if DNA[j][i] != New_DNA[0][0]:
            H_distance += 1

print("")
print(H_distance)
