def solution(N, trees):
    answer = 0
    # 제일 낮은 x좌표
    # 제일 낮은 y좌표 구한다
    # x좌표 낮은데 y좌표 높은 경우

    # x 좌표 낮은 순으로 정렬
    sorted_tree = sorted(trees,reverse=False)
    lowest = N
    # y 좌표가 이전 좌표의 y보다 낮은 경우 경계에 걸림
    for tree in sorted_tree:
        if tree[1] < lowest:
            answer += 1
            lowest = tree[1]

    print(answer)
    return answer


solution(5, [[4, 3], [3, 1], [2, 2], [1, 4]])
solution(5, [[3, 3], [2, 2], [1, 1]])