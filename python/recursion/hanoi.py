# 하노이의 탑 규칙
# 1. 한 번에 한 원판만 옮길 수 있다
# 2. 큰 원판이 작은 원판 위에 있어서는 안 된다.

# hanoi는 파라미터로 원판수 num_disks, 게임을 시작하는 기둥 번호 start_peg
# 목표로 하는 기둥번호 end_peg를 받고 재귀적으로 문제를 풀어 원판을 옮기는 순서를 모두 출력합니다.

def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    other_peg = 6 - start_peg - end_peg
    if num_disks == 1:
        return move_disk(num_disks, start_peg, end_peg)
    if num_disks >= 2:
        return hanoi(num_disks-1, start_peg, other_peg), move_disk(num_disks, start_peg, end_peg), hanoi(num_disks-1, other_peg, end_peg)
    # 코드를 입력하세요.


# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)