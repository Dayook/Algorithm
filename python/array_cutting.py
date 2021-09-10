def solution(array, commands):
    # command 1 2 3 나누어서
    answer = []
    for command in commands:
        start = command[0]-1
        end = command[1]
        index = command[2] - 1
        arr = sorted(array[start:end])
        answer.append(arr[index])
    return answer

def solution2(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])