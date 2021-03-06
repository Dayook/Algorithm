# 3의 거듭 제곱수는 3을 b번 곱한 수를 의미하며 3b 형태로 표현합니다. 30 = 1이 성립하며, 31 = 3, 32 = 9, 33 = 27, 34 = 81... 모두 거듭 제곱수입니다.
# 3의 거듭 제곱수를 임의로 더하여 거듭 제곱수 사이에 들어가는 수를 만들 수 있습니다. 예를 들어,
#
# 4 = 1 + 3
# 31 = 27 + 3 + 1
# 입니다.
# 이때, 같은 거듭 제곱수를 2번 이상 더할 수는 없습니다. 이러한 규칙으로 만들어낼 수 있는 수와 3의 거듭 제곱수를 합쳐서 순서대로 배치하면
# 1, 3, 4, 9, 10...이 됩니다.
# 이렇게 배치한 숫자의 n번째 숫자가 무엇인지를 알려주는 함수
# solution 을 완성해주세요.
import math

def solution(n):
    answer = 0
    arr = [1, 3]
    ex = [1, 3, 4, 9, 10, 12, 13, 27, 28, 30, 31, 36, 37, 81]
    pow = [1, 2, 4, 8, 16]
    print(round(n ** (1/2)))
    if n == 1:
        return 1
    # n이 2 이상인 경우:

    # (len(pow) -1) 팩토리얼 수만큼의 -가 있는지 확인
    # 없으면 다음 pow[-1] * 3
    pow.append(pow[-1] * 3)

    return answer


solution(10)