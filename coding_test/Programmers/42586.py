from collections import deque
def solution(progresses, speeds):
    answer = []
    
    pg = deque(progresses)
    sp = deque(speeds)
    
    while pg:
        while pg[0] < 100:
            for i in range(len(pg)):
                pg[i] += sp[i]
        cnt = 0
        while pg and pg[0] >= 100:
            pg.popleft()
            sp.popleft()
            cnt += 1
        answer.append(cnt)
    
    return answer