#2941번 크로아티아 알파벳

string = input()



i = 0
count = 0
while i<len(string):
    if string[i:i+2] == "c=" or string[i:i+2] == "c-" or string[i:i+2] == "d-"\
    or string[i:i+2] == "lj" or string[i:i+2] =="nj" or string[i:i+2] =="s=" or string[i:i+2] =="z=":
        count += 1
        i += 2
       
    elif string[i:i+3] == "dz=":
        count += 1
        i += 3
    else:
        count += 1
        i += 1

print(count)