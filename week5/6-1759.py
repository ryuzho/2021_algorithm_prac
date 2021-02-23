#1759번 암호 만들기
import sys
sys.setrecursionlimit(50000)

def dfs(start, length):
    if length == L:
        is_vowel_exist = False
        consonant_count = 0
        for k in password:
            if k in ['a','e','i','o','u']:
                is_vowel_exist = True
            else: consonant_count += 1
        if is_vowel_exist == True and consonant_count > 1:
            for j in password:
                print(j, end = '')
            print()
        return

    for i in range(start, C):
        password[length] = alphabets[i]
        dfs(i+1, length+1)



L, C = map(int, sys.stdin.readline().split())
alphabets = list(sys.stdin.readline().split())
password = [0]*L

alphabets.sort()

dfs(0,0)
