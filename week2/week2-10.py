#2609번 최대공약수와 최소공배수

a, b = map(int, input().split())

def find_GCD(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    elif a == b:
        return a
    elif a > b:
        return find_GCD(a%b, b)
    elif a < b:
        return find_GCD(a, b%a)
   


GCD = find_GCD(a, b)
LCM = (a//GCD ) * (b//GCD) * GCD

print(GCD)
print(LCM)
