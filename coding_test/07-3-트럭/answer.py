from collections import deque

def min_time_to_cross_bridge(n, w, L, truck_weights):
    bridge = deque([0] * w)
    total_weight = 0
    time = 0
    index = 0

    # 트럭이 모두 통과하지 않은 조건문(total_weight이 0 이 될 때 종료)
    while index < n or total_weight > 0:
        time += 1

        # 트럭이 끝에 도달 할 경우 제외 후 전체 무게에서 제거
        total_weight -= bridge.popleft()

        if index < n and total_weight + truck_weights[index] <= L:
            # 새로운 트럭 추가
            bridge.append(truck_weights[index])
            total_weight += truck_weights[index]
            index += 1
        else:
            # 빈 공간 채우기
            bridge.append(0)

    return time

# 입력 받기
n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

# 결과 출력
print(min_time_to_cross_bridge(n, w, L, trucks))