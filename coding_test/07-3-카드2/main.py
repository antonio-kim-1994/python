from collections import deque

def find_last_number(initNum: int):
    queue = deque(range(1, initNum+1))

    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())

    print(queue[0])


cardNumber = int(input())
find_last_number(cardNumber)