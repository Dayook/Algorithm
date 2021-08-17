# 이진 탐색을 recurstion으로 해결해보자.

def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    mid_index = (start_index + end_index) // 2
    if element == some_list[mid_index]:
        return mid_index
    if element < some_list[mid_index]:
        return binary_search(element, some_list, start_index, mid_index)
    if element > some_list[mid_index]:
        return binary_search(element, some_list, mid_index, end_index)
    


    # 코드를 작성하세요.

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))