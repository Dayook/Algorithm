def solution(weights, head2head):
    answer = []
    total = len(head2head)
    # 1. 승률 순으로 정렬
    win = []
    vs_heavy = []
    for i in range(len(weights)):
        for head in head2head:
            if head == 'W':
                

        win.append(head2head[i].count('W') / total - head2head[i].count('N'))
        weights[i]

    # 2. 승률 동점인 경우 무거운 복서 이긴 횟수대로
    # 3. 2번 동점인 경우 몸무게가 무거운 순
    # 4. 3번까지 동일하면 번호가 앞번호인대로


    return answer

solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"])
