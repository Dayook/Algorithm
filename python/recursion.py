# 재귀 함수
def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)


countdown(5)


# 팩토리얼
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


factorial(4)
