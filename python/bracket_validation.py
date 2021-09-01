# () {} []가 올바르게 짝지어져있는지 검증해보자.
# 대괄호 중괄호 소괄호 무관하게
# stack 공부를 하면 좀 도움이 될 거 같은데.

def bracket_validation(bracket_string):
    if len(bracket_string) == 0 :
        return True
    list = []

    for s in bracket_string:
        if s == '(' or s == '{' or s == '[':
            list.append(s)
        if s == ')':
            if list.count('(') > 0:
                list.remove('(')
            else:
                return False
        if s == '}':
            if list.count('{') > 0:
                list.remove('{')
            else:
                return False
        if s == ']':
            if list.count('[') > 0:
                list.remove('[')
            else:
                return False

    return len(list) == 0


print(bracket_validation('[[()())){}{}]'))
print(bracket_validation('[[[[]]]]]]]]]]]]]]]'))
print(bracket_validation('[](){}'))
print(bracket_validation('[()(){}{}]{{}}({})'))
