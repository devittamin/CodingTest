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


# 수빈님 풀이 : 덱했을때 pop 하면 O(1) / list 하면 시간초과 

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort() #정렬하기
    people = deque(people)
    #print (people) 
    
    while len(people) > 0:
        if len(people) == 1: # 뚱뚱이 애초부터 뺌
            people.pop()
            answer = answer + 1 
        else:
            if people[0] + people[-1] > limit:
                people.pop()
                answer = answer + 1
            else:
                people.popleft()  # 그래서 popleft 로
                # people.pop(0) 제일 둘러보고 왼쪽 빼면 O(n)-> 시간초과 pop(0)는 느리당 
                people.pop()
                answer = answer + 1

    return answer
