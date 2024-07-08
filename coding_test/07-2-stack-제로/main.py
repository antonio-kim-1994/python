def sum_numbers(arr: list):
    stack = []
    for i in arr:
        if i == 0:
            if stack:
                stack.pop()
        else:
            stack.append(i)

    return sum(stack)


line_count = int(input())
number = [int(input().strip()) for _ in range(line_count)]
print(sum_numbers(number))