

# 미래를 계산하지 않고 지금 당장 한 명을 살리는 선택을 반복해도 전체 최적이 되는 구조라서 그리디

def solution(n, lost, reserve): (수업 들을 수 있는 학생 수 , 체육복 없는사람 ,여벌 있는사람 ) 

    lost_set = set(lost) # 나중에 중복제거 하기 위해 집합으로 
    reserve_set = set(reserve)
    both = lost_set & reserve_set # 교

 # 겹치는 사람  제거
    lost_set -= both # 체육복 없는 사람 
    reserve_set -= both # 진짜 빌려줄 수 있는사람 

    # 작은 번호부터 빌려주기 >> 그리디  : 왼 (i-1) -> 오 (i+1) 순서로 빌림 
    for x in sorted(lost_set):

   
        # 왼쪽(x-1)을 먼저 확인하는 이유
        # x-1은 번호가 더 작음 이미 for문에서 지나갔거나 앞으로 다시 기회 x  
        
        # 왼쪽한테 빌릴 수 있을 때 
        if x - 1 in reserve_set:  # 여벌 체육복 가지고 있으면 
            reserve_set.remove(x - 1)  # reserve_set 에서 삭제 
        # 오른쪽한테 빌릴 수 있을 때 
        elif x + 1 in reserve_set:    # 여벌 체육복 가지고 있으면 
            reserve_set.remove(x + 1)     # reserve_set 에서 삭제 

        # 둘 다 안 되면 수업 못 들음 
        else:
            n -= 1  # 끝까지 못 빌린 사람  1명 감소

    return n


# discard 는 없어도 오류 안 뜸 
