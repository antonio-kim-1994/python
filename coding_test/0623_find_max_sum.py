'''
- 문제
매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.
예를 들어, 아래와 같이 10일 간의 온도가 주어졌을 때

    3 -2 -4 -9 0 3 7 13 8 -3

모든 연속적인 이틀간의 온도의 합이 가장 큰 값은 21이다.
또 다른 예로 위와 같은 온도가 주어졌을 때, 모든 연속적인 5일 간의 온도의 합이 가장 큰 값은 31이다.
매일 측정한 온도가 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오.

- 입력
첫째 줄에는 두 개의 정수 N과 K가 한 개의 공백을 사이에 두고 순서대로 주어진다.
첫 번째 정수 N은 온도를 측정한 전체 날짜의 수이다.
N은 2 이상 100,000 이하이다.

두 번째 정수 K는 합을 구하기 위한 연속적인 날짜의 수이다.
K는 1과 N 사이의 정수이다.
둘째 줄에는 매일 측정한 온도를 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다.
이 수들은 모두 -100 이상 100 이하이다.

- 출력
첫째 줄에는 입력되는 온도의 수열에서 연속적인 K일의 온도의 합이 최대가 되는 값을 출력한다.

예제 입력 1                   | 예제 출력 1
10 2                        | 21
3 -2 -4 -9 0 3 7 13 8 -3    |

예제 입력 2                   | 예제 출력 2
10 5                        | 31
3 -2 -4 -9 0 3 7 13 8 -3    |

'''

'''
map 함수
    - 주어진 함수와 이터러블(반복 가능한 객체)을 인자로 받아, 이터러블의 각 요소에 주어진 함수를 적용한 결과를 반환하는 함수(맵 객체로 반환)
    - 예시: map(function, iterable, ...)
        * function: 이터러블의 각 요소에 적용할 함수.
	    * iterable: 함수가 적용될 이터러블 객체 (리스트, 튜플, 문자열 등)
'''

# N: 측정일 수
# K: 합계 간격
def find_max_sum(N, K, temperatures):
    current_sum = sum(temperatures[:K]) # 0부터 K번째 까지의 합
    max_sum = current_sum

    for i in range(K, N):
        current_sum += temperatures[i] - temperatures[i - K] # 한 칸씩 옮기며 합계 값을 비교
        if current_sum > max_sum:
            max_sum = current_sum

N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

result = find_max_sum(N, K, temperatures)
print(result)