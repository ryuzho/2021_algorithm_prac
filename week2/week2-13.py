#2257번 화학식량

arr = list(input())
stack = []
i = 0


while i!=len(arr):
    temp = 0
    if arr[i] == "H" or arr[i] == "C" or arr[i] == "O" or arr[i] == "(":
        stack.append(arr[i])
        i += 1
    elif arr[i].isdigit() == True and 1 < int(arr[i]) < 10:
        if stack[-1] == "H":
            temp = 1*int(arr[i])
        elif stack[-1] == "C":
            temp = 12*int(arr[i])
        elif stack[-1] == "O":
            temp = 16*int(arr[i])
        else:
            temp = int(stack[-1])*int(arr[i])

        stack.pop()
        stack.append(str(temp))
        i += 1
    
    

    elif arr[i] == ")":
        while stack[-1] != "(":
            if stack[-1] == "H":
                temp += 1
            elif stack[-1] == "C":
                temp += 12
            elif stack[-1] == "O":
                temp += 16
            else:
                temp += int(stack[-1])

            stack.pop()

        stack.pop()
        stack.append(str(temp))
        i += 1

result = 0
while len(stack) != 0:
    if stack[-1] == "H":
        result += 1
    elif stack[-1] == "C":
        result += 12
    elif stack[-1] == "O":
        result+= 16
    else:
        result += int(stack[-1])
    
    stack.pop()

print(result)



        
