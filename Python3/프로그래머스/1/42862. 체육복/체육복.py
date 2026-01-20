

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



# 다른풀이 1 : 
# discard 는 remove 와 다르게 없어도 오류 안 뜸 !!! 
def solution(n, lost, reserve):
    r_lost = set(lost) - set(reserve)
    r_reserve = set(reserve) - set(lost)
    lost_num = len(r_lost)
    # print(dir(r_lost))
    for i in r_reserve:
        if i-1 in r_lost:
            r_lost.discard(i-1)
            lost_num -= 1
        elif i+1 in r_lost:
            r_lost.discard(i+1)
            lost_num -= 1
            
    return n - lost_num

# 다른 풀이 2 
def solution(n, lost, reserve):
    answer = 0
    #1. set으로 다시 저장하기
    lost = set(lost)
    reserve = set(reserve)
    
    #2. 교집합(잃어버렸는데 여벌도 있는 학생) 먼저 제거 
    if lost & reserve:
        common = lost & reserve #교집합은 한번 변수에 저장해두고 양쪽에서 제거해야함
        lost = lost - common
        reserve = reserve - common
     #3. 이제 빌려주기 (빌려줄 수 있는지 확인)
    for i in list(lost): #반복 중 set 변경하면 오류나기에 list로 방지 
        if i - 1 in reserve: # 앞번호 학생이 여벌 있으면 빌림
            reserve.remove(i-1) # 여벌 사용하기 
            lost.remove(i) # 체육복 문제 해결
            
        elif i + 1 in reserve: # 앞번호 x, 뒷번호 학생 여벌 있으면 빌림
            reserve.remove(i+1) # 여벌 사용하기 
            lost.remove(i) # 체육복 문제 해결
            
        else: # 앞/뒤 모두 여벌이 없으면 아무것도 못 함  
            pass
    # 체육복 입을 수 있는 학생 수 
    return n - len(lost)



