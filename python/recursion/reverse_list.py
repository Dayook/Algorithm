# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    if len(some_list) <= 1:
        return some_list
    return [some_list[-1]] + flip(some_list[:-1])
    # or just some_list[-1:]

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

"""
시간 복잡도
리스트 some_list 길이를 n이라고 하자.
base case => O(1)
recursive case =>
some_list[-1:] = [some_list[-1]]은 시간 복잡도가 O(1)이고
some_list[:-1]은 시간 복잡도가 O(n-1)
따라서 재귀적 부분을 제외한 flip의 시간 복잡도는 O(n)

flip 함수가 호출되는 횟수 : n번
따라서 총 시간 복잡도는 O(n제곱)번

"""

# 풀이 2번
def flip(some_list):
    mid_idx = len(some_list) // 2
    if len(some_list) == 1:
        return some_list
    return flip(some_list[mid_idx:]) + flip(some_list[:mid_idx])

some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)