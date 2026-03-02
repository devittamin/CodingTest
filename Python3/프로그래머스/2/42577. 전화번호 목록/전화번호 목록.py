def solution(phone_book):
    # 사전순으로 정렬하먼 바로 옆에 위치 
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        # 다음 번호가 현재 번호로 시작하면 접두어 
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True 