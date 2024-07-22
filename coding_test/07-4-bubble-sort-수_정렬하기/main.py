def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


line_count = int(input())
numbers = [ int(input()) for _ in range(line_count) ]
result = bubble_sort(numbers)

for i in range(line_count):
    print(result[i])
