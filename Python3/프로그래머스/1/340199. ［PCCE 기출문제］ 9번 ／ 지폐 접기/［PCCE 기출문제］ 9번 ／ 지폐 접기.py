def solution(wallet, bill):
    answer = 0
    
    w_min, w_max = sorted(wallet)
    b_min, b_max = sorted(bill)

    # 90도 회전 허용함 => 작은변<=작은변 AND 큰변<=큰변 이면 들어감
    while b_min > w_min or b_max > w_max:
        # 더 긴 쪽을 반으로 접.. 
        if b_max >= b_min:
            b_max //= 2
        else:
            b_min //= 2
        
        # 접고 나면 다시 작은거~ 큰거 정렬해서 비교 기준 유지
        b_min, b_max = sorted((b_min, b_max))
        answer += 1

    return answer
