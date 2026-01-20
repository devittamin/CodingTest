def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)

    # 1) 겹치는 학생 제거
    both = lost_set & reserve_set
    lost_set -= both
    reserve_set -= both

    # 2) 작은 번호부터 빌려주기
    for x in sorted(lost_set):
        if x - 1 in reserve_set:
            reserve_set.remove(x - 1)
        elif x + 1 in reserve_set:
            reserve_set.remove(x + 1)
        else:
            n -= 1  # 끝까지 못 빌린 학생 1명 감소

    return n
