def insertion_sort(arr, N, K):
    store_count = 0  # 저장된 횟수 추적

    for i in range(1, N):
        loc = i - 1
        newItem = arr[i]

        # newItem이 삽입될 위치를 찾을 때까지 loc를 감소시키며 반복
        while loc >= 0 and newItem < arr[loc]:
            arr[loc + 1] = arr[loc]
            store_count += 1
            if store_count == K:
                return arr[loc]  # K번째 저장 순간의 값을 반환
            loc -= 1

        # 삽입 위치에 newItem 배치
        if loc + 1 != i:
            arr[loc + 1] = newItem
            store_count += 1
            if store_count == K:
                return arr[loc]  # K번째 저장 순간의 값을 반환

    # K번 저장이 발생하지 않았다면 -1 반환
    return -1

N, K = map(int, input().split())
array = list(map(int, input().split()))

print(insertion_sort(array, N, K))
