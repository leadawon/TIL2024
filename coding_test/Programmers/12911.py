def numtoones(num):
    ones = 0
    for v in bin(num)[2:]:
        if v=='1':
            ones+=1
    return ones

def solution(n):
    answer = 0
    ones = numtoones(n)
    cnt = 1
    while True:
        if numtoones(n+cnt) == ones:
            answer = n+cnt
            break
        cnt+=1
    return answer