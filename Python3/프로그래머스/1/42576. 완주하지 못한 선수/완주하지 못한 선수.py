'''
문제 조건 
참여선수 왕많음 
참여선수 string > 해시 
완주 여부 > true false boolvalue 로 하면될거같은데 동명이인있어서 count 로 해야함 
'''

def solution(participant, completion):
    count={} # 이름 ->사람수 저장할 해시 테이블 
    
    for name in participant:
        count[name]=count.get(name,0)+1  # 예외처리 한번에 
        
    for name in completion : # 완주한사람 뺌 
        count[name]-=1
        
    for name in count : # 남아있는사람 계산 
        if count[name]==1:
            return name 


'''
count 

'''