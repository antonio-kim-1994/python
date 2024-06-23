'''
문제
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

입력
첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

예제 입력 1     | 예제 출력 1
2143          | 4321

예제 입력 2     | 예제 출력 2
999998999     | 999999998
'''

'''
Python에서 리스트를 정렬하는 방법에는 list.sort() 메서드와 sorted() 함수 두 가지 존재

1) sort 메서드
    예시: list.sort(key=None, reverse=False)
    적용 대상: 리스트 객체
    특징
    - 원본 리스트를 직접 정렬하여 변경
	- 정렬된 새로운 리스트를 반환하지 않는다.
	- key 매개변수를 사용하여 사용자 정의 정렬 기준을 지정
	- reverse=True로 설정하면 내림차순으로 정렬

2) sorted 함수
    예시: sorted(iterable, key=None, reverse=False)
    적용 대상: 모든 이터러블 (리스트, 튜플, 문자열 등)
    특징
    - 원본 이터러블을 변경하지 않는다.
    - 정렬된 새로운 리스트를 반환
    - key 매개변수를 사용하여 사용자 정의 정렬 기준을 지정
    - reverse=True로 설정하면 내림차순으로 정렬
'''

numbers = int(input())

sorted_numbers = sorted(numbers, reverse=True)

result = ''.join(sorted_numbers)
print(result)