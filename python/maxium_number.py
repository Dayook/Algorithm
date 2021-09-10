def solution(numbers):
    answer = ''
    arr = []
    for number in numbers:
        # number를 str로 변형
        arr.append(str(number))

    arr.sort(reverse=True)
    for i in range(len(arr)):
        answer += arr[i]
    return answer


solution([6,10,2]);
solution([3, 30, 34, 5, 9]);
