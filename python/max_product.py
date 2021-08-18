# 왼쪽, 오른쪽 카드 뭉치에서 한 장씩을 뽑았을 때 곱해서 나올 수 있는 가장 큰 수 구하기
def max_product(left_cards, right_cards):
    max = 0
    for i in left_cards:
        for j in right_cards:
            if i * j > max:
                max = i * j
    return max

# 다른 풀이
def max_product(left_cards, right_cards):
    # 현재까지 최댓값을 담기 위한 변수
    # 처음에는 임시로 각 리스트의 첫 번째 요소의 곱으로 설정
    max = left_cards[0] * right_cards[0]

    # 가능한 모든 조합을 보기 위한 중첩문
    for left in left_cards:
        for right in right_cards:
            # 현재까지의 최댓값과 지금 보고 있는 곱을 비교해서 더 큰 값을 max로 지정한다
            max = max(max, left * right)
    # 찾은 최댓값을 리턴한다
    return max_product

# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))