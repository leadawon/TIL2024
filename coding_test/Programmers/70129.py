def count_1(s):
    cnt = 0
    for v in s:
        if v=='1':
            cnt += 1
    return cnt


def solution(s):
    answer = [0,0]
    last_len = len(s)
    while s!='1':
        cnt=count_1(s)
        answer[1] += last_len - cnt
        s=bin(cnt)[2:]
        answer[0] += 1
        last_len = len(s)
    return answer