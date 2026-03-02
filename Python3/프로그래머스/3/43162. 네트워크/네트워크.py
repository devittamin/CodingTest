def solution(n, computers):
    # 각 컴퓨터 방문 여부 저장
    visited = [False] * n

    # DFS 함수
    def dfs(node):
        # 현재 컴퓨터 방문 처리
        visited[node] = True

        # 현재 컴퓨터와 연결된 다른 컴퓨터들 확인
        for j in range(n):
            # 연결되어 있고 아직 방문하지 않았다면
            if computers[node][j] == 1 and not visited[j]:
                dfs(j)

    answer = 0

    # 모든 컴퓨터를 하나씩 확인
    for i in range(n):
        # 아직 방문하지 않은 컴퓨터라면
        # 새로운 네트워크 시작
        if not visited[i]:
            dfs(i)        # 연결된 컴퓨터들 전부 방문
            answer += 1   # 네트워크 개수 증가

    return answer