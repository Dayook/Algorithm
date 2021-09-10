# 문자열에서 일정한 간격으로 같은 문자열이 반복해서 나타난다면 이를 문자열의 주기라고 합니다. 예를 들어 문자열 "abababab"에서 문자열의 주기는 다음과 같이 세 가지가 있습니다.
#
# 문자열 "ab"가 네 번 반복해서 나타납니다.
# 문자열 "abab"가 두 번 반복해서 나타납니다.
# 문자열 "abababab"가 한 번 반복해서 나타납니다.
# 이때, 가능한 짧은 주기를 문자열의 주기로 정합니다. 따라서 위 문자열의 주기는 2가 됩니다.
# 문자열 s가 매개변수로 주어질 때, 문자열의 주기를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항

def solution(s):
    answer = 0
    arr = ""
    length = len(s)
    for i in s :
        arr += i
        if arr * (length // len(arr)) == s:
            break
    answer = len(arr)
    return answer

solution("abababab")
solution("abcabcabd")

