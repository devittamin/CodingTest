def solution(genres, plays):
    # 해시 사용
    # 장르를 key로 해서-> 장르별 총 재생수->장르별 노래 목록을 저장하기 위함

    total = {}   # 장르별 총 재생수
    songs = {}   # 장르별 노래 정보 (재생수, 고유번호)

    # 한 번만 돌면서 전부 저장
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]

        # 아직 없는 장르면 초기화
        if g not in total:
            total[g] = 0
            songs[g] = []

        # 총 재생수 누적
        total[g] += p

        # 해당 장르에 노래 추가
        songs[g].append((p, i))

    # 장르를 총 재생수 기준으로 내림차순 정렬
    genre_order = sorted(total.keys(), key=lambda g: total[g], reverse=True)

    answer = []

    # 재생수 많은 장르부터 처리
    for g in genre_order:

        # 장르 안에서는 재생수 많은 순 / 같으면 고유번호 작은 순
        songs[g].sort(key=lambda x: (-x[0], x[1]))

        answer.append(songs[g][0][1]) # 최대 두개만

        if len(songs[g]) > 1:
            answer.append(songs[g][1][1])

    return answer