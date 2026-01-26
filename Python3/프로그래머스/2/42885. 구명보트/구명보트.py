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
            answer+=1 # 태움 
        b-=1 # 덜뚱뚱
    # return answer : 두명 타는 것만 고려함
    return len(people)-answer