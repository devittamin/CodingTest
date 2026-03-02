from collections import deque
def solution(progresses, speeds):
    # 각 작업이 끝날때까지 며칠걸리는지 계산
    days = []
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        day = (remain + speeds[i] - 1) // speeds[i]
        days.append(day)

    q = deque(days)     # 완료 날짜를 큐에 넣어 앞에서부터 처리
    answer = []

    while q: # 큐 빌때까지 
        gijun = q.popleft() # 맨 앞을 기준으로 
        count = 1

        while q and q[0] <=gijun: # 뒷잡업이 기준 날짜보다 빨리 끝나면 같이 
            q.popleft()
            count += 1
        answer.append(count) # 배포한 개수 저장 

    return answer