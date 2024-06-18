'''
[입력] : 1번째 줄에 숫자의 개수 N(1 <= N <= 100), 2번째 줄에 숫자 N개가 공백 없이 주어진다.
[출력]
예제 입력     | 예제 출력
1           | 1
1           |

5           | 15
54321       |

11          | 46
10987654321 |
'''

numbers = list(input())
sum = 0

for i in numbers:
    sum += int(i) # innput() : input 값은 string으로 취급한다.

print(sum)