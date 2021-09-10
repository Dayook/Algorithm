def solution(card, words):
    answer = []
    # word의 단어를 card 세 줄 모두 사용하여 완성하기
    for word in words:
        dup_card_1 = list(card[0])
        dup_card_2 = list(card[1])
        dup_card_3 = list(card[2])

        for alphabet in word:
            # 알파벳이 카드 덱에 있는지 확인
            is_in = True
            if alphabet in dup_card_1:
                dup_card_1.remove(alphabet)
            elif alphabet in dup_card_2:
                dup_card_2.remove(alphabet)
            elif alphabet in dup_card_3:
                dup_card_3.remove(alphabet)
            # 카드 덱에 없는 경우 아예 break
            else:
                is_in = False
                break

        if is_in == False or len(dup_card_1) == 8 or len(dup_card_2) == 8 or len(dup_card_3) == 8:
            continue
        else:
            answer.append(word)
    print(answer)
    if len(answer) == 0 :
        return ["-1"]
    return answer


solution(["ABACDEFG", "NOPQRSTU", "HIJKLKMM"], ["GPQM", "GPMZ", "EFU", "MMNA"])
