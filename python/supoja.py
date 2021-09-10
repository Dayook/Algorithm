def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer_count = {1: 0, 2: 0, 3: 0}
    one_len = len(one)
    two_len = len(two)
    three_len = len(three)

    print(one_len)

    for i in range(len(answers)):
        if answers[i] == one[i % one_len]:
            answer_count[1] += 1
        if answers[i] == two[i % two_len]:
            answer_count[2] += 1
        if answers[i] == three[i % three_len]:
            answer_count[3] += 1

    max_score = max(answer_count.values())
    for key in answer_count.keys():
        if answer_count[key] == max_score:
            answer.append(key)
    return answer


solution([1, 2, 3, 4, 5])
