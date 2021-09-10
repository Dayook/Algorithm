import collections

def solution(participant, completion):
    answer = ''
    answer_list = participant[:]
    for p in participant:
        for c in completion:
            if p == c:
                answer_list.remove(p)
                completion.remove(c)
    answer = answer_list[0]
    print(answer)
    return answer

# def solution2(participant,completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[len(participant)-1]

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]


solution(["leo", "kiki", "eden"], ["eden", "kiki"]);
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]);
solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]);
