'''
n, w, L값 받기 # n: 트럭의 수, w: 다리의 길이, L: 다리의 최대하중
list(a 값 받기) : 트럭의 무게

def 최단 시간 구하기(트럭 리스트):
    다리 = deque()
    sumArray =

    if 다리의 길이 < 트럭 수:

    elif 다리의 길이 >= 트럭 수:

'''
from collections import deque

def getting_min_time(trucks: list):
    briedge = deque()
    sumArray = []
    temp = 0

    for i in range(len(trucks)):
        temp += trucks[i]
        sumArray.append(temp)




n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))


