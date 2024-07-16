'''
7
2
1
4
5
1
3
3
'''

def calculate_largest_rectangle(hist: list):
    max_area: int = 0
    index: int = 0
    index_list: list = []

    while index < len(hist):
        if not index_list or hist[index_list[-1]] <= hist[index]:
            index_list.append(index)
            index += 1
        else:
            large_index = index_list.pop()
            area = hist[large_index] * ((index - index_list[-1]) if index_list else index)



N = int(input())
histogram = [int(input()) for _ in range(N)]