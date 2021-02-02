#18258번 큐2
import sys

N = int(input())
queue = []
cnt = 0

for i in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        queue.append(int(cmd[1]))

    elif cmd[0] == "pop":
        if len(queue) == cnt:
            print(-1)
        else:
            print(queue[cnt])
            cnt += 1

    elif cmd[0] == "size":
        print(len(queue)-cnt)

    elif cmd[0] == "empty":
        if len(queue) == cnt:
            print(1)
        else:
            print(0)

    elif cmd[0] == "front":
        if len(queue) == cnt:
            print(-1)
        else:
            print(queue[cnt])

    elif cmd[0] == "back":
        if len(queue) == cnt:
            print(-1)
        else:
            print(queue[-1])



# import sys

# N = int(input())
# queue = []

# for i in range(N):
#     cmd = sys.stdin.readline().split()
#     if cmd[0] == "push":
#         queue.append(int(cmd[1]))

#     elif cmd[0] == "pop":
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[0])
#             queue = queue[1:]

#     elif cmd[0] == "size":
#         print(len(queue))

#     elif cmd[0] == "empty":
#         if len(queue) == 0:
#             print(1)
#         else:
#             print(0)

#     elif cmd[0] == "front":
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[0])

#     elif cmd[0] == "back":
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[len(queue)-1])
