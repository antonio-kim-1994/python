'''
- push X: 정수 X를 큐에 넣는 연산이다.
- pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- size: 큐에 들어있는 정수의 개수를 출력한다.
- empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
- front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import readline
# import sys
# def queue(command: list):
#     result = []
#     for cmd in command:
#         if cmd[0] == 'push':
#             result.append(int(cmd[1]))
#         else:
#             if cmd[0] == 'pop':
#                 print(result.pop(0)) if result else print(-1)
#             elif cmd[0] == 'size':
#                 print(len(result))
#             elif cmd[0] == 'empty':
#                 print(0) if result else print(1)
#             elif cmd[0] == 'front':
#                 print(result[0]) if result else print(-1)
#             elif cmd[0] == 'back':
#                 print(result[-1]) if result else print(-1)
#
#
# line_num = int(input())
# commands = [input().split() for _ in range(line_num)]
# queue(commands)

import sys
from collections import deque


def queue(numbers: int):
    result = deque()

    for i in range(numbers):
        cmd = sys.stdin.readline().split()
        if cmd[0] == 'push':
            result.append(int(cmd[1]))
        elif cmd[0] == 'pop':
            print(result.popleft()) if result else print(-1)
        elif cmd[0] == 'size':
            print(len(result))
        elif cmd[0] == 'empty':
            print(0) if result else print(1)
        elif cmd[0] == 'front':
            print(result[0]) if result else print(-1)
        elif cmd[0] == 'back':
            print(result[-1]) if result else print(-1)


line_num = int(input())
queue(line_num)