from collections import deque
def solution(priorities, location):
    answer = 0
    dq = deque()
    for i,p in enumerate(priorities):
        dq.append((i,p))
    spr = sorted(priorities)
    cnt = 1
    while True:
        tg = dq.popleft()
        if tg[1] < spr[-1]:
            dq.append(tg)
        elif tg[0]==location:
            answer = cnt
            break
        else:
            spr.pop()
            cnt+=1
            
    
    
    return answer