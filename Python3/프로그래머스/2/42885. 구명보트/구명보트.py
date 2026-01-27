'''
무거운 사람은 선택지가 적음, 
제일가벼운 + 제일 뚱뚱 조합으로 하는 게 최선 (나중에 가벼운사람 2명에서 탈 경우를 고려)
'''

def solution(people, limit):
    answer = 0
    # 일단정렬
    people.sort()
    # 포인터
    a=0
    b=len(people)-1 # 뚱뚱
    while a<b:
        if people[a]+people[b]<=limit:
            a+=1 # 다음 뚱뚱으로 포인터 바꿈
            answer+=1 # 두명이 한 보트에 탄 횟수 
        b-=1 # 덜뚱뚱
    # return answer : 두명 타는 것만 고려함
    return len(people)-answer
