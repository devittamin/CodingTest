'''
ord('A')=65
66 > B
a~z 
'''

def solution(s, n):
    answer = ''
    for ch in s:
        if ch == ' ':
            answer += ' '
            continue
        if ch.isupper():
            kk = ord('A')
        else:
            kk = ord('a')
        pos = ord(ch) - kk # 알파벳위치 0~25 
        pos = pos + n   # 위치 + n
        pos = pos % 26 # 알파벳 26개 
        answer += chr(pos + kk)  # 문자로 변환

    return answer

