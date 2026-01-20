from collections import deque

def solution(priorities, location):
    """
    priorities : 각 프로세스의 우선순위 리스트
    location   : 내가 알고 싶은 프로세스의 '처음 위치(index)'
    return     : 해당 프로세스가 몇 번째로 실행되는지 (1부터 시작)
    """

# 큐(Queue) 만들기

    # enumerate(priorities)
    # → (인덱스, 우선순위) 형태로 반환
    # 예: priorities = [2,1,3,2]
    # → (0,2), (1,1), (2,3), (3,2)
    #
    # (p, i) 형태로 바꾸는 이유:
    # → 우선순위(p)를 먼저 비교하기 쉽게 하기 위해
    #
    # deque를 쓰는 이유:
    # → 앞에서 꺼내고(popleft), 뒤에 넣는(append) 작업이 빠르기 때문
    q = deque((p, i) for i, p in enumerate(priorities))
    # 결과 예시:
    # deque([(2,0), (1,1), (3,2), (2,3)])

    executed = 0  # 지금까지 실행(종료)된 프로세스 수

    # 프로세스 실행 시뮬레이션

    while True:
        # 큐 맨 앞 프로세스를 하나 꺼냄
        cur_priority, cur_index = q.popleft()


        # 나보다 우선순위 높은 프로세스가 있는지 확인

        # q 안에 cur_priority 보다 큰 우선순위(p)가 하나라도 있으면 True
        if any(cur_priority < p for p, _ in q):
            # 더 중요한 프로세스가 있으므로
            # 지금 프로세스는 실행 못 하고 다시 큐 뒤로 감
            q.append((cur_priority, cur_index))
        else:
            # 현재 큐에서 가장 높은 우선순위 → 실행!
            executed += 1  # 실행 순서 +1

            # 찾던 프로세스인지 확인

            # cur_index는 "처음 위치"
            # location과 같다면 정답
            if cur_index == location:
                return executed
