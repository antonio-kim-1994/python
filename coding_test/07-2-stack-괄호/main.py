# def judge_bracket(list_input: list):
#     for i in range(len(list_input)):
#         left_count = list_input[i].count('(')
#         right_count = list_input[i].count(')')
#         if left_count != right_count:
#             print('NO')
#         else:
#             print('YES')
#     return
#
#
# line_number: int = int(input())
# bracket_list = []
#
# for _ in range(line_number):
#     bracket = input()
#     bracket_list.append(bracket)
#
# judge_bracket(bracket_list)

# for ~ else / while ~ else 확인

def judge_ps(ps: str):
    stack = []
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return ("NO")
            else:
                stack.pop()
    return "YES" if not stack else "NO"


line_number = int(input())
for _ in range(line_number):
    print(judge_ps(input().strip()))