def solution(n, lost, reserve): (n, 체육복 없는사람 ,여벌 있는사람 ) 

    lost_set = set(lost) # 나중에 중복제거 하기 위해 집합으로 
    reserve_set = set(reserve)

   
    both = lost_set & reserve_set # 교
 # 겹치는 사람  제거
    lost_set -= both 
    reserve_set -= both

    # 작은 번호부터 빌려주기 >> 그리디  : 왼 (i-1) -> 오 (i+1) 순서로 빌림 
    for x in sorted(lost_set):

        # 왼쪽한테 빌릴 수 있을 때 
        if x - 1 in reserve_set:
            reserve_set.remove(x - 1)
        # 오른쪽한테 빌릴 수 있을 때 
        elif x + 1 in reserve_set:
            reserve_set.remove(x + 1)

        # 둘 다 안 되면 수업 못 들음 
        else:
            n -= 1  # 끝까지 못 빌린 사람  1명 감소

    return n
