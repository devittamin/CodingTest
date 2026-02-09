# 모든 차량이 최소 한 번은 단속카메라 만나야함 
# 최소 몇대 카메라를 설치해야하는지 >> 그리디 
# routes[i][0] : 들어간시점 / roues[i][1] : 나간시점 
# 여러개의 선분이 있을 때 그 선분들을 모두 포함하는 최소 개수의 점을 구하는 문제 >> 구간문제, 최소 점 커버문제, 대표 그리디 유형 .. 
# 차량은 구간이고 카메라는 점임. 모든 구간을 점으로 덮기 
# 구간문제 거의 다 그리디 
def solution(routes):
    routes.sort(key=lambda x: x[1])  # 차량 진출지점. 작은순대로 정렬 
    camera = -30001  # 진출 지점은 -30,000 이상 30,000 이하니까 
    answer = 0 # 설치한 카메라 개수 저장 
    
    for start, end in routes: # 정렬된 차량 하나씩 확인 
        if camera < start: # 카메라가 이 차량을 찍고있지않음녀 
            camera = end  # 카메라 설치 
            answer += 1
            
    return answer