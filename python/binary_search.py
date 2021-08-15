# 2진 탐색은 정렬된 리스트를 전제로 합니다.
# 1회 비교를 거칠 때마다 탐색 범위를 절반으로 줄여나가는 이진탐색 알고리즘을 작성해보세요


# 1. for문
def binary_search(element, some_list):
    start_idx = 0
    end_idx = len(some_list) - 1
    mid_idx = (start_idx + end_idx) // 2

    for i in range(len(some_list) // 2 + 1):
        if some_list[mid_idx] == element:
            return mid_idx
        elif some_list[mid_idx] < element:
            start_idx = mid_idx + 1
        else :
            end_idx = mid_idx - 1
        mid_idx = (start_idx + end_idx) // 2
    return None

#2. while문
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
