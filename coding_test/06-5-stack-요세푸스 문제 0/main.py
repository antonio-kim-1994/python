def josephus(n: int, k: int):
    people = list(range(1, n + 1)) # 특정 범위의 숫자를 생성, range(start, stop)
    result = []
    index = 0

    while len(people) > 0:
        index = (index + k - 1) % len(people)
        result.append(people.pop(index))

    return result


N, K = map(int, input().split())
result = josephus(N, K)
print('<' + ', '.join(map(str, result)) + '>')