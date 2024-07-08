def pop_balloon(arr: list[int]):
    total_range = list(range(1, count + 1))
    current_index = 0
    result = []

    while total_range:
        balloon_index = total_range.pop(current_index)
        result.append(balloon_index)
        if not total_range:
            break

        move = arr[balloon_index - 1] # total_range를 1부터 시작, 각 위치의 값을 얻기 위해 -1

        if move > 0: # 양수인 경우
            current_index = (current_index + (move - 1)) % len(total_range)
            # total_range에서 값을 하나 pop 했기 때문에 -1
            # 전체 index 길이를 넘지 않기 위해 % 연산자 사용
        else:
            current_index = (current_index + move) % len(total_range)
    return result


count = int(input())
numbers = list(map(int, input().split()))
print(" ".join(map(str, pop_balloon(numbers))))